#!/usr/bin/env python
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "watchdog",
#   "websockets",
# ]
# ///

import asyncio
import http.server
import os
import socketserver
import subprocess
import sys
import threading
import time
import webbrowser
from pathlib import Path

import websockets
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

PORT = 8000
WEBSOCKET_PORT = 8765


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, websocket_server):
        self.websocket_server = websocket_server

    def on_modified(self, event):
        if event.src_path.endswith(".org"):
            print(f"{event.src_path} has been modified. Rebuilding...")
            self.process_file(event.src_path)
        elif event.src_path.endswith("style.css"):
            print(f"{event.src_path} has been modified. Reloading...")
            if self.websocket_server:
                asyncio.run(self.websocket_server.reload())

    def on_created(self, event):
        if event.src_path.endswith(".org"):
            print(f"{event.src_path} has been created. Building...")
            self.process_file(event.src_path)

    def process_file(self, org_file_path):
        org_file = Path(org_file_path)
        html_file = org_file.with_suffix(".html")

        try:
            subprocess.run(["pandoc", str(org_file), "-s", "--css=style.css", "--toc", "--section-divs", "--metadata=lang:en", "--number-sections", "-o", str(html_file)], check=True)
            self.inject_livereload_script(html_file)
            if self.websocket_server:
                asyncio.run(self.websocket_server.reload())
            print(f"Successfully built {html_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error running pandoc: {e}", file=sys.stderr)
        except FileNotFoundError:
            print("Error: pandoc not found. Please make sure it is installed and in your PATH.", file=sys.stderr)

    def inject_livereload_script(self, html_file):
        with open(html_file, "r+") as f:
            content = f.read()
            if "ws://localhost:8765" in content:
                return  # Script already injected

            script = f"""
            <script>
              const socket = new WebSocket('ws://localhost:{WEBSOCKET_PORT}');
              socket.onmessage = function(event) {{
                if (event.data === 'reload') {{
                  location.reload();
                }}
              }};
            </script>
            </body>
            """
            content = content.replace("</body>", script)
            f.seek(0)
            f.write(content)
            f.truncate()


class WebSocketServer:
    def __init__(self, host="localhost", port=WEBSOCKET_PORT):
        self.clients = set()
        self.host = host
        self.port = port

    async def handler(self, websocket):
        self.clients.add(websocket)
        try:
            await websocket.wait_closed()
        finally:
            self.clients.remove(websocket)

    async def serve(self):
        server = await websockets.serve(self.handler, self.host, self.port)
        await server.wait_closed()

    async def reload(self):
        if self.clients:
            await asyncio.gather(*[client.send("reload") for client in self.clients])


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith(".html"):
            try:
                with open(self.path.lstrip('/'), 'r') as f:
                    content = f.read()
                
                html_files = [f for f in os.listdir('.') if f.endswith('.html')]
                file_list_html = "<div class='file-list'><ul>"
                for html_file in sorted(html_files):
                    file_list_html += f'<li><a href="/{html_file}">{html_file}</a></li>'
                file_list_html += "</ul></div>"

                # Inject the file list and wrap content in <main>
                content = content.replace("<body>", f"<body>\n{file_list_html}\n<main>")
                content = content.replace("</body>", "</main>\n</body>")
                
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            except FileNotFoundError:
                self.send_error(404, "File not found")
        else:
            super().do_GET()


def run_web_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()

def main():
    observer = None
    try:
        # Check for pandoc
        try:
            subprocess.run(["pandoc", "--version"], check=True, capture_output=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Error: pandoc not found. Please make sure it is installed and in your PATH.", file=sys.stderr)
            sys.exit(1)

        # Initial build
        print("Performing initial build of all .org files...")
        for org_file in Path(".").glob("*.org"):
            FileChangeHandler(None).process_file(str(org_file)) # Don't need websocket server for initial build

        # Start WebSocket server
        websocket_server = WebSocketServer()
        websocket_thread = threading.Thread(target=asyncio.run, args=(websocket_server.serve(),), daemon=True)
        websocket_thread.start()

        # Start file watcher
        event_handler = FileChangeHandler(websocket_server)
        observer = Observer()
        observer.schedule(event_handler, ".", recursive=False)
        observer.start()

        # Start web server
        web_server_thread = threading.Thread(target=run_web_server, daemon=True)
        web_server_thread.start()

        # Open the main page in a browser
        webbrowser.open_new_tab(f"http://localhost:{PORT}/README.html")

        print("Watching for file changes... Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        if observer:
            observer.stop()
            observer.join()



if __name__ == "__main__":
    main()
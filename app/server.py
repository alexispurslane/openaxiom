#!/usr/bin/env python
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "flask",
#   "flask-socketio",
#   "watchdog",
#   "pandoc",
# ]
# ///

import os
import subprocess
import sys
import threading
import time
import webbrowser
from pathlib import Path

from flask import Flask, send_from_directory, jsonify
from flask_socketio import SocketIO, emit
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Configuration
PORT = 8000
HOST = "localhost"

# Create Flask app
import os
app = Flask(__name__, 
            static_folder=os.path.join(os.path.dirname(__file__), "static"))
app.config["SECRET_KEY"] = "openaxiom-secret-key"

# Create SocketIO instance
socketio = SocketIO(app, cors_allowed_origins="*")

# File watcher
class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, socketio_instance):
        self.socketio_instance = socketio_instance

    def on_modified(self, event):
        if event.src_path.endswith(".org"):
            print(f"{event.src_path} has been modified. Rebuilding...")
            self.process_file(event.src_path)
        elif event.src_path.endswith("style.css"):
            print(f"{event.src_path} has been modified. Reloading...")
            # Emit reload event to all connected clients (if socketio_instance is available)
            if self.socketio_instance:
                self.socketio_instance.emit("reload", {"data": "reload"})

    def on_created(self, event):
        if event.src_path.endswith(".org"):
            print(f"{event.src_path} has been created. Building...")
            self.process_file(event.src_path)

    def process_file(self, org_file_path):
        org_file = Path(org_file_path)
        html_file = org_file.with_suffix(".html")
        output_path = os.path.join(os.path.dirname(__file__), "html", html_file.name)

        try:
            subprocess.run([
                "pandoc", 
                str(org_file), 
                "-s", 
                "--css=/static/style.css", 
                "--toc", 
                "--section-divs", 
                "--metadata=lang:en", 
                "--number-sections", 
                "-o", 
                output_path
            ], check=True)
            
            # Emit reload event to all connected clients (if socketio_instance is available)
            if self.socketio_instance:
                self.socketio_instance.emit("reload", {"data": "reload"})
            print(f"Successfully built {html_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error running pandoc: {e}", file=sys.stderr)
        except FileNotFoundError:
            print("Error: pandoc not found. Please make sure it is installed and in your PATH.", file=sys.stderr)

# Routes
@app.route("/")
def index():
    # Redirect to README.html by default
    return serve_html("README.html")

@app.route("/<path:filename>")
def serve_html(filename):
    # Check if the requested file is an HTML file
    if not filename.endswith(".html"):
        # If not, serve it from static directory
        return send_from_directory(app.static_folder, filename)
    
    # Serve HTML files with injected navigation and live reload
    html_dir = os.path.join(os.path.dirname(__file__), "html")
    html_file_path = os.path.join(html_dir, filename)
    
    # Check if file exists
    if not os.path.exists(html_file_path):
        # Return 404 if file doesn't exist
        return f"<h1>File not found</h1><p>The file {filename} was not found.</p>", 404
    
    # Read the HTML file
    with open(html_file_path, "r") as f:
        content = f.read()
    
    # Get all HTML files for navigation
    html_files = [f for f in os.listdir(html_dir) if f.endswith(".html")]
    html_files.sort()
    
    # Create navigation bar
    file_list_html = "<div class='file-list'><ul>"
    for html_file in html_files:
        # Highlight the current file
        if html_file == filename:
            file_list_html += f'<li><strong>{html_file}</strong></li>'
        else:
            file_list_html += f'<li><a href="/{html_file}">{html_file}</a></li>'
    file_list_html += "</ul></div>"
    
    # Inject navigation bar and live reload script
    if "<body>" in content:
        # Insert file list after <body> tag and wrap content in <main>
        content = content.replace("<body>", f"<body>\n{file_list_html}\n<main>", 1)
    
    # Add live reload script before </body> tag and close <main> tag
    if "</body>" in content:
        script = """
        </main>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
        <script>
          const socket = io();
          socket.on('reload', function(data) {
            location.reload();
          });
        </script>
        </body>
        """
        content = content.replace("</body>", script, 1)
    
    # Return the modified content
    return content

@app.route("/api/files")
def list_files():
    html_files = [f for f in os.listdir(os.path.join(os.path.dirname(__file__), "html")) if f.endswith(".html")]
    html_files.sort()
    return jsonify(html_files)

# Serve static files
@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# SocketIO event handlers
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

# Initial build function
def initial_build():
    print("Performing initial build of all .org files...")
    for org_file in Path(".").glob("*.org"):
        FileChangeHandler(None).process_file(str(org_file))

# Observer setup
observer = None
file_handler = None

def start_file_watcher():
    global observer, file_handler
    # Start file watcher
    file_handler = FileChangeHandler(socketio)
    observer = Observer()
    observer.schedule(file_handler, ".", recursive=False)
    observer.start()

def stop_file_watcher():
    global observer
    if observer:
        observer.stop()
        observer.join()

# Main function
def main():
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
            FileChangeHandler(None).process_file(str(org_file))  # Don't need socketio for initial build

        # Start file watcher
        start_file_watcher()

        # Open the main page in a browser
        webbrowser.open_new_tab(f"http://{HOST}:{PORT}/")

        # Run the Flask app
        print(f"Serving at http://{HOST}:{PORT}")
        socketio.run(app, host=HOST, port=PORT, debug=True, use_reloader=False, allow_unsafe_werkzeug=True)
        
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        stop_file_watcher()

if __name__ == "__main__":
    main()

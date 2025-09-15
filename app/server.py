
import os
import subprocess
import sys
import threading
import time
import webbrowser
import json
import shutil
from pathlib import Path

from flask import Flask, send_from_directory, jsonify, request, render_template, send_file
from flask_socketio import SocketIO, emit
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Import weasyprint for PDF generation
from weasyprint import HTML, CSS

# Import search module
import sys
import os
sys.path.append(os.path.dirname(__file__))
from search import index_org_files, search_index

# Configuration
PORT = 8000
HOST = "localhost"

# Create Flask app
import os
app = Flask(__name__, 
            static_folder=os.path.join(os.path.dirname(__file__), "static"),
            template_folder=os.path.join(os.path.dirname(__file__), "templates"))
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
            # Regenerate search index
            index_org_files()
        elif event.src_path.endswith("style.css"):
            print(f"{event.src_path} has been modified. Reloading...")
            # Emit reload event to all connected clients (if socketio_instance is available)
            if self.socketio_instance:
                self.socketio_instance.emit("reload", {"data": "reload"})

    def on_created(self, event):
        if event.src_path.endswith(".org"):
            print(f"{event.src_path} has been created. Building...")
            self.process_file(event.src_path)
            # Regenerate search index
            index_org_files()

    def process_file(self, org_file_path):
        org_file = Path(org_file_path)
        html_file = org_file.with_suffix(".html")
        output_path = os.path.join(os.path.dirname(__file__), "html", html_file.name)
        template_path = os.path.join(os.path.dirname(__file__), "templates", "pandoc_fragment.html")

        try:
            subprocess.run([
                "pandoc", 
                str(org_file), 
                "-s",
                "--template", 
                template_path,
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

def get_org_title(org_file_path):
    """Extract the title from an org file."""
    try:
        with open(org_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Extract title from first line if it's a heading
        if content.startswith("#+TITLE:"):
            title_line = content.split("\n", 1)[0]
            return title_line[8:].strip()  # Remove "#+TITLE:" prefix
        else:
            # Fallback to filename
            return Path(org_file_path).stem.replace("_", " ").title()
    except Exception as e:
        print(f"Error extracting title from {org_file_path}: {e}")
        return Path(org_file_path).stem.replace("_", " ").title()

def get_sorted_html_files():
    """Get HTML files sorted according to TOC order."""
    # Load the table of contents order
    toc_file = os.path.join(os.path.dirname(__file__), "..", "toc_order.json")
    try:
        with open(toc_file, "r") as f:
            toc_data = json.load(f)
        html_files = [f.replace(".org", ".html") for f in toc_data["files"]]
    except Exception as e:
        print(f"Error loading TOC order: {e}")
        # Fallback to alphabetical order
        toc_order = []
    
    # Get titles for each file
    html_files_with_titles = []
    for f in html_files:
        org_file_path = os.path.join(os.path.dirname(__file__), "..", f.replace(".html", ".org"))
        if os.path.exists(org_file_path):
            title = get_org_title(org_file_path)
        else:
            title = f.replace(".html", "").replace("_", " ").title()
        html_files_with_titles.append((f, title))
    
    return html_files_with_titles

# Routes
@app.route("/")
def index():
    # Redirect to openaxiom_manual.html by default
    return serve_html("openaxiom_manual.html")

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
    
    # Get all HTML files for navigation with their titles, sorted according to TOC
    html_files_with_titles = get_sorted_html_files()
    
    # Get title for current page
    org_file_path = os.path.join(os.path.dirname(__file__), "..", filename.replace(".html", ".org"))
    if os.path.exists(org_file_path):
        title = get_org_title(org_file_path)
    else:
        title = filename.replace(".html", "").replace("_", " ").title()
    
    # Render template with content
    return render_template("page.html", 
                          content=content,
                          title=title,
                          html_files_with_titles=html_files_with_titles,
                          current_file=filename)

@app.route("/api/files")
def list_files():
    html_files = [f for f in os.listdir(os.path.join(os.path.dirname(__file__), "html")) if f.endswith(".html")]
    html_files.sort()
    return jsonify(html_files)

@app.route("/api/search")
def search():
    query = request.args.get("q", "")
    if not query:
        return jsonify([])
    results = search_index(query)
    return jsonify(results)

@app.route("/api/print")
def print_manual():
    import tempfile
    try:
        # Get HTML files sorted according to TOC order
        html_files_with_titles = get_sorted_html_files()
        html_files = [f[0] for f in html_files_with_titles]
        
        # Create a temporary directory in the system temp folder
        temp_dir = tempfile.mkdtemp()
        combined_html_file = os.path.join(temp_dir, "combined_manual.html")
        
        # Read the CSS file
        css_file = os.path.join(os.path.dirname(__file__), "static", "style.css")
        with open(css_file, "r") as f:
            css_content = f.read()
        
        # Combine all HTML files in order
        with open(combined_html_file, "w") as outfile:
            outfile.write("<!DOCTYPE html>\n<html>\n<head>\n")
            outfile.write('<meta charset="utf-8">\n')
            outfile.write('<style>\n')
            outfile.write(css_content)
            outfile.write('\n</style>\n')
            outfile.write("</head>\n<body>\n")
            
            for i, html_file in enumerate(html_files):
                html_path = os.path.join(os.path.dirname(__file__), "html", html_file)
                if os.path.exists(html_path):
                    with open(html_path, "r") as infile:
                        content = infile.readlines()
                        # Extract the main content (excluding header, nav, etc.)
                        
                        outfile.write('<div style="page-break-before: always;"></div>\n')
                        title = get_org_title(os.path.join(os.path.dirname(__file__), "..", Path(html_file).with_suffix('.org')))
                        outfile.write(f'<h1>{title}</h1>')
                        # Write the main content
                        outfile.write("\n".join(content))
            
            outfile.write("\n</body>\n</html>")
        
        # Generate PDF using weasyprint
        pdf_file = os.path.join(temp_dir, "openaxiom_manual.pdf")
        
        # Create HTML object and CSS object for weasyprint
        html = HTML(filename=combined_html_file, base_url='http://localhost:8000', media_type='print')
        css = CSS(filename=css_file)
        
        # Generate PDF
        html.write_pdf(pdf_file, stylesheets=[css], presentational_hints=True)
        
        # Send the PDF file
        return send_file(pdf_file, as_attachment=True, download_name="openaxiom_manual.pdf")
        
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return f"Error generating PDF: {str(e)}", 500
    finally:
        # Clean up temp directory
        try:
            if 'temp_dir' in locals():
                shutil.rmtree(temp_dir)
        except Exception as e:
            print(f"Error cleaning up temp directory: {e}")

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
    # Create initial search index
    index_org_files()

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

        # Create initial search index
        index_org_files()

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

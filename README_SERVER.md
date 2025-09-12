# OpenAxiom Manual Server

This is a Flask-based server for serving the OpenAxiom TTRPG manual with live reloading capabilities.

## Features

- Serves HTML files generated from Org-mode documents
- Live reloading when Org files or CSS are modified
- Automatic generation of HTML files from Org files using Pandoc
- File listing and navigation interface

## Requirements

- Python 3.8+
- Pandoc
- UV (for dependency management)

## Installation

1. Install the required dependencies using UV:
   ```
   uv pip install flask flask-socketio watchdog pandoc
   ```

   Or if you prefer to use the pyproject.toml file:
   ```
   uv pip install .
   ```

## Usage

Run the server using UV:
```
uv run app/server.py
```

The server will:
1. Generate HTML files from all Org files in the current directory
2. Start a web server on http://localhost:8000
3. Automatically open the default browser
4. Watch for changes to Org files and CSS, rebuilding and reloading as needed

## Directory Structure

- `app/templates/` - Flask templates
- `app/static/` - Static files (CSS, JS, images)
- `app/html/` - Generated HTML files (created automatically)
- `*.org` - Source Org files in the root directory

## How It Works

1. When the server starts, it processes all Org files in the root directory using Pandoc to generate HTML files in `app/html/`
2. The main page (`/`) shows a file listing and embeds the selected HTML file in an iframe
3. File watcher monitors for changes to Org files and CSS
4. When an Org file is modified, it's reprocessed with Pandoc
5. When CSS is modified, the page is reloaded
6. WebSocket connection provides live reloading in the browser

## Customization

You can modify the following variables in `app/server.py`:
- `PORT` - Server port (default: 8000)
- `HOST` - Server host (default: localhost)
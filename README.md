# OpenAxiom TTRPG

OpenAxiom is a free and open source, universal tabletop roleplaying game (TTRPG) engine inspired by GURPS. Rather than providing a complete game with predefined settings, characters, or monsters, OpenAxiom focuses purely on the core mechanics needed for any TTRPG. It's designed to be setting and genre agnostic, with modular "packs" that can be composed to simulate the setting, characters, and events /you/ want to play. It is designed to be simulationist not by providing specific rules for every possible thing (at least not in its core) but by providing powerful, advanced abstract systems that can be used to simulate a logic of action and consequences, which players can then compose together and map specific setting concepts onto to arrive at meaningful simulations of anything they can imagine. It's designed to provide substantial mechanical crunch at the same time as avoiding complex math, by using more logic-based crunch than mathematical formulas. It's also designed to provide meaningful simulation and crunch for every area of play equally, from physical, to social, to mental.

## Licensing

The OpenAxiom project uses separate licenses for the rules content and the code:

- All prose for this TTRPG (the rules, in both org and html form, and introductions to those rules, etc.) are licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. See [LICENSE.rules.txt](LICENSE.rules.txt) for the full license text.

- All code in this project is licensed under the Mozilla Public License 2.0. See [LICENSE.code.txt](LICENSE.code.txt) for the full license text.

## Manual Server

This repository also includes a Flask-based server for serving the OpenAxiom TTRPG manual with enhanced capabilities. This is not strictly necessary, as the manual is just plain text and regular html, but it will give GMs an improved experience.

### Features

- Serves HTML files generated from Org-mode documents
- Live reloading when Org files or CSS are modified
- Automatic generation of HTML files from Org files using Pandoc
- File listing and navigation interface
- Full-text search functionality
- Dice roller functionality that can do skill checks and evaluate them based on game rules
- Allow you to print well-formatted, print-friendly PDFs from the HTML

### Requirements

- Python 3.8+
- Pandoc
- UV (for dependency management)

### Installation

Install the required dependencies using UV:
```bash
uv sync
```

### Usage

Run the server using UV:

```bash
uv run openaxiom-server
```

The server will:
1. Generate HTML files from all Org files in the current directory
2. Start a web server on http://localhost:8000
3. Automatically open the default browser
4. Watch for changes to Org files and CSS, rebuilding and reloading as needed

### Directory Structure

- `app/templates/` - Flask templates
- `app/static/` - Static files (CSS, JS, images)
- `app/html/` - Generated HTML files (created automatically)
- `*.org` - Source Org files in the root directory

### Customization

You can modify the following variables in `app/server.py`:
- `PORT` - Server port (default: 8000)
- `HOST` - Server host (default: localhost)

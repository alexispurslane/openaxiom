#!/bin/bash

# ==============================================================================
# OpenAxiom SRD - Org-mode to Markdown Converter & Watcher
#
# This script manages the conversion of .org files from the `src` directory
# to .md files in the `docs` directory, which MkDocs uses to build the site.
#
# It can be run in two modes:
#
# 1. Default (no arguments): `./convert.sh`
#    - Checks for dependencies (pandoc, watchexec).
#    - Performs an initial conversion of all .org files.
#    - Starts watchexec to monitor the `src` folder for changes.
#
# 2. Convert-Only: `./convert.sh convert`
#    - Runs the conversion logic just once. This is the mode
#      that watchexec calls internally.
# ==============================================================================

# --- Helper function to check for required command-line tools ---
check_deps() {
  local deps=("pandoc" "watchexec")
  echo "Checking for required dependencies..."
  for dep in "${deps[@]}"; do
    if ! command -v "$dep" &> /dev/null; then
      echo "Error: Required command '$dep' is not installed." >&2
      echo "Please install it to continue." >&2
      exit 1
    fi
  done
  echo "All dependencies found."
}

# --- Core function to convert all .org files to .md ---
convert_files() {
  echo "--- Running conversion at $(date) ---"
  
  # Find all .org files in src, and convert them one by one
  find src -name "*.org" | while read -r infile; do
    # Determine the output filename, preserving the directory structure
    outfile="docs/${infile#src/}"
    outfile="${outfile%.org}.md"

    # Ensure the output directory exists
    mkdir -p "$(dirname "$outfile")"

    # Extract the title from the org file
    title=$(grep "^#+TITLE:" "$infile" | sed 's/^#+TITLE:[[:space:]]*//')

    # Convert the file using pandoc with our custom heading numbering filter
    pandoc --from=org --to=markdown_mmd-mmd_header_identifiers --lua-filter=number_sections.lua --output="$outfile" "$infile"

    echo "Converted $infile -> $outfile"
  done
  echo "--- Conversion complete ---"
}

# --- Main Script Logic ---
# Use a case statement to handle different modes.

case "$1" in
  # Mode 2: If the first argument is 'convert', just run the function.
  convert)
    convert_files
    ;;

  # Mode 1: Default behavior if no arguments are given.
  *)
    # Step 1: Check if pandoc and watchexec are installed.
    check_deps

    # Step 2: Perform an initial conversion to make sure the `docs` folder is up to date.
    echo "Performing initial conversion of all .org files..."
    convert_files

    # Step 3: Start the watcher.
    # It will watch the 'src' directory for changes to any '.org' file.
    # When a change is detected, it will call this script again with the 'convert' argument.
    echo
    echo "✅ Setup complete. Starting file watcher..."
    echo "   Watching for changes in the 'src' directory."
    echo "   In another terminal, run 'mkdocs serve' to start the live-reloading website."
    echo
    watchexec --exts org --watch src -- sh "$0" convert
    ;;
esac

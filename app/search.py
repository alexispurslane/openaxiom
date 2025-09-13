#!/usr/bin/env python
"""
Search module for indexing and searching .org files.
"""
import os
import re
import subprocess
import tempfile
from pathlib import Path
from bs4 import BeautifulSoup
from whoosh.index import create_in, open_dir, exists_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from whoosh.analysis import StandardAnalyzer

# Schema for the search index
schema = Schema(
    title=TEXT(stored=True),
    path=ID(stored=True),
    content=TEXT(stored=True, analyzer=StandardAnalyzer())
)

INDEX_DIR = "search_index"

def get_index_dir():
    """Get the directory where the search index is stored."""
    return os.path.join(os.path.dirname(__file__), INDEX_DIR)

def create_index():
    """Create a new search index."""
    index_dir = get_index_dir()
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)
    return create_in(index_dir, schema)

def get_index():
    """Get the search index, creating it if it doesn't exist."""
    index_dir = get_index_dir()
    if not exists_in(index_dir):
        return create_index()
    return open_dir(index_dir)

def org_to_plain_text(org_file_path):
    """Convert an org file to plain text using pandoc."""
    try:
        # Create a temporary file for the output
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as tmp_file:
            tmp_path = tmp_file.name
        
        # Convert org to plain text using pandoc
        subprocess.run([
            "pandoc",
            str(org_file_path),
            "-t", "plain",
            "-o", tmp_path
        ], check=True, capture_output=True)
        
        # Read the plain text content
        with open(tmp_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Clean up the temporary file
        os.unlink(tmp_path)
        
        return content
    except Exception as e:
        print(f"Error converting {org_file_path} to plain text: {e}")
        # Fallback to reading the org file directly
        try:
            with open(org_file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e2:
            print(f"Error reading {org_file_path} directly: {e2}")
            return ""

def get_section_id_for_position(org_file_path, query_string):
    """Get the section ID for the first occurrence of query terms in the main content."""
    try:
        # Convert org file path to HTML file path
        html_file_path = org_file_path.replace('.org', '.html')
        html_full_path = os.path.join(os.path.dirname(__file__), 'html', os.path.basename(html_file_path))
        
        # Check if HTML file exists
        if not os.path.exists(html_full_path):
            return None
            
        # Parse the HTML file
        with open(html_full_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
        
        # Remove the table of contents from consideration
        toc = soup.find('nav', id='TOC')
        if toc:
            toc.decompose()
        
        # Split query into terms
        terms = query_string.lower().split()
        
        # Find all sections in order
        sections = soup.find_all('section', id=True)
        
        # Look for the most specific section containing any of the query terms
        # We want the deepest/nested section that contains the term
        best_section = None
        best_depth = -1
        
        for section in sections:
            # Get all text content from this section
            section_text = section.get_text().lower()
            
            # Check if any term appears in this section
            found_term = False
            for term in terms:
                if term in section_text:
                    found_term = True
                    break
            
            if found_term:
                # Calculate depth by counting ancestor sections
                depth = 0
                parent = section.parent
                while parent:
                    if parent.name == 'section':
                        depth += 1
                    parent = parent.parent
                
                # If this is deeper than our current best, use it
                if depth > best_depth:
                    best_depth = depth
                    best_section = section
        
        # If we found a specific section, return its ID
        if best_section:
            return best_section.get('id')
                
        # Fallback: return the first section ID if we can't find a specific match
        if sections:
            return sections[0].get('id')
                
        return None
    except Exception as e:
        print(f"Error getting section ID for {org_file_path}: {e}")
        return None

def index_org_files():
    """Index all .org files in the current directory as plain text."""
    # Create a fresh index (this automatically clears any existing content)
    index = create_index()
    writer = index.writer()
    
    # Index each .org file
    for org_file in Path(".").glob("*.org"):
        try:
            # Convert org file to plain text
            content = org_to_plain_text(org_file)
            
            # Extract title from first line if it's a heading
            title = org_file.stem.replace("_", " ").title()
            if content.startswith("# "):
                title = content.split("\n", 1)[0][2:].strip()
            
            # Add document to index
            writer.add_document(
                title=title,
                path=str(org_file),
                content=content
            )
        except Exception as e:
            print(f"Error indexing {org_file}: {e}")
    
    writer.commit()
    print("Search index updated successfully.")

def search_index(query_string):
    """Search the index for the given query string."""
    try:
        index = get_index()
        searcher = index.searcher()
        parser = QueryParser("content", schema=index.schema)
        
        # Parse the query string as a phrase or set of terms
        query = parser.parse(query_string)
        results = searcher.search(query, limit=20)
        
        # Enable highlighting with custom formatter
        from whoosh.highlight import HtmlFormatter
        results.fragmenter.charlimit = None  # Don't limit the size of documents to scan
        results.fragmenter.maxchars = 200    # Limit the size of fragments
        results.fragmenter.surround = 50     # Context around matches
        results.formatter = HtmlFormatter(tagname="span", classname="highlight")  # Use our CSS class
        
        # Return results as a list of dictionaries
        search_results = []
        for result in results:
            # Get highlighted fragment
            highlighted_content = result.highlights("content")
            
            # If no highlights were found, fall back to a snippet
            if not highlighted_content:
                highlighted_content = result["content"][:200] + "..." if len(result["content"]) > 200 else result["content"]
            
            # Get section ID for the match using the original query string
            section_id = get_section_id_for_position(result["path"], query_string)
            
            search_results.append({
                "title": result["title"],
                "path": result["path"],
                "content": highlighted_content,
                "section_id": section_id,
                "query": query_string
            })
        return search_results
    except Exception as e:
        print(f"Error searching index: {e}")
        return []

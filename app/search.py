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

def get_section_id_for_position(org_file_path, match_text):
    """Get the section ID for a given match text by parsing the corresponding HTML."""
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
        
        # Find all text elements containing the match text
        # We'll search for the text in the HTML content
        import re
        escaped_text = re.escape(match_text)
        pattern = re.compile(escaped_text, re.IGNORECASE)
        
        # Find all text nodes containing the match
        matching_elements = []
        for element in soup.find_all(text=pattern):
            # Get the parent element that contains this text
            parent = element.parent
            matching_elements.append(parent)
        
        # If we found matching elements, find the closest section ID
        if matching_elements:
            # Get the first matching element
            element = matching_elements[0]
            # Traverse up the tree to find the closest section with an ID
            while element:
                if element.name == 'section' and element.get('id'):
                    return element.get('id')
                element = element.parent
                
        # Fallback: return the first section ID if we can't find a specific match
        sections = soup.find_all('section', id=True)
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

def highlight_terms(text, terms, org_file_path, context_length=150):
    """Extract context around search terms in text and return it without any highlighting markup."""
    # Create a regex pattern to find any of the terms
    pattern = '|'.join(re.escape(term) for term in terms)
    regex = re.compile(pattern, re.IGNORECASE)
    
    # Find all matches
    matches = list(regex.finditer(text))
    
    if not matches:
        # If no matches, return beginning of text
        return text[:200] + "..." if len(text) > 200 else text, None
    
    # Get context around the first match
    first_match = matches[0]
    start = max(0, first_match.start() - context_length)
    end = min(len(text), first_match.end() + context_length)
    
    # Extract context
    context = text[start:end]
    
    # Add ellipsis if we're not at the beginning or end
    if start > 0:
        context = "..." + context
    if end < len(text):
        context = context + "..."
    
    # Try to find the section ID that contains this match
    match_text = first_match.group()
    section_id = get_section_id_for_position(org_file_path, match_text)
    
    return context, section_id

def search_index(query_string):
    """Search the index for the given query string."""
    try:
        index = get_index()
        searcher = index.searcher()
        parser = QueryParser("content", schema=index.schema)
        
        # Parse the query string as a phrase or set of terms
        query = parser.parse(query_string)
        results = searcher.search(query, limit=20)
        
        # Split query into terms for highlighting
        terms = query_string.split()
        
        # Return results as a list of dictionaries
        search_results = []
        for result in results:
            content, section_id = highlight_terms(result["content"], terms, result["path"])
            search_results.append({
                "title": result["title"],
                "path": result["path"],
                "content": content,
                "section_id": section_id,
                "query": query_string  # Pass the original query for highlighting
            })
        return search_results
    except Exception as e:
        print(f"Error searching index: {e}")
        return []
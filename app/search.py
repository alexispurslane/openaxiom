#!/usr/bin/env python
"""
Search module for indexing and searching .org files.
"""
import os
import re
from pathlib import Path
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

def index_org_files():
    """Index all .org files in the current directory."""
    # Create a fresh index (this automatically clears any existing content)
    index = create_index()
    writer = index.writer()
    
    # Index each .org file
    for org_file in Path(".").glob("*.org"):
        try:
            with open(org_file, "r", encoding="utf-8") as f:
                content = f.read()
            
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

def highlight_terms(text, terms, context_length=100):
    """Highlight search terms in text and return context around them."""
    # Create a regex pattern to find the terms
    pattern = '|'.join(re.escape(term) for term in terms)
    regex = re.compile(pattern, re.IGNORECASE)
    
    # Find all matches
    matches = list(regex.finditer(text))
    
    if not matches:
        # If no matches, return beginning of text
        return text[:200] + "..." if len(text) > 200 else text
    
    # Get context around the first match
    first_match = matches[0]
    start = max(0, first_match.start() - context_length)
    end = min(len(text), first_match.end() + context_length)
    
    # Extract context
    context = text[start:end]
    
    # Highlight terms in context
    highlighted = regex.sub(r'**\g<0>**', context)
    
    # Add ellipsis if we're not at the beginning or end
    if start > 0:
        highlighted = "..." + highlighted
    if end < len(text):
        highlighted = highlighted + "..."
    
    return highlighted


def get_text_fragment(text, terms):
    """Generate a text fragment for linking to specific text in a document."""
    # Create a regex pattern to find the terms
    pattern = '|'.join(re.escape(term) for term in terms)
    regex = re.compile(pattern, re.IGNORECASE)
    
    # Find all matches
    matches = list(regex.finditer(text))
    
    if not matches:
        # If no matches, return empty string
        return ""
    
    # Get the first match
    first_match = matches[0]
    match_text = first_match.group()
    
    # Clean up the text for URL encoding
    # Remove extra whitespace and limit length
    clean_text = re.sub(r'\s+', ' ', match_text.strip())
    
    # URL encode the match text for the fragment
    import urllib.parse
    encoded_text = urllib.parse.quote(clean_text)
    
    return f"#:~:text={encoded_text}"

def search_index(query_string):
    """Search the index for the given query string."""
    try:
        index = get_index()
        searcher = index.searcher()
        parser = QueryParser("content", schema=index.schema)
        query = parser.parse(query_string)
        results = searcher.search(query, limit=20)
        
        # Split query into terms for highlighting
        terms = query_string.split()
        
        # Return results as a list of dictionaries
        return [
            {
                "title": result["title"],
                "path": result["path"],
                "content": highlight_terms(result["content"], terms),
                "fragment": get_text_fragment(result["content"], terms)
            }
            for result in results
        ]
    except Exception as e:
        print(f"Error searching index: {e}")
        return []


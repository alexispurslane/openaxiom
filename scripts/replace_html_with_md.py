#!/usr/bin/env python3

import os
import re

# Directory containing the org files
src_dir = "../src"

# Function to replace .html with .md in a file
def replace_html_with_md(file_path):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace .html with .md in links
    updated_content = re.sub(r'\.html(?=[#\]])', '.md', content)
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"Updated {file_path}")

# Walk through all .org files in the src directory
for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith('.org'):
            file_path = os.path.join(root, file)
            replace_html_with_md(file_path)

print("All .html references have been replaced with .md in org files.")
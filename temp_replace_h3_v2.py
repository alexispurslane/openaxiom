import re

file_path = '/Users/alexispurslane/Documents/ttrpg/character_creation.org'

with open(file_path, 'r') as f:
    content = f.read()

# Scenario 1: Heading followed by regular text
# Matches '*** Heading', then a newline, then any text *not* starting with '#+BEGIN_QUOTE'.
# re.MULTILINE is needed for '^' to match the start of each line.
# re.DOTALL is NOT used here, so '.' does not match newlines.
content = re.sub(r'^\*\*\* (.*?)\n(?!#\+BEGIN_QUOTE)(.+)', r'**\1:** \2', content, flags=re.MULTILINE)

# Scenario 2: Heading followed by a quote block
# Matches '*** Heading', then a newline, then an empty line, then '#+BEGIN_QUOTE' and everything until the end of the quote block.
# re.MULTILINE and re.DOTALL are used here.
content = re.sub(r'^\*\*\* (.*?)\n\n(#\+BEGIN_QUOTE.*?)', r'**\1:**\n\n\2', content, flags=re.MULTILINE | re.DOTALL)

with open(file_path, 'w') as f:
    f.write(content)

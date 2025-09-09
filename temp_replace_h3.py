import re

file_path = '/Users/alexispurslane/Documents/ttrpg/character_creation.org'

with open(file_path, 'r') as f:
    content = f.read()

# Scenario 1: Heading followed by regular text
# This regex matches '*** Heading', then a newline, then any text *not* starting with '#+BEGIN_QUOTE'.
# re.DOTALL is needed for '.*' to match newlines in the following text.
# re.MULTILINE is needed for '^' to match the start of each line.
content = re.sub(r'^\*\*\* (.*?)\n(?!#\+BEGIN_QUOTE)(.*)', r'**\1:** \2', content, flags=re.MULTILINE | re.DOTALL)

# Scenario 2: Heading followed by a quote block
# This regex matches '*** Heading', then a newline, then '#+BEGIN_QUOTE' and everything until the end of the quote block.
content = re.sub(r'^\*\*\* (.*?)\n(#\+BEGIN_QUOTE.*?)', r'**\1:**\n\2', content, flags=re.MULTILINE | re.DOTALL)

with open(file_path, 'w') as f:
    f.write(content)


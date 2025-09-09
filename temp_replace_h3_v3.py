import re

file_path = '/Users/alexispurslane/Documents/ttrpg/character_creation.org'

with open(file_path, 'r') as f:
    content = f.read()

# Step 1: Transform all '*** Heading' to '**Heading:'
# This is a simple replacement that doesn't care about what follows.
content = re.sub(r'^\*\*\* (.*)', r'**\1:**', content, flags=re.MULTILINE)

# Step 2: For headings followed by text (not a quote block), move the text to the same line
# This pattern looks for a bolded heading ending with a colon, followed by a newline,
# and then any text *not* starting with '#+BEGIN_QUOTE'. It then puts the text on the same line.
content = re.sub(r'(\**.*?:)\n(?!#\+BEGIN_QUOTE)(.*)', r'\1 \2', content, flags=re.MULTILINE)

with open(file_path, 'w') as f:
    f.write(content)

import re

file_path = '/Users/alexispurslane/Documents/ttrpg/character_creation.org'

with open(file_path, 'r') as f:
    content = f.read()

# Pass 1: Replace `*** Heading` with `**Heading:**`
content = re.sub(r'^\*\*\* (.*)', r'**\1:**', content, flags=re.MULTILINE)

# Pass 2: Remove newline after bolded heading if followed by text (not empty line or quote block)
# Pattern: `(**Heading:)
(?!$)(?!#+BEGIN_QUOTE)(.*)`
# Replacement: `**Heading:** **Text**`
# `(?!$)` ensures it's not followed by an empty line.
pattern_pass2 = r'(\*\*.*?:)\n(?!$)(?!#\\+BEGIN_QUOTE)(.*)'
content = re.sub(pattern_pass2, r'\1 \2', content, flags=re.MULTILINE)

with open(file_path, 'w') as f:
    f.write(content)

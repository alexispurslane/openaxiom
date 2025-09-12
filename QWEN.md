# Project Guidelines for OpenAxiom TTRPG Rules

This document outlines the meta-rules for writing the OpenAxiom tabletop RPG rules.

## Formatting

The TTRPG rules will be formatted using Emacs Org-mode. This ensures consistency and readability within the Emacs environment.

## Sentence Structure and Clarity

Rule sentences must be simple, short, and clear. Each sentence should be easily understood by any reader. Avoid complex sentence structures. Em-dashes and semicolons are not permitted within the text.

## Tone and Prose

The tone of the rules should remain calm and neutral. The prose must flow nicely, creating a smooth reading experience for the player. Avoid abrupt transitions or jarring language.

## Noun Usage

Nouns will be used frequently instead of pronouns. This practice enhances clarity and reduces ambiguity regarding the subject of a sentence. The rule text will clearly state the actor or object.

## Heading Hierarchy

Rule sections will employ a simple heading hierarchy. This hierarchy will be limited to two or three levels deep at any given time. This structure maintains organization without excessive nesting.

## Lists

Bullet points and numbered lists will be used sparingly. The rule text will primarily rely on continuous prose for explanations. Lists are to be avoided unless absolutely necessary for presenting distinct, short items.

## Gameplay Examples

Gameplay examples will be enclosed in quote blocks.

## Cross-References

When writing new rules, automatically look up and link relevant sections from elsewhere in the manual. This ensures consistency and helps readers navigate between related concepts. Use descriptive links that clearly indicate what the reader will find at the destination. Link to specific sections by getting the heading's anchor link ID from the corresponding .html page and linking to ./the-page#the-id, *not* using org's internal linking system.

## Python Scripts

Python scripts in this project use **only** UV for dependency management. Scripts with dependencies should include a UV script header:
```
# /// script
# dependencies = [
#     "package1",
#     "package2",
# ]
# ///
```
To run a script with dependencies, use: `uv run script.py`

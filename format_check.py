import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure we don't have broken tags
if content.count("<div") != content.count("</div"):
    print("Warning: Unmatched div tags")

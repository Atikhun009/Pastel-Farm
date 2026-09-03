import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We will manipulate the file in chunks or write a fully new state management if needed.
# Since the script might be too long to write in one go, I'll do it sequentially.

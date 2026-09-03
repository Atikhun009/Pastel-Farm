import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add id to the tabs container wrapper
content = content.replace('<!-- Right Column: Interactive Tabs -->\n            <div class="w-full">', '<!-- Right Column: Interactive Tabs -->\n            <div id="view-tabs-container" class="w-full hidden">')

# wait, view-tabs-container is hidden by default? Yes, if farm is the default tab. Wait, which tab is default?
# Let's see the end of the script to see if a tab is switched by default.

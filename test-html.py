import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the grid classes from the main area
content = content.replace('<div class="grid grid-cols-1 lg:grid-cols-12 gap-6 relative z-10">', '<div class="space-y-6 relative z-10">')
content = content.replace('<div class="lg:col-span-8 space-y-6">', '<div id="view-farm" class="space-y-6">')
content = content.replace('<div class="lg:col-span-4 h-full">', '<div class="h-full">')

# But wait, there is a section inside lg:col-span-4 that has the tabs. We want to move the tabs menu outside of it, above the views.

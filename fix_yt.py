import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace display:none with absolute positioning offscreen
content = content.replace('<div id="yt-player" style="display:none;"></div>', '<div id="yt-player" style="position:absolute; width:1px; height:1px; top:-9999px; left:-9999px; opacity:0;"></div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


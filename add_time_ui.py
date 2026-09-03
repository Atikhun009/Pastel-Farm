import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add time-layer
content = content.replace('<div id="weather-layer" class="weather-overlay"></div>', '<div id="time-layer" style="position:fixed; top:0; left:0; right:0; bottom:0; pointer-events:none; z-index:-1; transition: background-color 1s ease;"></div>\n    <div id="weather-layer" class="weather-overlay"></div>')

# 2. Add time UI to header
old_header = '<div id="ui-season" class="text-sm font-semibold text-pink-800 bg-pink-100/80 px-3 py-0.5 rounded-full shadow-sm border border-white transition-all">🌸 ฤดูใบไม้ผลิ</div>'
new_header = old_header + '\n                            <div id="ui-time" class="hidden text-sm font-semibold text-amber-800 bg-amber-100/80 px-3 py-0.5 rounded-full shadow-sm border border-white transition-all">☀️ 06:00</div>'
content = content.replace(old_header, new_header)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

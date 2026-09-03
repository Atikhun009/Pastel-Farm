import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(r'class=\"', 'class="')
content = content.replace(r'y-1\"', 'y-1"')
content = content.replace(r'pointer\"', 'pointer"')
content = content.replace(r'allowed\"', 'allowed"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


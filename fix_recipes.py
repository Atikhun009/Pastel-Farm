import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("meat: 1", "egg: 1")
content = content.replace("salt: 1", "herb: 1")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

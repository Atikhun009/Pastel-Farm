import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("${state.level * 1000}", "<span id='diamond-gold-reward'>1000</span>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

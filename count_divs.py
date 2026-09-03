import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Opening:", content.count("<div"))
print("Closing:", content.count("</div"))

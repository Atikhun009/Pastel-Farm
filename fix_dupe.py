import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace multiple occurrences of auto_planter definition with a single one
pattern = r"(auto_planter: \{[^\}]+\},\s*)+"
replacement = r"auto_planter: { id: 'auto_planter', name: 'หุ่นยนต์ปลูกผัก', emoji: '🌱', desc: 'ปลูกเมล็ดพันธุ์เดิมอัตโนมัติ (ถ้ามี)', buyPrice: 4000, maxLevel: 1, priceMult: 1, type: 'feature' },\n            "
content = re.sub(pattern, replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

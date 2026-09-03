import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'const MAX_PLOTS = \d+;', 'const MAX_PLOTS = 27;', content)
content = re.sub(r'const MAX_PENS = \d+;', 'const MAX_PENS = 23;', content)

# Fix fruit icons
content = content.replace("'มะละกอ', emoji: '🍈'", "'กล้วย', emoji: '🍌'") # Rename papaya to Banana because there is no papaya emoji
content = content.replace("'มะนาว', emoji: '🍋'", "'มะนาว', emoji: '🍋‍🟩'") # Change to green lemon

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

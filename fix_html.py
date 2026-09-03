import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Tailwind script
content = re.sub(r'<script src="https://cdn.tailwindcss.com">.*?</script>', '<script src="https://cdn.tailwindcss.com"></script>', content, flags=re.DOTALL)

# Fix Confetti script
content = re.sub(r'<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js">.*?</script>', '<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>', content, flags=re.DOTALL)

# Fix Youtube script
content = re.sub(r'<script src="https://www.youtube.com/iframe_api">.*?</script>', '<script src="https://www.youtube.com/iframe_api"></script>', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


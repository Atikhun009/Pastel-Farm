import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_style = """        .glass {
            background: rgba(255, 255, 255, 0.4);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.5);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05);
            border-radius: 1.5rem;
            position: relative;
            overflow: hidden;
            z-index: 1;
        }"""

new_style = """        .glass {
            background: rgba(255, 255, 255, 0.4);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.5);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05);
            border-radius: 1.5rem;
            position: relative;
            overflow: hidden;
            z-index: 1;
            transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }

        #plots-container .glass:hover,
        #pens-container .glass:hover {
            transform: scale(1.05);
            box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.15);
            z-index: 10;
        }"""

if old_style in content:
    content = content.replace(old_style, new_style)
    print("Style updated successfully")
else:
    print("Style not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


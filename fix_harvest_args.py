import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("function harvest(plotId) {", "function harvest(plotId, isAuto = false) {")
content = content.replace("function collectAnimal(penId) {", "function collectAnimal(penId, isAuto = false) {")

content = content.replace("showAlert('โรงนาเต็ม!', 'ไม่สามารถเก็บผลผลิตได้ โปรดอัปเกรดโรงนาหรือขายของ', '📦');", "if(!isAuto) showAlert('โรงนาเต็ม!', 'ไม่สามารถเก็บผลผลิตได้ โปรดอัปเกรดโรงนาหรือขายของ', '📦');")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

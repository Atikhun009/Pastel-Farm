import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_capacity_check = """                if (!checkBarnCapacity(amount)) {
                    if(!isAuto) showAlert('โรงนาเต็ม!', 'ไม่สามารถเก็บผลผลิตได้ โปรดอัปเกรดโรงนาหรือขายของ', '📦');
                    return;
                }"""

new_capacity_check = """                if (!checkBarnCapacity(amount)) {
                    if (checkBarnCapacity(1)) {
                        amount = 1;
                        doubleDropStr = ' (ที่เต็ม!)';
                    } else {
                        if(!isAuto) showAlert('โรงนาเต็ม!', 'ไม่สามารถเก็บผลผลิตได้ โปรดอัปเกรดโรงนาหรือขายของ', '📦');
                        return;
                    }
                }"""

content = content.replace(old_capacity_check, new_capacity_check)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

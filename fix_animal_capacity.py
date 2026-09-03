import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_collect = """                if (Math.random() < dropChance) {
                    amount = 2;
                    doubleDropStr = ' 🍀เบิ้ล!';
                    if (pen.happiness && Math.random() < 0.5) {
                        pen.happiness -= 5; // consume some happiness on double drop
                        if (pen.happiness < 0) pen.happiness = 0;
                    }
                }
                
                state.inventory.products[product] = (state.inventory.products[product] || 0) + amount;"""

new_collect = """                if (Math.random() < dropChance) {
                    amount = 2;
                    doubleDropStr = ' 🍀เบิ้ล!';
                    if (pen.happiness && Math.random() < 0.5) {
                        pen.happiness -= 5; // consume some happiness on double drop
                        if (pen.happiness < 0) pen.happiness = 0;
                    }
                }
                
                if (!checkBarnCapacity(amount)) {
                    if(!isAuto) showAlert('โรงนาเต็ม!', 'ไม่สามารถเก็บผลผลิตได้ โปรดอัปเกรดโรงนาหรือขายของ', '📦');
                    return;
                }
                
                state.inventory.products[product] = (state.inventory.products[product] || 0) + amount;"""

content = content.replace(old_collect, new_collect)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

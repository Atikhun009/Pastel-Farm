import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 3. Modify harvest
old_harvest = """                if (state.upgrades && state.upgrades.magic_beans) {
                    if (Math.random() < state.upgrades.magic_beans * 0.02) {
                        amount = 2;
                        bonusStr = ' ✨ถั่ววิเศษ!';
                    }
                }
                
                state.inventory.products[product] = (state.inventory.products[product] || 0) + amount;"""

new_harvest = """                if (state.upgrades && state.upgrades.magic_beans) {
                    if (Math.random() < state.upgrades.magic_beans * 0.02) {
                        amount = 2;
                        bonusStr = ' ✨ถั่ววิเศษ!';
                    }
                }
                
                if (!checkBarnCapacity(amount)) {
                    showAlert('โรงนาเต็ม!', 'ไม่สามารถเก็บผลผลิตได้ โปรดอัปเกรดโรงนาหรือขายของ', '📦');
                    return;
                }
                
                state.inventory.products[product] = (state.inventory.products[product] || 0) + amount;"""

content = content.replace(old_harvest, new_harvest)

# 4. Modify collectAnimal
old_collect = """                if (Math.random() < dropChance) {
                    amount = 2;
                    doubleDropStr = ' 🍀เบิ้ล!';
                    if (pen.happiness && Math.random() < 0.5) {
                        pen.happiness -= 5; // consume some happiness on double drop
                    }
                }
                
                state.inventory.products[product] = (state.inventory.products[product] || 0) + amount;"""

new_collect = """                if (Math.random() < dropChance) {
                    amount = 2;
                    doubleDropStr = ' 🍀เบิ้ล!';
                    if (pen.happiness && Math.random() < 0.5) {
                        pen.happiness -= 5; // consume some happiness on double drop
                    }
                }
                
                if (!checkBarnCapacity(amount)) {
                    showAlert('โรงนาเต็ม!', 'ไม่สามารถเก็บผลผลิตได้ โปรดอัปเกรดโรงนาหรือขายของ', '📦');
                    return;
                }
                
                state.inventory.products[product] = (state.inventory.products[product] || 0) + amount;"""

content = content.replace(old_collect, new_collect)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

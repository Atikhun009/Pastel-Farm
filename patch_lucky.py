import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_lucky = """                // Happiness gives chance for double drop (100 happiness = 50% chance)
                if (pen.happiness && Math.random() < (pen.happiness / 200)) {
                    amount = 2;
                    doubleDropStr = ' 🍀เบิ้ล!';
                    pen.happiness -= 5; // consume some happiness on double drop
                    if (pen.happiness < 0) pen.happiness = 0;
                }"""

new_lucky = """                // Happiness gives chance for double drop (100 happiness = 50% chance)
                let dropChance = (pen.happiness || 0) / 200;
                if (state.upgrades && state.upgrades.lucky_hand) {
                    dropChance += (state.upgrades.lucky_hand * 0.02);
                }
                
                if (Math.random() < dropChance) {
                    amount = 2;
                    doubleDropStr = ' 🍀เบิ้ล!';
                    if (pen.happiness && Math.random() < 0.5) {
                        pen.happiness -= 5; // consume some happiness on double drop
                        if (pen.happiness < 0) pen.happiness = 0;
                    }
                }"""

content = content.replace(old_lucky, new_lucky)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


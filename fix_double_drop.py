import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update harvest
old_harvest = """                // Base drop
                let amount = 1;
                let bonusStr = '';
                
                // Random bonus from Green Thumb
                if (state.upgrades && state.upgrades.green_thumb) {
                    if (Math.random() < state.upgrades.green_thumb * 0.005) {
                        amount = 2;
                        bonusStr = ' 🍀เบิ้ล!';
                    }
                }"""

new_harvest = """                // Base drop
                let amount = 1;
                let bonusStr = '';
                
                // Random bonus from Green Thumb
                if (state.upgrades && state.upgrades.green_thumb) {
                    if (Math.random() < state.upgrades.green_thumb * 0.005) {
                        amount = 2;
                        bonusStr = ' 🍀เบิ้ล!';
                    }
                }
                
                // Double Drop Buff
                if (state.activeBuffs && state.activeBuffs.doubleDropEnd && Date.now() < state.activeBuffs.doubleDropEnd) {
                    amount = 2;
                    bonusStr = ' 🍀บัฟเบิ้ล!';
                }"""
content = content.replace(old_harvest, new_harvest)


# Update collectAnimal
old_collect = """                // Happiness gives chance for double drop (100 happiness = 50% chance)
                let dropChance = (pen.happiness || 0) / 200;
                if (state.upgrades && state.upgrades.lucky_hand) {
                    dropChance += (state.upgrades.lucky_hand * 0.005);
                }
                
                if (Math.random() < dropChance) {
                    amount = 2;
                    doubleDropStr = ' 🍀เบิ้ล!';
                    if (pen.happiness && Math.random() < 0.5) {
                        pen.happiness -= 5; // consume some happiness on double drop
                        if (pen.happiness < 0) pen.happiness = 0;
                    }
                }"""

new_collect = """                // Happiness gives chance for double drop (100 happiness = 50% chance)
                let dropChance = (pen.happiness || 0) / 200;
                if (state.upgrades && state.upgrades.lucky_hand) {
                    dropChance += (state.upgrades.lucky_hand * 0.005);
                }
                
                if (Math.random() < dropChance) {
                    amount = 2;
                    doubleDropStr = ' 🍀เบิ้ล!';
                    if (pen.happiness && Math.random() < 0.5) {
                        pen.happiness -= 5; // consume some happiness on double drop
                        if (pen.happiness < 0) pen.happiness = 0;
                    }
                }
                
                // Double Drop Buff
                if (state.activeBuffs && state.activeBuffs.doubleDropEnd && Date.now() < state.activeBuffs.doubleDropEnd) {
                    amount = 2;
                    doubleDropStr = ' 🍀บัฟเบิ้ล!';
                }"""

content = content.replace(old_collect, new_collect)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_breeder = """                        const bonusGold = Math.floor(PRODUCTS[product].basePrice * amount * 0.5);
                        state.gold += Math.floor(bonusGold * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 1.5 : 1));
                        bonusGoldStr = ` +${bonusGold} 🪙`;"""

new_breeder = """                        let bonusGold = Math.floor(PRODUCTS[product].basePrice * amount * 0.5);
                        if (state.rebirths && state.rebirths > 0) bonusGold *= (1 + state.rebirths);
                        const finalBonusGold = Math.floor(bonusGold * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 2 : 1));
                        state.gold += finalBonusGold;
                        bonusGoldStr = ` +${finalBonusGold} 🪙`;"""

content = content.replace(old_breeder, new_breeder)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

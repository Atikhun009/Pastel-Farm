import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("state.gold += sellPrice;", "state.gold += Math.floor(sellPrice * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 1.5 : 1));")
content = content.replace("state.gold += bonusGold;", "state.gold += Math.floor(bonusGold * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 1.5 : 1));")
content = content.replace("state.gold += quest.reward.gold;", "state.gold += Math.floor(quest.reward.gold * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 1.5 : 1));")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

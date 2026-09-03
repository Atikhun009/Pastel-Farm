import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_levelup = """                levelsGained.forEach(lvl => {
                    totalGoldReward += lvl * 500;
                    totalDiamondReward += Math.floor(lvl / 2) + 1; // 2+ diamonds
                    totalSeedReward += lvl;
                });
                
                state.gold += totalGoldReward;"""

new_levelup = """                levelsGained.forEach(lvl => {
                    totalGoldReward += lvl * 500;
                    totalDiamondReward += Math.floor(lvl / 2) + 1; // 2+ diamonds
                    totalSeedReward += lvl;
                });
                
                if (state.rebirths && state.rebirths > 0) totalGoldReward *= (1 + state.rebirths);
                state.gold += totalGoldReward;"""

content = content.replace(old_levelup, new_levelup)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

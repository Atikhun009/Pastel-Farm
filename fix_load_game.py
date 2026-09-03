import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_load = """                    if (!state.activeDynamicQuests) state.activeDynamicQuests = [];"""

new_load = """                    if (!state.activeDynamicQuests) state.activeDynamicQuests = [];
                    if (state.diamonds === undefined) state.diamonds = 0;
                    if (!state.claimedLevelRewards) state.claimedLevelRewards = 1;

                    // Retroactive rewards
                    if (state.level > state.claimedLevelRewards) {
                        let totalGoldReward = 0;
                        let totalDiamondReward = 0;
                        let totalSeedReward = 0;
                        for (let lvl = state.claimedLevelRewards + 1; lvl <= state.level; lvl++) {
                            totalGoldReward += lvl * 500;
                            totalDiamondReward += Math.floor(lvl / 2) + 1;
                            totalSeedReward += lvl;
                        }
                        state.gold += totalGoldReward;
                        state.diamonds += totalDiamondReward;
                        state.inventory.seeds['carrot'] = (state.inventory.seeds['carrot'] || 0) + totalSeedReward;
                        state.claimedLevelRewards = state.level;
                        setTimeout(() => {
                            showAlert('🎁 ของรางวัลย้อนหลัง!', `ยินดีด้วยที่เล่นมาไกล! ระบบได้เพิ่มของรางวัลย้อนหลังตามเลเวลให้แล้ว:\\n- เงิน: +${totalGoldReward} 🪙\\n- เพชร: +${totalDiamondReward} 💎\\n- เมล็ดแครอท: +${totalSeedReward} 🌱`, '💎');
                        }, 2000);
                    }
"""

content = content.replace(old_load, new_load)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_addxp = """        function addXP(amount) {
            if (state.upgrades && state.upgrades.golden_hoe) {
                amount = Math.floor(amount * (1 + (state.upgrades.golden_hoe * 0.005)));
            }
            state.xp += amount;
            let xpNeeded = state.level * 100;
            let leveledUp = false;
            
            while (state.xp >= xpNeeded) {
                state.xp -= xpNeeded;
                state.level++;
                xpNeeded = state.level * 100;
                leveledUp = true;
            }

            updateUI(); // Full update on XP change
            if (leveledUp) {
                showAlert('🎉 เลเวลอัพ!', `ยินดีด้วย! คุณอัพเป็นเลเวล ${state.level} แล้ว! เมนูและของใหม่ๆ ในตลาดถูกปลดล็อกแล้ว`, '🌟');
                if (typeof fireConfetti === 'function') fireConfetti();
            }
        }"""

new_addxp = """        function addXP(amount) {
            if (state.upgrades && state.upgrades.golden_hoe) {
                amount = Math.floor(amount * (1 + (state.upgrades.golden_hoe * 0.005)));
            }
            state.xp += amount;
            let xpNeeded = state.level * 100;
            let leveledUp = false;
            let levelsGained = [];
            
            while (state.xp >= xpNeeded) {
                state.xp -= xpNeeded;
                state.level++;
                xpNeeded = state.level * 100;
                levelsGained.push(state.level);
                leveledUp = true;
            }

            if (leveledUp) {
                let totalGoldReward = 0;
                let totalDiamondReward = 0;
                let totalSeedReward = 0;
                
                levelsGained.forEach(lvl => {
                    totalGoldReward += lvl * 500;
                    totalDiamondReward += Math.floor(lvl / 2) + 1; // 2+ diamonds
                    totalSeedReward += lvl;
                });
                
                state.gold += totalGoldReward;
                state.diamonds = (state.diamonds || 0) + totalDiamondReward;
                state.inventory.seeds['carrot'] = (state.inventory.seeds['carrot'] || 0) + totalSeedReward;
                
                // Track claim
                state.claimedLevelRewards = state.level;

                showAlert('🎉 เลเวลอัพ!', `ยินดีด้วย! คุณอัพเป็นเลเวล ${state.level} แล้ว!\n\n🎁 ของรางวัล:\n- เงิน: +${totalGoldReward} 🪙\n- เพชร: +${totalDiamondReward} 💎\n- เมล็ดแครอท: +${totalSeedReward} 🌱`, '🌟');
                if (typeof fireConfetti === 'function') fireConfetti();
            }
            updateUI();
        }"""

content = content.replace(old_addxp, new_addxp)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

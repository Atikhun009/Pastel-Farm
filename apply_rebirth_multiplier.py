import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update UI for Rebirths
old_ui = """            const uiDiamond = document.getElementById('ui-diamond');"""
new_ui = """            // Show rebirth tab if eligible
            const tabRebirth = document.getElementById('tab-rebirth');
            if (tabRebirth) {
                if (state.level >= 500 || (state.rebirths && state.rebirths > 0)) {
                    tabRebirth.classList.remove('hidden');
                } else {
                    tabRebirth.classList.add('hidden');
                }
            }
            
            const uiRebirthCount = document.getElementById('ui-rebirth-count');
            if (uiRebirthCount) uiRebirthCount.innerText = (state.rebirths || 0);
            
            const btnRebirth = document.getElementById('btn-perform-rebirth');
            const reqMsg = document.getElementById('rebirth-req-msg');
            if (btnRebirth && reqMsg) {
                if (state.level >= 500) {
                    btnRebirth.classList.remove('hidden', 'opacity-50', 'cursor-not-allowed');
                    reqMsg.classList.add('hidden');
                } else {
                    btnRebirth.classList.add('opacity-50', 'cursor-not-allowed');
                    reqMsg.classList.remove('hidden');
                }
            }

            const uiDiamond = document.getElementById('ui-diamond');"""
content = content.replace(old_ui, new_ui)

# 2. AddXP multiplier
old_addxp = """            if (state.upgrades && state.upgrades.golden_hoe) {
                amount = Math.floor(amount * (1 + (state.upgrades.golden_hoe * 0.005)));
            }
            state.xp += amount;"""
new_addxp = """            if (state.upgrades && state.upgrades.golden_hoe) {
                amount = Math.floor(amount * (1 + (state.upgrades.golden_hoe * 0.005)));
            }
            // Rebirth Multiplier
            if (state.rebirths && state.rebirths > 0) {
                amount *= (1 + state.rebirths); // +100% per rebirth
            }
            state.xp += amount;"""
content = content.replace(old_addxp, new_addxp)

# 3. Sell Gold multiplier
old_sell = """                let totalValue = Math.floor(p.basePrice * qty * multiplier);
                
                // Achievement buff
                if (state.achievements && state.achievements.claimed) {
                    if (state.achievements.claimed.includes('a1')) totalValue = Math.floor(totalValue * 1.05);
                    if (state.achievements.claimed.includes('a2')) totalValue = Math.floor(totalValue * 1.10);
                }"""
new_sell = """                let totalValue = Math.floor(p.basePrice * qty * multiplier);
                
                // Achievement buff
                if (state.achievements && state.achievements.claimed) {
                    if (state.achievements.claimed.includes('a1')) totalValue = Math.floor(totalValue * 1.05);
                    if (state.achievements.claimed.includes('a2')) totalValue = Math.floor(totalValue * 1.10);
                }
                // Rebirth Multiplier
                if (state.rebirths && state.rebirths > 0) {
                    totalValue *= (1 + state.rebirths);
                }"""
content = content.replace(old_sell, new_sell)

# 4. Orders multiplier
old_order_gold = "state.gold += Math.floor(order.reward.gold * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 2 : 1));"
new_order_gold = """            let finalGold = order.reward.gold;
            if (state.rebirths && state.rebirths > 0) finalGold *= (1 + state.rebirths);
            state.gold += Math.floor(finalGold * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 2 : 1));"""
content = content.replace(old_order_gold, new_order_gold)

old_order_alert = "showAlert('ส่งของสำเร็จ!', `คุณได้รับ ${order.reward.gold} 🪙, ${order.reward.xp} XP${diamondStr}`, '✅');"
new_order_alert = "showAlert('ส่งของสำเร็จ!', `คุณได้รับ ${finalGold} 🪙, ${order.reward.xp * (state.rebirths ? 1 + state.rebirths : 1)} XP${diamondStr}`, '✅');"
content = content.replace(old_order_alert, new_order_alert)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

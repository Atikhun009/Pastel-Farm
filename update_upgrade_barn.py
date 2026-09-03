import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_func = """        function upgradeBarn() {
            const lvl = state.inventory.barnLevel || 1;
            if (lvl >= 10) return;
            
            const nextUpg = BARN_UPGRADES.find(u => u.level === lvl + 1);
            if (!state.inventory.barnSubmissions) state.inventory.barnSubmissions = {};
            
            // Check again
            if (state.gold < nextUpg.reqGold) return;
            let canUpgrade = true;
            Object.entries(nextUpg.reqItems).forEach(([reqId, reqQty]) => {
                if ((state.inventory.barnSubmissions[reqId] || 0) < reqQty) canUpgrade = false;
            });
            
            if (!canUpgrade) return;
            
            // Deduct Gold
            state.gold -= nextUpg.reqGold;
            
            // Upgrade
            state.inventory.barnLevel = lvl + 1;
            
            // Clear submissions for next level
            state.inventory.barnSubmissions = {};
            
            closeBarnUpgradeModal();
            updateUI();
            
            showAlert('อัปเกรดโรงนาสำเร็จ!', `ยินดีด้วย! พื้นที่เก็บของเพิ่มเป็น ${nextUpg.capacity >= 999999 ? 'MAX' : nextUpg.capacity} ชิ้นแล้ว`, '🎉');
            if (typeof fireConfetti === 'function') fireConfetti();
        }"""

new_func = """        function upgradeBarn() {
            const lvl = state.inventory.barnLevel || 1;
            if (lvl >= 10) return;
            
            const nextUpg = BARN_UPGRADES.find(u => u.level === lvl + 1);
            
            // Check again
            if (state.gold < nextUpg.reqGold) return;
            let canUpgrade = true;
            Object.entries(nextUpg.reqItems).forEach(([reqId, reqQty]) => {
                if ((state.inventory.products[reqId] || 0) < reqQty) canUpgrade = false;
            });
            
            if (!canUpgrade) return;
            
            // Deduct Gold
            state.gold -= nextUpg.reqGold;
            
            // Deduct Items
            Object.entries(nextUpg.reqItems).forEach(([reqId, reqQty]) => {
                state.inventory.products[reqId] -= reqQty;
            });
            
            // Upgrade
            state.inventory.barnLevel = lvl + 1;
            
            closeBarnUpgradeModal();
            updateUI();
            
            showAlert('อัปเกรดโรงนาสำเร็จ!', `ยินดีด้วย! พื้นที่เก็บของเพิ่มเป็น ${nextUpg.capacity >= 999999 ? 'MAX' : nextUpg.capacity} ชิ้นแล้ว`, '🎉');
            if (typeof fireConfetti === 'function') fireConfetti();
        }"""

if old_func in content:
    content = content.replace(old_func, new_func)
    print("upgradeBarn updated successfully.")
else:
    print("upgradeBarn pattern not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

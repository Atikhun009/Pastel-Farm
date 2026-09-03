import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update openBarnUpgradeModal HTML
old_modal_html = """                        <div class="space-y-2 mb-4">
                            <div class="flex items-center justify-between bg-white/60 p-2 rounded-xl text-sm">
                                <span class="flex items-center gap-2">🪙 ทองคำ</span>
                                <span class="${state.gold >= nextUpg.reqGold ? 'text-green-600' : 'text-red-500'} font-bold">${state.gold}/${nextUpg.reqGold}</span>
                            </div>
                            ${reqHtml}
                        </div>
                        
                        <button onclick="upgradeBarn()" class="w-full glass-btn ${canUpgrade ? 'bg-blue-500 hover:bg-blue-600 text-white border-blue-400' : 'bg-gray-200 text-gray-500'} py-3 rounded-xl font-bold shadow-sm" ${!canUpgrade ? 'disabled' : ''}>
                            อัปเกรดเลย!
                        </button>
                    </div>"""

new_modal_html = """                        <div class="space-y-2 mb-4">
                            <div class="flex items-center justify-between bg-white/60 p-2 rounded-xl text-sm">
                                <span class="flex items-center gap-2">🪙 ทองคำ</span>
                                <span class="${state.gold >= nextUpg.reqGold ? 'text-green-600' : 'text-red-500'} font-bold">${state.gold}/${nextUpg.reqGold}</span>
                            </div>
                            ${reqHtml}
                        </div>
                        
                        <div class="flex flex-col gap-2">
                            ${(state.inventory.barnFreeUpgradeCoupons && state.inventory.barnFreeUpgradeCoupons > 0) ? `
                            <button onclick="upgradeBarn(true)" class="w-full glass-btn bg-purple-500 hover:bg-purple-600 text-white py-3 rounded-xl font-bold shadow-sm border-purple-400">
                                🎫 ใช้คูปองอัปฟรี (${state.inventory.barnFreeUpgradeCoupons} ใบ)
                            </button>
                            ` : ''}
                            <button onclick="upgradeBarn(false)" class="w-full glass-btn ${canUpgrade ? 'bg-blue-500 hover:bg-blue-600 text-white border-blue-400' : 'bg-gray-200 text-gray-500'} py-3 rounded-xl font-bold shadow-sm" ${!canUpgrade ? 'disabled' : ''}>
                                อัปเกรดเลย!
                            </button>
                        </div>
                    </div>"""

if old_modal_html in content:
    content = content.replace(old_modal_html, new_modal_html)
    print("openBarnUpgradeModal updated")

# 2. Update upgradeBarn function
old_upgrade_barn = """        function upgradeBarn() {
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

new_upgrade_barn = """        function upgradeBarn(useCoupon = false) {
            const lvl = state.inventory.barnLevel || 1;
            if (lvl >= 10) return;
            
            const nextUpg = BARN_UPGRADES.find(u => u.level === lvl + 1);
            
            if (useCoupon) {
                if ((state.inventory.barnFreeUpgradeCoupons || 0) < 1) return;
                state.inventory.barnFreeUpgradeCoupons--;
            } else {
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
            }
            
            // Upgrade
            state.inventory.barnLevel = lvl + 1;
            
            closeBarnUpgradeModal();
            updateUI();
            
            showAlert('อัปเกรดโรงนาสำเร็จ!', `ยินดีด้วย! พื้นที่เก็บของเพิ่มเป็น ${nextUpg.capacity >= 999999 ? 'MAX' : nextUpg.capacity} ชิ้นแล้ว`, '🎉');
            if (typeof fireConfetti === 'function') fireConfetti();
        }"""

if old_upgrade_barn in content:
    content = content.replace(old_upgrade_barn, new_upgrade_barn)
    print("upgradeBarn updated")

# 3. Add new redeem code
old_redeem = """            if (code === 'PASTELFARM2025') {"""

new_redeem = """            if (code === 'SUPERGIFT2026') {
                state.inventory.barnFreeUpgradeCoupons = (state.inventory.barnFreeUpgradeCoupons || 0) + 1;
                
                const twoHours = 2 * 60 * 60 * 1000;
                const now = Date.now();
                state.activeBuffs.cropSpeedEnd = Math.max(state.activeBuffs.cropSpeedEnd || 0, now) + twoHours;
                state.activeBuffs.goldMultEnd = Math.max(state.activeBuffs.goldMultEnd || 0, now) + twoHours;
                state.activeBuffs.animalSpeedEnd = Math.max(state.activeBuffs.animalSpeedEnd || 0, now) + twoHours;
                state.activeBuffs.doubleDropEnd = Math.max(state.activeBuffs.doubleDropEnd || 0, now) + twoHours;
                
                state.redeemedCodes.push(code);
                
                updateUI();
                inputEl.value = '';
                showAlert('รับรางวัลสำเร็จ!', 'ได้รับคูปองอัปเกรดโรงนาฟรี 1 ระดับ x1\\nและบัฟทุกชนิด 2 ชั่วโมงเต็ม!', '🎉');
                if (typeof fireConfetti === 'function') fireConfetti();
                return;
            }
            
            if (code === 'PASTELFARM2025') {"""

if old_redeem in content:
    content = content.replace(old_redeem, new_redeem)
    print("SUPERGIFT2026 code added")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


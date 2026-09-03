import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_redeem = """            if (code === 'PASTELFARM2025') {
                state.gold += 2000000;
                state.inventory.barnResetCoupons = (state.inventory.barnResetCoupons || 0) + 2;
                
                state.activeBuffs.cropSpeedEnd = Math.max(state.activeBuffs.cropSpeedEnd || 0, Date.now()) + 60000; // 1 min
                state.activeBuffs.goldMultEnd = Math.max(state.activeBuffs.goldMultEnd || 0, Date.now()) + 120000; // 2 mins
                
                state.redeemedCodes.push(code);
                
                updateUI();
                inputEl.value = '';
                showAlert('รับรางวัลสำเร็จ!', 'ได้รับเงิน 2,000,000 🪙\\nคูปองล้างโรงนา x2\\nพืชโตไว 2x (1 นาที)\\nเงินขาย 1.5x (2 นาที)', '🎉');
                if (typeof fireConfetti === 'function') fireConfetti();
                return;
            }"""

new_redeem = """            if (code === 'PASTELFARM2025') {
                state.gold += 2000000;
                state.inventory.barnResetCoupons = (state.inventory.barnResetCoupons || 0) + 2;
                
                state.activeBuffs.cropSpeedEnd = Math.max(state.activeBuffs.cropSpeedEnd || 0, Date.now()) + 60000; // 1 min
                state.activeBuffs.goldMultEnd = Math.max(state.activeBuffs.goldMultEnd || 0, Date.now()) + 120000; // 2 mins
                
                state.redeemedCodes.push(code);
                
                updateUI();
                inputEl.value = '';
                showAlert('รับรางวัลสำเร็จ!', 'ได้รับเงิน 2,000,000 🪙\\nคูปองล้างโรงนา x2\\nพืชโตไว 2x (1 นาที)\\nเงินขาย 1.5x (2 นาที)', '🎉');
                if (typeof fireConfetti === 'function') fireConfetti();
                return;
            }
            
            if (code === 'WELCOMEBUFF') {
                state.gold += 20000;
                state.diamonds = (state.diamonds || 0) + 100;
                
                const fourMins = 4 * 60 * 1000;
                const now = Date.now();
                state.activeBuffs.cropSpeedEnd = Math.max(state.activeBuffs.cropSpeedEnd || 0, now) + fourMins;
                state.activeBuffs.goldMultEnd = Math.max(state.activeBuffs.goldMultEnd || 0, now) + fourMins;
                state.activeBuffs.animalSpeedEnd = Math.max(state.activeBuffs.animalSpeedEnd || 0, now) + fourMins;
                state.activeBuffs.doubleDropEnd = Math.max(state.activeBuffs.doubleDropEnd || 0, now) + fourMins;
                
                state.redeemedCodes.push(code);
                
                updateUI();
                inputEl.value = '';
                showAlert('รับรางวัลสำเร็จ!', 'ได้รับเงิน 20,000 🪙\\nเพชร 100 💎\\nบัฟทุกชนิด 4 นาที!', '🎁');
                if (typeof fireConfetti === 'function') fireConfetti();
                return;
            }"""

content = content.replace(old_redeem, new_redeem)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

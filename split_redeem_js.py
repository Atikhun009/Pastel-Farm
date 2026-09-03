import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_js = """        function redeemCode() {
            const inputEl = document.getElementById('redeem-code-input');
            if (!inputEl) return;
            const code = inputEl.value.trim().toUpperCase();
            
            if (!code) return;
            
            if (!state.redeemedCodes) state.redeemedCodes = [];
            if (!state.activeBuffs) state.activeBuffs = { cropSpeedEnd: 0, goldMultEnd: 0 };
            
            
            // Parse Gift Code
            if (code.startsWith('GIFT-')) {
                const b64 = code.replace('GIFT-', '');
                try {
                    const jsonStr = decodeURIComponent(atob(b64));
                    const payload = JSON.parse(jsonStr);
                    
                    // Check expiry
                    if (Date.now() > payload.x) {
                        showAlert('โค้ดหมดอายุ!', 'โค้ดของขวัญนี้หมดอายุไปแล้ว (เกิน 2 นาที)', '⌛');
                        return;
                    }
                    
                    // Check if used
                    if (state.redeemedCodes.includes(payload.r)) {
                        showAlert('โค้ดถูกใช้ไปแล้ว!', 'มีคนใช้โค้ดของขวัญนี้ไปแล้ว', '🚫');
                        return;
                    }
                    
                    // Add items
                    let itemName = '';
                    let emoji = '🎁';
                    const val = payload.t;
                    const qty = payload.q;
                    
                    if (val === 'gold') {
                        state.gold += qty;
                        itemName = 'เงินทอง';
                        emoji = '🪙';
                    } else if (val === 'diamonds') {
                        state.diamonds = (state.diamonds || 0) + qty;
                        itemName = 'เพชร';
                        emoji = '💎';
                    } else if (val.startsWith('p_')) {
                        const id = val.replace('p_', '');
                        state.inventory.products[id] = (state.inventory.products[id] || 0) + qty;
                        const ref = PRODUCTS[id] || ANIMALS[id] || RECIPES[id];
                        if (ref) { itemName = ref.name; emoji = ref.emoji; }
                    } else if (val.startsWith('s_')) {
                        const id = val.replace('s_', '');
                        state.inventory.seeds[id] = (state.inventory.seeds[id] || 0) + qty;
                        const ref = SEEDS[id];
                        if (ref) { itemName = `เมล็ด${ref.name}`; emoji = ref.emoji; }
                    }
                    
                    state.redeemedCodes.push(payload.r);
                    updateUI();
                    
                    inputEl.value = '';
                    showAlert('รับของขวัญสำเร็จ!', `คุณได้รับ ${itemName} จำนวน ${qty} ชิ้น`, emoji);
                    if (typeof fireConfetti === 'function') fireConfetti();
                    return;
                } catch(e) {
                    showAlert('โค้ดไม่ถูกต้อง', 'โค้ดของขวัญนี้พังหรือไม่สมบูรณ์', '❌');
                    return;
                }
            }

            // Normal codes
            if (state.redeemedCodes.includes(code)) {
                showAlert('ใช้โค้ดไปแล้ว', 'คุณได้ใช้งานโค้ดนี้ไปแล้วนะ!', '🚫');
                return;
            }
            
            if (code === 'PASTELFARM2025') {
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
            }
            
            showAlert('โค้ดไม่ถูกต้อง', 'โค้ดนี้ไม่มีอยู่จริง หรือหมดอายุไปแล้ว', '❌');
        }"""

new_js = """        function redeemDevCode() {
            const inputEl = document.getElementById('redeem-dev-code-input');
            if (!inputEl) return;
            const code = inputEl.value.trim().toUpperCase();
            
            if (!code) return;
            
            if (!state.redeemedCodes) state.redeemedCodes = [];
            if (!state.activeBuffs) state.activeBuffs = { cropSpeedEnd: 0, goldMultEnd: 0 };
            
            // Normal codes
            if (state.redeemedCodes.includes(code)) {
                showAlert('ใช้โค้ดไปแล้ว', 'คุณได้ใช้งานโค้ดนี้ไปแล้วนะ!', '🚫');
                return;
            }
            
            if (code === 'PASTELFARM2025') {
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
            }
            
            showAlert('โค้ดไม่ถูกต้อง', 'โค้ดนี้ไม่มีอยู่จริง หรือหมดอายุไปแล้ว', '❌');
        }

        function redeemFriendGift() {
            const inputEl = document.getElementById('redeem-gift-code-input');
            if (!inputEl) return;
            const code = inputEl.value.trim();
            
            if (!code) return;
            
            if (!state.redeemedCodes) state.redeemedCodes = [];
            
            if (code.startsWith('GIFT-')) {
                const b64 = code.replace('GIFT-', '');
                try {
                    const jsonStr = decodeURIComponent(atob(b64));
                    const payload = JSON.parse(jsonStr);
                    
                    // Check expiry
                    if (Date.now() > payload.x) {
                        showAlert('โค้ดหมดอายุ!', 'โค้ดของขวัญนี้หมดอายุไปแล้ว (เกิน 2 นาที)', '⌛');
                        return;
                    }
                    
                    // Check if used
                    if (state.redeemedCodes.includes(payload.r)) {
                        showAlert('โค้ดถูกใช้ไปแล้ว!', 'มีคนใช้โค้ดของขวัญนี้ไปแล้ว', '🚫');
                        return;
                    }
                    
                    // Add items
                    let itemName = '';
                    let emoji = '🎁';
                    const val = payload.t;
                    const qty = payload.q;
                    
                    if (val === 'gold') {
                        state.gold += qty;
                        itemName = 'เงินทอง';
                        emoji = '🪙';
                    } else if (val === 'diamonds') {
                        state.diamonds = (state.diamonds || 0) + qty;
                        itemName = 'เพชร';
                        emoji = '💎';
                    } else if (val.startsWith('p_')) {
                        const id = val.replace('p_', '');
                        state.inventory.products[id] = (state.inventory.products[id] || 0) + qty;
                        const ref = PRODUCTS[id] || ANIMALS[id] || RECIPES[id];
                        if (ref) { itemName = ref.name; emoji = ref.emoji; }
                    } else if (val.startsWith('s_')) {
                        const id = val.replace('s_', '');
                        state.inventory.seeds[id] = (state.inventory.seeds[id] || 0) + qty;
                        const ref = SEEDS[id];
                        if (ref) { itemName = `เมล็ด${ref.name}`; emoji = ref.emoji; }
                    }
                    
                    state.redeemedCodes.push(payload.r);
                    updateUI();
                    
                    inputEl.value = '';
                    showAlert('รับของขวัญสำเร็จ!', `คุณได้รับ ${itemName} จำนวน ${qty} ชิ้น`, emoji);
                    if (typeof fireConfetti === 'function') fireConfetti();
                    return;
                } catch(e) {
                    showAlert('โค้ดไม่ถูกต้อง', 'โค้ดของขวัญนี้พังหรือไม่สมบูรณ์', '❌');
                    return;
                }
            } else {
                showAlert('รูปแบบผิดพลาด', 'โค้ดเพื่อนต้องขึ้นต้นด้วย GIFT- เท่านั้น', '❌');
            }
        }"""

if old_js in content:
    content = content.replace(old_js, new_js)
    print("JS updated")
else:
    print("JS NOT FOUND")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

gift_logic = """
        function populateGiftDropdown() {
            const select = document.getElementById('gift-item-select');
            if (!select) return;
            
            let html = '';
            // Add Gold
            if (state.gold > 0) {
                html += `<option value="gold">🪙 เงินทอง (มี: ${state.gold})</option>`;
            }
            // Add Diamonds
            if (state.diamonds > 0) {
                html += `<option value="diamonds">💎 เพชร (มี: ${state.diamonds})</option>`;
            }
            
            // Add Products
            if (state.inventory && state.inventory.products) {
                Object.entries(state.inventory.products).forEach(([id, qty]) => {
                    if (qty > 0) {
                        const item = PRODUCTS[id] || ANIMALS[id] || RECIPES[id];
                        if (item) {
                            html += `<option value="p_${id}">${item.emoji} ${item.name} (มี: ${qty})</option>`;
                        }
                    }
                });
            }
            
            // Add Seeds
            if (state.inventory && state.inventory.seeds) {
                Object.entries(state.inventory.seeds).forEach(([id, qty]) => {
                    if (qty > 0) {
                        const item = SEEDS[id];
                        if (item) {
                            html += `<option value="s_${id}">${item.emoji} เมล็ด${item.name} (มี: ${qty})</option>`;
                        }
                    }
                });
            }
            
            if (html === '') {
                html = '<option value="">(ไม่มีของในกระเป๋าเลย)</option>';
            }
            select.innerHTML = html;
            
            // Update max qty dynamically when changed
            select.onchange = function() {
                const val = this.value;
                const qtyInput = document.getElementById('gift-qty-input');
                let max = 0;
                if (val === 'gold') max = state.gold;
                else if (val === 'diamonds') max = state.diamonds || 0;
                else if (val.startsWith('p_')) max = state.inventory.products[val.replace('p_', '')] || 0;
                else if (val.startsWith('s_')) max = state.inventory.seeds[val.replace('s_', '')] || 0;
                
                qtyInput.max = max;
                if (parseInt(qtyInput.value) > max) qtyInput.value = max;
            };
            // trigger once
            if (select.onchange) select.onchange();
        }

        function generateGiftCode() {
            const select = document.getElementById('gift-item-select');
            const qtyInput = document.getElementById('gift-qty-input');
            const resultBox = document.getElementById('gift-result-box');
            const output = document.getElementById('gift-code-output');
            
            const val = select.value;
            let qty = parseInt(qtyInput.value) || 0;
            
            if (!val || qty <= 0) {
                showAlert('ข้อมูลไม่ถูกต้อง', 'กรุณาเลือกไอเทมและระบุจำนวนที่มากกว่า 0', '❌');
                return;
            }
            
            // Verify quantity
            let max = 0;
            if (val === 'gold') max = state.gold;
            else if (val === 'diamonds') max = state.diamonds || 0;
            else if (val.startsWith('p_')) max = state.inventory.products[val.replace('p_', '')] || 0;
            else if (val.startsWith('s_')) max = state.inventory.seeds[val.replace('s_', '')] || 0;
            
            if (qty > max) {
                showAlert('ของไม่พอ!', 'คุณมีของไม่พอที่จะส่ง', '❌');
                return;
            }
            
            // Deduct from sender
            if (val === 'gold') state.gold -= qty;
            else if (val === 'diamonds') state.diamonds -= qty;
            else if (val.startsWith('p_')) state.inventory.products[val.replace('p_', '')] -= qty;
            else if (val.startsWith('s_')) state.inventory.seeds[val.replace('s_', '')] -= qty;
            
            // Payload
            const payload = {
                t: val, // type/id
                q: qty, // quantity
                x: Date.now() + (2 * 60 * 1000), // Expiry 2 mins
                r: Math.random().toString(36).substring(2,10) // random nonce to prevent reuse
            };
            
            const jsonStr = JSON.stringify(payload);
            const b64 = btoa(encodeURIComponent(jsonStr));
            const code = 'GIFT-' + b64;
            
            output.value = code;
            resultBox.classList.remove('hidden');
            
            updateUI();
            populateGiftDropdown(); // refresh dropdown
            
            showAlert('สร้างโค้ดสำเร็จ!', 'คัดลอกโค้ดไปให้เพื่อนได้เลย (มีเวลา 2 นาทีเท่านั้น)', '🎁');
        }

        function copyGiftCode() {
            const output = document.getElementById('gift-code-output');
            output.select();
            document.execCommand('copy');
            showAlert('ก๊อปปี้สำเร็จ!', 'นำโค้ดไปส่งให้เพื่อนได้เลย', '📋');
        }
"""

content = content.replace("function redeemCode() {", gift_logic + "\n        function redeemCode() {")

# Call populateGiftDropdown in updateUI or switchTab.
old_switch = """        function switchTab(tabId) {"""
new_switch = """        function switchTab(tabId) {
            if (tabId === 'redeem') {
                populateGiftDropdown();
            }"""
content = content.replace(old_switch, new_switch)

# Add Gift code parsing to redeemCode
old_redeem = """            if (state.redeemedCodes.includes(code)) {
                showAlert('ใช้โค้ดไปแล้ว', 'คุณได้ใช้งานโค้ดนี้ไปแล้วนะ!', '🚫');
                return;
            }"""
new_redeem = """            
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
            }"""

content = content.replace(old_redeem, new_redeem)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


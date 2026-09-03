with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

funcs = """
        function redeemCode() {
            const inputEl = document.getElementById('redeem-code-input');
            if (!inputEl) return;
            const code = inputEl.value.trim().toUpperCase();
            
            if (!code) return;
            
            if (!state.redeemedCodes) state.redeemedCodes = [];
            if (!state.activeBuffs) state.activeBuffs = { cropSpeedEnd: 0, goldMultEnd: 0 };
            
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
            
            showAlert('โค้ดไม่ถูกต้อง', 'โค้ดนี้ไม่มีอยู่จริง หรือหมดอายุไปแล้ว', '❌');
        }
        
        function useBarnResetCoupon() {
            if (state.inventory.barnResetCoupons > 0) {
                state.inventory.products = {};
                state.inventory.seeds = {};
                state.inventory.fertilizer = 0;
                state.inventory.barnResetCoupons -= 1;
                updateUI();
                showAlert('ล้างโรงนาสำเร็จ!', 'โรงนาของคุณถูกลบของทั้งหมดกลายเป็น 0 แล้ว มีพื้นที่ว่างเหลือเฟือ!', '🎫');
            } else {
                showAlert('ไม่มีคูปอง', 'คุณไม่มีคูปองล้างโรงนา', '🚫');
            }
        }
"""

content = content.replace('</script>', funcs + '\n    </script>')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

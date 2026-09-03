import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_func = """
        function buyDiamondBuff(type, cost) {
            if ((state.diamonds || 0) < cost) {
                showAlert('เพชรไม่พอ!', 'คุณมีเพชรไม่เพียงพอสำหรับซื้อไอเทมนี้', '💎');
                return;
            }
            
            state.diamonds -= cost;
            const now = Date.now();
            const duration = 2 * 60 * 1000; // 2 mins
            
            if (type === 'gold_x2') {
                state.activeBuffs.goldMultEnd = Math.max(now, state.activeBuffs.goldMultEnd || 0) + duration;
                showAlert('ซื้อสำเร็จ!', 'คุณได้รับบัฟเงินคูณสอง 2 นาที', '🪙');
            } else if (type === 'crop_speed_x2') {
                state.activeBuffs.cropSpeedEnd = Math.max(now, state.activeBuffs.cropSpeedEnd || 0) + duration;
                showAlert('ซื้อสำเร็จ!', 'คุณได้รับบัฟพืชโตไวสองเท่า 2 นาที', '🌱');
            } else if (type === 'animal_speed_x2') {
                state.activeBuffs.animalSpeedEnd = Math.max(now, state.activeBuffs.animalSpeedEnd || 0) + duration;
                showAlert('ซื้อสำเร็จ!', 'คุณได้รับบัฟสัตว์ผลิตไวสองเท่า 2 นาที', '🐾');
            } else if (type === 'double_drop') {
                state.activeBuffs.doubleDropEnd = Math.max(now, state.activeBuffs.doubleDropEnd || 0) + duration;
                showAlert('ซื้อสำเร็จ!', 'คุณได้รับโอกาสสุ่มได้ผลผลิต x2 แบบ 100% เป็นเวลา 2 นาที', '🍀');
            } else if (type === 'gold_instant') {
                const goldGained = state.level * 1000;
                state.gold += goldGained;
                showAlert('ซื้อสำเร็จ!', `แลกเพชรเป็นเงินสำเร็จ ได้รับ ${goldGained} 🪙`, '💰');
            }
            
            updateUI();
        }
"""

content = content.replace("function useBarnResetCoupon()", new_func + "\n        function useBarnResetCoupon()")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update getCurrentItemsCount
old_count = """        function getCurrentItemsCount() {
            return Object.values(state.inventory.products).reduce((sum, val) => sum + val, 0);
        }"""

new_count = """        function getCurrentItemsCount() {
            let count = Object.values(state.inventory.products).reduce((sum, val) => sum + val, 0);
            count += Object.values(state.inventory.seeds).reduce((sum, val) => sum + val, 0);
            count += (state.inventory.fertilizer || 0);
            return count;
        }"""

content = content.replace(old_count, new_count)

# 2. Update buyItem
old_buy = """            if (state.gold < totalPrice) {
                showAlert('เงินไม่พอ!', `เหรียญทองไม่พอสำหรับซื้อ ${qty} ชิ้น`, '💸');
                return;
            }

            if (type === 'seed') {"""

new_buy = """            if (state.gold < totalPrice) {
                showAlert('เงินไม่พอ!', `เหรียญทองไม่พอสำหรับซื้อ ${qty} ชิ้น`, '💸');
                return;
            }
            
            if (type === 'seed' || type === 'fertilizer') {
                if (!checkBarnCapacity(qty)) {
                    showAlert('พื้นที่กระเป๋าเต็ม!', 'ไม่สามารถซื้อของเพิ่มได้ โปรดอัปเกรดโรงนาหรือขายของก่อน', '📦');
                    return;
                }
            }

            if (type === 'seed') {"""

content = content.replace(old_buy, new_buy)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

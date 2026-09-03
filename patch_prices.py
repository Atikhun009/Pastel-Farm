import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Modify decor_discount to upgrade_discount in UPGRADES
content = content.replace("decor_discount: { id: 'decor_discount', name: 'บัตรส่วนลดร้านค้า', emoji: '🏷️', desc: 'ซื้อของตกแต่งถูกลง 5% ต่อเลเวล', buyPrice: 1000, maxLevel: 5, priceMult: 1.5, type: 'passive' }",
"upgrade_discount: { id: 'upgrade_discount', name: 'บัตรส่วนลดอัปเกรด', emoji: '🏷️', desc: 'ซื้ออัปเกรดถูกลง 5% ต่อเลเวล', buyPrice: 1000, maxLevel: 5, priceMult: 1.5, type: 'passive' }")

# 2. Modify sellAllInventory for sales_license
old_sell = """            const finalValue = Math.floor(totalValue * 0.95);
            state.gold += finalValue;
            
            updateUI();
            showAlert('ขายทั้งหมดสำเร็จ!', `ขายผลผลิต ${totalItems} ชิ้น ได้รับเงิน ${finalValue} 🪙\\n(มูลค่าเดิม ${totalValue} หักค่าธรรมเนียม 5%)`, '💰');"""
new_sell = """            let feePercent = 5;
            if (state.upgrades && state.upgrades.sales_license) {
                feePercent -= state.upgrades.sales_license * 1;
            }
            if (feePercent < 0) feePercent = 0;
            const finalValue = Math.floor(totalValue * ((100 - feePercent) / 100));
            state.gold += finalValue;
            
            updateUI();
            showAlert('ขายทั้งหมดสำเร็จ!', `ขายผลผลิต ${totalItems} ชิ้น ได้รับเงิน ${finalValue} 🪙\\n(มูลค่าเดิม ${totalValue} หักค่าธรรมเนียม ${feePercent}%)`, '💰');"""
content = content.replace(old_sell, new_sell)

# 3. Modify bulk_buyer in animal pricing inside renderShopDOM
old_animal_price = """const dynamicPrice = Math.floor(animal.buyPrice * mult);"""
new_animal_price = """let dynamicPrice = Math.floor(animal.buyPrice * mult);
                if (state.upgrades && state.upgrades.bulk_buyer) {
                    dynamicPrice = Math.floor(dynamicPrice * (1 - (state.upgrades.bulk_buyer * 0.05)));
                }"""
# Note: we need to replace only the animal dynamicPrice, not the seed one.
# So we can use a more specific replace. Let's find the exact block.
content = re.sub(r"const dynamicPrice = Math.floor\(animal.buyPrice \* mult\);", new_animal_price, content)

# 4. Modify upgrade pricing inside renderUpgradesDOM
old_upgrade_price = """const nextPrice = Math.floor(u.buyPrice * Math.pow(u.priceMult, curLevel));"""
new_upgrade_price = """let nextPrice = Math.floor(u.buyPrice * Math.pow(u.priceMult, curLevel));
                if (state.upgrades && state.upgrades.upgrade_discount) {
                    nextPrice = Math.floor(nextPrice * (1 - (state.upgrades.upgrade_discount * 0.05)));
                }"""
content = re.sub(r"const nextPrice = Math.floor\(u\.buyPrice \* Math\.pow\(u\.priceMult, curLevel\)\);", new_upgrade_price, content)

# 5. Modify buyDynamicUpgrade to use the discount
old_buy_upgrade = """const nextPrice = Math.floor(u.buyPrice * Math.pow(u.priceMult, curLevel));"""
new_buy_upgrade = """let nextPrice = Math.floor(u.buyPrice * Math.pow(u.priceMult, curLevel));
            if (state.upgrades && state.upgrades.upgrade_discount) {
                nextPrice = Math.floor(nextPrice * (1 - (state.upgrades.upgrade_discount * 0.05)));
            }"""
# Wait, this matches the exact same string, let's just use re.sub again, but since it's global, both will be replaced! Perfect.
content = re.sub(r"const nextPrice = Math.floor\(u\.buyPrice \* Math\.pow\(u\.priceMult, curLevel\)\);", new_buy_upgrade, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


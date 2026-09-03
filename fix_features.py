import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Market Interval to 5 minutes
content = content.replace("now - state.lastMarketUpdate > 60000", "now - state.lastMarketUpdate > 300000")

# 2. Add Upgrades
new_upgrades = """
            greenhouse: { id: 'greenhouse', name: 'เรือนกระจก', emoji: '🏡', desc: 'พืชโตไว 50% ตลอดกาล', buyPrice: 2500, maxLevel: 1, priceMult: 1, type: 'passive' },
            master_chef: { id: 'master_chef', name: 'มาสเตอร์เชฟ', emoji: '👨‍🍳', desc: 'ทำอาหารได้ XP เพิ่ม 10% ต่อเลเวล', buyPrice: 1500, maxLevel: 5, priceMult: 2, type: 'passive' },
            sales_license: { id: 'sales_license', name: 'ใบอนุญาตการค้า', emoji: '🎫', desc: 'ค่าธรรมเนียมขายทั้งหมดลดลง 1% ต่อเลเวล', buyPrice: 2000, maxLevel: 5, priceMult: 1.8, type: 'passive' },
            bulk_buyer: { id: 'bulk_buyer', name: 'เหมาจ่าย', emoji: '🤝', desc: 'ซื้อสัตว์เลี้ยงถูกลง 5% ต่อเลเวล', buyPrice: 1800, maxLevel: 5, priceMult: 2, type: 'passive' },
            lucky_hand: { id: 'lucky_hand', name: 'มือทองคำ', emoji: '🧤', desc: 'โอกาส 2% ต่อเลเวล ที่สัตว์จะให้ผลผลิต x2', buyPrice: 3000, maxLevel: 5, priceMult: 2.2, type: 'passive' },
            decor_discount: { id: 'decor_discount', name: 'บัตรส่วนลดร้านค้า', emoji: '🏷️', desc: 'ซื้อของตกแต่งถูกลง 5% ต่อเลเวล', buyPrice: 1000, maxLevel: 5, priceMult: 1.5, type: 'passive' },
"""
content = re.sub(r"greenhouse: { id: 'greenhouse', name: 'เรือนกระจก', emoji: '🏡', desc: 'พืชโตไว 50% ตลอดกาล', buyPrice: 2500, maxLevel: 1, priceMult: 1, type: 'passive' },", new_upgrades, content)

# 3. Modify Kitchen UI
old_cook_ui = """<button onclick="cookRecipe('${recipe.id}')" class="glass-btn px-5 py-2.5 rounded-xl text-sm font-bold text-blue-700 shadow-sm whitespace-nowrap bg-blue-50/50" ${isLocked || !canCook ? 'disabled' : ''}>
                            ทำอาหาร
                        </button>"""
new_cook_ui = """<div class="flex items-center gap-2">
                            <input type="number" id="qty-${recipe.id}" value="1" min="1" class="w-16 rounded-xl border-gray-300 shadow-sm px-2 py-2 text-sm text-center" ${isLocked || !canCook ? 'disabled' : ''}>
                            <button onclick="cookRecipe('${recipe.id}')" class="glass-btn px-4 py-2.5 rounded-xl text-sm font-bold text-blue-700 shadow-sm whitespace-nowrap bg-blue-50/50" ${isLocked || !canCook ? 'disabled' : ''}>
                                ทำอาหาร
                            </button>
                        </div>"""
content = content.replace(old_cook_ui, new_cook_ui)

# 4. Modify cookRecipe function
old_cookRecipe = """        function cookRecipe(recipeId) {
            const recipe = RECIPES[recipeId];
            if (!recipe) return;

            // Double check ingredients
            let canCook = true;
            Object.entries(recipe.req).forEach(([reqId, reqQty]) => {
                if ((state.inventory.products[reqId] || 0) < reqQty) canCook = false;
            });

            if (canCook) {
                // Deduct ingredients
                Object.entries(recipe.req).forEach(([reqId, reqQty]) => {
                    state.inventory.products[reqId] -= reqQty;
                });
                // Add product
                state.inventory.products[recipeId] = (state.inventory.products[recipeId] || 0) + 1;
                
                trackStat(`cook_${recipeId}`, 1);
                addXP(recipe.xp);
                updateUI();
                
                showAlert('ทำอาหารสำเร็จ!', `คุณทำ ${recipe.name} เสร็จแล้ว กลิ่นหอมน่าทานมาก!`, recipe.emoji);
            }
        }"""
new_cookRecipe = """        function cookRecipe(recipeId) {
            const recipe = RECIPES[recipeId];
            if (!recipe) return;

            const qtyInput = document.getElementById(`qty-${recipeId}`);
            const qty = parseInt(qtyInput ? qtyInput.value : 1) || 1;
            if (qty < 1) return;

            // Double check ingredients
            let canCook = true;
            Object.entries(recipe.req).forEach(([reqId, reqQty]) => {
                if ((state.inventory.products[reqId] || 0) < reqQty * qty) canCook = false;
            });

            if (canCook) {
                // Deduct ingredients
                Object.entries(recipe.req).forEach(([reqId, reqQty]) => {
                    state.inventory.products[reqId] -= reqQty * qty;
                });
                // Add product
                state.inventory.products[recipeId] = (state.inventory.products[recipeId] || 0) + qty;
                
                trackStat(`cook_${recipeId}`, qty);
                let xpBonus = 1;
                if (state.upgrades && state.upgrades.master_chef) {
                    xpBonus += state.upgrades.master_chef * 0.1;
                }
                addXP(Math.floor(recipe.xp * qty * xpBonus));
                updateUI();
                
                showAlert('ทำอาหารสำเร็จ!', `คุณทำ ${recipe.name} x${qty} เสร็จแล้ว กลิ่นหอมน่าทานมาก!`, recipe.emoji);
            } else {
                showAlert('วัตถุดิบไม่พอ', `คุณมีวัตถุดิบไม่พอสำหรับทำ ${qty} จาน!`, '❌');
            }
        }"""
content = content.replace(old_cookRecipe, new_cookRecipe)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_cook = """        function cookRecipe(recipeId) {
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
                // Find empty slot
                const emptySlot = state.cookingSlots.find(s => !s.recipeId);
                if (!emptySlot) {
                    showAlert('เตาเต็ม!', 'เตาปรุงอาหารเต็มแล้ว โปรดรอให้เมนูปัจจุบันเสร็จก่อน', '🍳');
                    return;
                }

                // Deduct ingredients
                Object.entries(recipe.req).forEach(([reqId, reqQty]) => {
                    state.inventory.products[reqId] -= reqQty * qty;
                });
                
                // Start cooking
                let timeMs = (recipe.xp * 500) * qty;
                if (timeMs < 3000) timeMs = 3000;
                if (timeMs > 300000) timeMs = 300000;

                emptySlot.recipeId = recipeId;
                emptySlot.startTime = Date.now();
                emptySlot.qty = qty;
                emptySlot.cookTime = timeMs;

                updateUI();
                showAlert('เริ่มปรุงอาหาร!', `กำลังทำ ${recipe.name} x${qty} โปรดรอสักครู่`, '🍳');
            } else {
                showAlert('วัตถุดิบไม่พอ!', 'คุณมีวัตถุดิบไม่เพียงพอสำหรับทำเมนูนี้', '❌');
            }
        }"""

new_cook = """        function cookRecipe(recipeId) {
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
                if (!checkBarnCapacity(qty)) {
                    showAlert('โรงนาเต็ม!', 'ไม่สามารถเก็บอาหารได้ โปรดอัปเกรดโรงนาหรือขายของก่อน', '📦');
                    return;
                }
                
                // Deduct ingredients
                Object.entries(recipe.req).forEach(([reqId, reqQty]) => {
                    state.inventory.products[reqId] -= reqQty * qty;
                });
                
                // Add product directly
                state.inventory.products[recipeId] = (state.inventory.products[recipeId] || 0) + qty;
                trackStat(`cook_${recipeId}`, qty);
                
                let xpBonus = 1;
                if (state.upgrades && state.upgrades.master_chef) {
                    xpBonus += state.upgrades.master_chef * 0.005;
                }
                addXP(Math.floor(recipe.xp * qty * xpBonus));

                updateUI();
                showAlert('ทำอาหารสำเร็จ!', `ปรุง ${recipe.name} x${qty} เสร็จเรียบร้อยแล้ว`, '🍳');
            } else {
                showAlert('วัตถุดิบไม่พอ!', 'คุณมีวัตถุดิบไม่เพียงพอสำหรับทำเมนูนี้', '❌');
            }
        }"""

if old_cook in content:
    content = content.replace(old_cook, new_cook)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated cookRecipe successfully.")
else:
    print("Could not find old_cook")

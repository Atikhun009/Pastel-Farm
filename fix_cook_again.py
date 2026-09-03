import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_cook = """            if (canCook) {
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

new_cook = """            if (canCook) {
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
        }

        function collectFood(slotId) {
            const slot = state.cookingSlots.find(s => s.id === slotId);
            if (!slot || !slot.recipeId) return;
            
            if (!checkBarnCapacity(slot.qty)) {
                showAlert('โรงนาเต็ม!', 'ไม่สามารถเก็บอาหารได้ โปรดอัปเกรดโรงนาหรือขายของก่อน', '📦');
                return;
            }
            
            const recipe = RECIPES[slot.recipeId];
            
            // Add product
            state.inventory.products[slot.recipeId] = (state.inventory.products[slot.recipeId] || 0) + slot.qty;
            
            trackStat(`cook_${slot.recipeId}`, slot.qty);
            let xpBonus = 1;
            if (state.upgrades && state.upgrades.master_chef) {
                xpBonus += state.upgrades.master_chef * 0.1;
            }
            addXP(Math.floor(recipe.xp * slot.qty * xpBonus));
            
            showAlert('ทำอาหารเสร็จแล้ว!', `คุณได้รับ ${recipe.name} x${slot.qty} กลิ่นหอมน่าทานมาก!`, recipe.emoji);
            if (typeof fireConfetti === 'function') fireConfetti();
            
            // Reset slot
            slot.recipeId = null;
            slot.startTime = null;
            slot.qty = 0;
            slot.cookTime = 0;
            
            updateUI();
        }"""

content = content.replace(old_cook, new_cook)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

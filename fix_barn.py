import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add BARN_UPGRADES to GAME DATA
game_data_marker = "const ACHIEVEMENTS = ["
barn_data = """        const BARN_UPGRADES = [
            { level: 1, capacity: 100, reqGold: 0, reqItems: {} },
            { level: 2, capacity: 250, reqGold: 100000, reqItems: { wheat: 500, corn: 300, potato: 500 } },
            { level: 3, capacity: 600, reqGold: 500000, reqItems: { tomato: 1000, onion: 1000, egg: 300 } },
            { level: 4, capacity: 1500, reqGold: 2000000, reqItems: { strawberry: 2000, milk: 800, bread: 300, cabbage: 1000 } },
            { level: 5, capacity: 4000, reqGold: 8000000, reqItems: { watermelon: 3000, goat_milk: 1000, cake: 300, pumpkin: 1500 } },
            { level: 6, capacity: 10000, reqGold: 25000000, reqItems: { rose: 3000, apple: 2000, pizza: 500, honey: 1000 } },
            { level: 7, capacity: 25000, reqGold: 80000000, reqItems: { peach: 4000, truffle: 1000, goat_cheese: 800, omelet: 1000 } },
            { level: 8, capacity: 60000, reqGold: 250000000, reqItems: { tulip: 5000, coconut: 3000, golden_egg: 800, honey_toast: 1000 } },
            { level: 9, capacity: 150000, reqGold: 800000000, reqItems: { mango: 8000, turkey_egg: 3000, llama_wool: 1000, pineapple_fried_rice: 1500 } },
            { level: 10, capacity: 999999, reqGold: 2500000000, reqItems: { truffle: 3000, golden_egg: 2000, alpaca_wool: 1500, melon_pan: 2000, cake: 2000 } }
        ];

        function getCurrentItemsCount() {
            return Object.values(state.inventory.products).reduce((sum, val) => sum + val, 0);
        }

        function getBarnCapacity() {
            const lvl = state.inventory.barnLevel || 1;
            const upg = BARN_UPGRADES.find(u => u.level === lvl) || BARN_UPGRADES[0];
            return upg.capacity;
        }

        function checkBarnCapacity(amountToAdd) {
            return (getCurrentItemsCount() + amountToAdd) <= getBarnCapacity();
        }
        
"""
content = content.replace(game_data_marker, barn_data + game_data_marker)


# 2. Fix cook logic and collectFood
old_cook_logic = """            if (canCook) {
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
                showAlert('วัตถุดิบไม่พอ!', 'คุณมีวัตถุดิบไม่เพียงพอสำหรับทำเมนูนี้', '❌');
            }
        }"""

new_cook_logic = """            if (canCook) {
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
content = content.replace(old_cook_logic, new_cook_logic)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

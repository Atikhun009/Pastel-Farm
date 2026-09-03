import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. State migration
old_migration = "if (!state.stats) state.stats = {};"
new_migration = """if (!state.stats) state.stats = {};
                    if (!state.cookingSlots) {
                        state.cookingSlots = [
                            { id: 0, recipeId: null, startTime: null, qty: 0, cookTime: 0 },
                            { id: 1, recipeId: null, startTime: null, qty: 0, cookTime: 0 },
                            { id: 2, recipeId: null, startTime: null, qty: 0, cookTime: 0 }
                        ];
                    }"""
content = content.replace(old_migration, new_migration)

# 2. Cooking UI
old_cooking_ui_start = """        function renderCooking() {
            document.getElementById('cooking-recipes').innerHTML = Object.values(RECIPES).map(recipe => {"""

new_cooking_ui_start = """        function renderCooking() {
            // Render Cooking Slots
            const slotsContainer = document.getElementById('cooking-slots-container');
            if (slotsContainer && state.cookingSlots) {
                slotsContainer.innerHTML = state.cookingSlots.map(slot => {
                    if (!slot.recipeId) {
                        return `<div class="glass p-4 rounded-xl flex items-center justify-center text-gray-400 border border-dashed border-gray-300 h-24">เตาว่าง</div>`;
                    }
                    const recipe = RECIPES[slot.recipeId];
                    const now = Date.now();
                    const progress = Math.min((now - slot.startTime) / slot.cookTime, 1);
                    const isDone = progress >= 1;
                    
                    return `
                    <div class="glass p-3 rounded-xl flex flex-col gap-2 relative overflow-hidden">
                        <div class="flex justify-between items-center z-10 relative">
                            <div class="flex items-center gap-2">
                                <span class="text-2xl">${recipe.emoji}</span>
                                <div>
                                    <div class="font-bold text-gray-800 text-sm">${recipe.name} x${slot.qty}</div>
                                    <div class="text-[10px] text-gray-500">${isDone ? 'เสร็จแล้ว!' : 'กำลังปรุง...'}</div>
                                </div>
                            </div>
                            ${isDone ? `<button onclick="collectFood(${slot.id})" class="text-xs font-bold bg-green-500 hover:bg-green-600 text-white px-3 py-1.5 rounded-lg shadow-sm transition animate-pulse">เก็บ</button>` : ''}
                        </div>
                        <div class="h-1.5 bg-gray-200 rounded-full overflow-hidden z-10 relative">
                            <div class="h-full bg-orange-400 transition-all duration-1000" style="width: ${progress * 100}%"></div>
                        </div>
                    </div>`;
                }).join('');
            }

            document.getElementById('cooking-recipes').innerHTML = Object.values(RECIPES).map(recipe => {"""

content = content.replace(old_cooking_ui_start, new_cooking_ui_start)

# 3. Modify cookRecipe and collectFood logic
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
                // Base time: 500ms per 1 XP, scaled by qty. Min 3s, Max 5 mins.
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

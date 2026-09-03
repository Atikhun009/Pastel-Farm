import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_quick_cook = """                        <div id="quick-cook-container" class="flex items-center justify-between bg-white/40 p-2 rounded-xl mb-4">
                            <span class="text-sm font-bold text-blue-900">ทำจำนวน:</span>
                            <div class="flex gap-1">
                                <button onclick="setQuickCook(1)" id="qc-1" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-blue-500 text-white shadow">x1</button>
                                <button onclick="setQuickCook(10)" id="qc-10" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x10</button>
                                <button onclick="setQuickCook(100)" id="qc-100" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x100</button>
                                <button onclick="setQuickCook(1000)" id="qc-1000" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x1000</button>
                            </div>
                        </div>"""

new_quick_cook = """                        <div class="flex flex-col gap-2 mb-4">
                            <div id="quick-cook-container" class="flex items-center justify-between bg-white/40 p-2 rounded-xl">
                                <span class="text-sm font-bold text-blue-900">ทำจำนวน:</span>
                                <div class="flex gap-1">
                                    <button onclick="setQuickCook(1)" id="qc-1" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-blue-500 text-white shadow">x1</button>
                                    <button onclick="setQuickCook(10)" id="qc-10" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x10</button>
                                    <button onclick="setQuickCook(100)" id="qc-100" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x100</button>
                                    <button onclick="setQuickCook(1000)" id="qc-1000" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x1000</button>
                                </div>
                            </div>
                            <button id="btn-toggle-cookable" onclick="toggleCookableOnly()" class="w-full flex justify-between items-center bg-white/40 p-2 rounded-xl text-sm font-bold text-gray-700 hover:bg-white/60 transition-all">
                                <span class="flex items-center gap-1">🍽️ แสดงเฉพาะเมนูที่ทำได้</span>
                                <span id="ui-cookable-status" class="bg-gray-300 text-gray-600 px-2 py-0.5 rounded-lg text-xs">ปิด</span>
                            </button>
                        </div>"""

if old_quick_cook in content:
    content = content.replace(old_quick_cook, new_quick_cook)
    print("quick-cook-container updated")

old_render_cooking = """        function renderCooking() {
            // Cooking slots removed

            document.getElementById('cooking-recipes').innerHTML = Object.values(RECIPES).map(recipe => {
                if (recipe.shopPrice > 0 && !state.inventory.unlockedRecipes.includes(recipe.id)) return '';
                const isLocked = state.level < recipe.unlockLevel;
                
                // Build requirement string and check if cookable
                let canCook = true;
                const reqHtml = Object.entries(recipe.req).map(([reqId, reqQty]) => {
                    const hasQty = state.inventory.products[reqId] || 0;
                    const totalReq = reqQty * quickCookAmount;
                    if (hasQty < totalReq) canCook = false;
                    const pItem = PRODUCTS[reqId] || RECIPES[reqId];
                    return `<span class="inline-flex items-center gap-1 bg-white/50 px-2 py-0.5 rounded text-[10px] ${hasQty >= totalReq ? 'text-green-700' : 'text-red-600 font-bold'}">
                        ${pItem ? pItem.emoji : '❓'} ${hasQty}/${totalReq}
                    </span>`;
                }).join(' ');

                return `
                <div class="glass p-4 rounded-xl flex flex-col gap-3 ${isLocked ? 'opacity-60 grayscale' : 'hover:bg-white/60'} transition">
                    <div class="flex justify-between items-center">
                        <div class="flex items-center gap-3">
                            <span class="text-4xl bg-white/50 p-2 rounded-lg shadow-sm">${isLocked ? '🔒' : recipe.emoji}</span>
                            <div>
                                <div class="font-bold text-gray-800 text-lg">${recipe.name} ${isLocked ? `<span class="text-[10px] text-red-500 ml-1">ปลดล็อก Lv.${recipe.unlockLevel}</span>` : ''}</div>
                                <div class="text-xs font-semibold text-green-600">ได้รับ ${recipe.xp} XP</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-2">
                            <button onclick="cookRecipe('${recipe.id}')" class="glass-btn px-4 py-2.5 rounded-xl text-sm font-bold text-blue-700 shadow-sm whitespace-nowrap bg-blue-50/50" ${isLocked || !canCook ? 'disabled' : ''}>
                                <span class="text-[10px] text-blue-500 mr-1">x${quickCookAmount}</span>ทำอาหาร
                            </button>
                        </div>
                    </div>
                    <div class="flex flex-wrap gap-1 mt-1 items-center">
                        <span class="text-[10px] font-bold text-gray-500 mr-1">วัตถุดิบ:</span>
                        ${isLocked ? '<span class="text-[10px] text-gray-400">? ? ?</span>' : reqHtml}
                    </div>
                </div>
            `}).join('');
        }"""

new_render_cooking = """        let isCookableOnly = false;
        
        function toggleCookableOnly() {
            isCookableOnly = !isCookableOnly;
            const statusEl = document.getElementById('ui-cookable-status');
            if (statusEl) {
                if (isCookableOnly) {
                    statusEl.innerText = 'เปิด';
                    statusEl.className = 'bg-blue-500 text-white px-2 py-0.5 rounded-lg text-xs font-bold shadow-sm';
                } else {
                    statusEl.innerText = 'ปิด';
                    statusEl.className = 'bg-gray-300 text-gray-600 px-2 py-0.5 rounded-lg text-xs font-bold shadow-sm';
                }
            }
            renderCooking();
        }

        function renderCooking() {
            // Cooking slots removed

            let html = Object.values(RECIPES).map(recipe => {
                if (recipe.shopPrice > 0 && !state.inventory.unlockedRecipes.includes(recipe.id)) return '';
                const isLocked = state.level < recipe.unlockLevel;
                
                // Build requirement string and check if cookable
                let canCook = true;
                const reqHtml = Object.entries(recipe.req).map(([reqId, reqQty]) => {
                    const hasQty = state.inventory.products[reqId] || 0;
                    const totalReq = reqQty * quickCookAmount;
                    if (hasQty < totalReq) canCook = false;
                    const pItem = PRODUCTS[reqId] || RECIPES[reqId];
                    return `<span class="inline-flex items-center gap-1 bg-white/50 px-2 py-0.5 rounded text-[10px] ${hasQty >= totalReq ? 'text-green-700' : 'text-red-600 font-bold'}">
                        ${pItem ? pItem.emoji : '❓'} ${hasQty}/${totalReq}
                    </span>`;
                }).join(' ');
                
                if (isCookableOnly && (isLocked || !canCook)) return '';

                return `
                <div class="glass p-4 rounded-xl flex flex-col gap-3 ${isLocked ? 'opacity-60 grayscale' : 'hover:bg-white/60'} transition">
                    <div class="flex justify-between items-center">
                        <div class="flex items-center gap-3">
                            <span class="text-4xl bg-white/50 p-2 rounded-lg shadow-sm">${isLocked ? '🔒' : recipe.emoji}</span>
                            <div>
                                <div class="font-bold text-gray-800 text-lg">${recipe.name} ${isLocked ? `<span class="text-[10px] text-red-500 ml-1">ปลดล็อก Lv.${recipe.unlockLevel}</span>` : ''}</div>
                                <div class="text-xs font-semibold text-green-600">ได้รับ ${recipe.xp} XP</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-2">
                            <button onclick="cookRecipe('${recipe.id}')" class="glass-btn px-4 py-2.5 rounded-xl text-sm font-bold text-blue-700 shadow-sm whitespace-nowrap bg-blue-50/50" ${isLocked || !canCook ? 'disabled' : ''}>
                                <span class="text-[10px] text-blue-500 mr-1">x${quickCookAmount}</span>ทำอาหาร
                            </button>
                        </div>
                    </div>
                    <div class="flex flex-wrap gap-1 mt-1 items-center">
                        <span class="text-[10px] font-bold text-gray-500 mr-1">วัตถุดิบ:</span>
                        ${isLocked ? '<span class="text-[10px] text-gray-400">? ? ?</span>' : reqHtml}
                    </div>
                </div>
            `}).join('');
            
            if (html === '') {
                html = `<div class="text-center text-gray-500 py-8 bg-white/30 rounded-xl">ไม่มีเมนูที่ทำได้ในขณะนี้</div>`;
            }
            document.getElementById('cooking-recipes').innerHTML = html;
        }"""

if old_render_cooking in content:
    content = content.replace(old_render_cooking, new_render_cooking)
    print("renderCooking updated")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

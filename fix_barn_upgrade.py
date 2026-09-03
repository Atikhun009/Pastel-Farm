import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add barnSubmissions to state fallback
old_state = "if (!state.inventory.fertilizer) state.inventory.fertilizer = 0;"
new_state = "if (!state.inventory.fertilizer) state.inventory.fertilizer = 0;\n                    if (!state.inventory.barnSubmissions) state.inventory.barnSubmissions = {};"
content = content.replace(old_state, new_state)

old_modal = """                let reqHtml = Object.entries(nextUpg.reqItems).map(([reqId, reqQty]) => {
                    let hasQty = state.inventory.products[reqId] || 0;
                    if (hasQty < reqQty) canUpgrade = false;
                    let pItem = PRODUCTS[reqId] || ANIMALS[reqId] || RECIPES[reqId]; // Can be any item
                    if(!pItem && reqId === 'duck_egg') pItem = {emoji:'🥚', name:'ไข่เป็ด'}; // fallback
                    let emoji = pItem ? pItem.emoji : '📦';
                    return `
                        <div class="flex items-center justify-between bg-white/60 p-2 rounded-xl text-sm">
                            <span class="flex items-center gap-2">${emoji} ${pItem ? pItem.name : reqId}</span>
                            <span class="${hasQty >= reqQty ? 'text-green-600' : 'text-red-500'} font-bold">${hasQty}/${reqQty}</span>
                        </div>
                    `;
                }).join('');
                
                content.innerHTML = `
                    <div class="flex items-center justify-center gap-4 mb-2">
                        <div class="text-center bg-gray-100 p-3 rounded-2xl flex-1">
                            <div class="text-xs text-gray-500">ปัจจุบัน Lv.${lvl}</div>
                            <div class="font-bold text-lg text-gray-800">${curUpg.capacity} <span class="text-xs">ชิ้น</span></div>
                        </div>
                        <div class="text-2xl text-gray-300">➔</div>
                        <div class="text-center bg-blue-50 p-3 rounded-2xl flex-1 border border-blue-100 shadow-inner">
                            <div class="text-xs text-blue-500">Lv.${lvl + 1}</div>
                            <div class="font-bold text-lg text-blue-800">${nextUpg.capacity} <span class="text-xs">ชิ้น</span></div>
                        </div>
                    </div>
                    
                    <div class="bg-gray-50 p-3 rounded-xl">
                        <div class="text-xs font-bold text-gray-500 mb-2">วัตถุดิบที่ต้องใช้:</div>
                        <div class="space-y-2 mb-3">
                            <div class="flex items-center justify-between bg-white/60 p-2 rounded-xl text-sm">
                                <span class="flex items-center gap-2">🪙 เหรียญทอง</span>
                                <span class="${state.gold >= nextUpg.reqGold ? 'text-amber-600' : 'text-red-500'} font-bold">${state.gold}/${nextUpg.reqGold}</span>
                            </div>
                            ${reqHtml}
                        </div>
                    </div>
                    
                    <button onclick="upgradeBarn()" class="w-full py-3 rounded-xl font-bold shadow-md transition ${canUpgrade ? 'bg-blue-500 text-white hover:bg-blue-600' : 'bg-gray-200 text-gray-400 cursor-not-allowed'}">
                        อัปเกรดเลย!
                    </button>
                `;"""

new_modal = """                let reqHtml = Object.entries(nextUpg.reqItems).map(([reqId, reqQty]) => {
                    if (!state.inventory.barnSubmissions) state.inventory.barnSubmissions = {};
                    let submittedQty = state.inventory.barnSubmissions[reqId] || 0;
                    let remainingReq = Math.max(0, reqQty - submittedQty);
                    
                    let hasQty = state.inventory.products[reqId] || 0;
                    if (submittedQty < reqQty) canUpgrade = false;
                    
                    let pItem = PRODUCTS[reqId] || ANIMALS[reqId] || RECIPES[reqId] || SEEDS[reqId];
                    if(!pItem && reqId === 'duck_egg') pItem = {emoji:'🥚', name:'ไข่เป็ด'};
                    let emoji = pItem ? pItem.emoji : '📦';
                    
                    let canSubmitAmount = Math.min(remainingReq, hasQty);
                    
                    return `
                        <div class="flex flex-col bg-white/60 p-2 rounded-xl text-sm mb-2 gap-2">
                            <div class="flex items-center justify-between">
                                <span class="flex items-center gap-2">${emoji} ${pItem ? pItem.name : reqId}</span>
                                <span class="${submittedQty >= reqQty ? 'text-green-600' : 'text-amber-500'} font-bold">${submittedQty}/${reqQty}</span>
                            </div>
                            ${submittedQty < reqQty ? `
                            <div class="flex items-center justify-between">
                                <span class="text-xs text-gray-500">ในกระเป๋า: ${hasQty}</span>
                                <button onclick="submitBarnItem('${reqId}', ${canSubmitAmount})" class="px-3 py-1 rounded-lg text-xs font-bold ${canSubmitAmount > 0 ? 'bg-blue-500 text-white hover:bg-blue-600' : 'bg-gray-200 text-gray-400 cursor-not-allowed'}">
                                    ส่งของ ${canSubmitAmount > 0 ? `(${canSubmitAmount})` : ''}
                                </button>
                            </div>
                            ` : `<div class="text-xs text-green-500 font-bold text-right">ส่งครบแล้ว ✅</div>`}
                        </div>
                    `;
                }).join('');
                
                content.innerHTML = `
                    <div class="flex items-center justify-center gap-4 mb-2">
                        <div class="text-center bg-gray-100 p-3 rounded-2xl flex-1">
                            <div class="text-xs text-gray-500">ปัจจุบัน Lv.${lvl}</div>
                            <div class="font-bold text-lg text-gray-800">${curUpg.capacity} <span class="text-xs">ชิ้น</span></div>
                        </div>
                        <div class="text-2xl text-gray-300">➔</div>
                        <div class="text-center bg-blue-50 p-3 rounded-2xl flex-1 border border-blue-100 shadow-inner">
                            <div class="text-xs text-blue-500">Lv.${lvl + 1}</div>
                            <div class="font-bold text-lg text-blue-800">${nextUpg.capacity} <span class="text-xs">ชิ้น</span></div>
                        </div>
                    </div>
                    
                    <div class="bg-gray-50 p-3 rounded-xl">
                        <div class="text-xs font-bold text-gray-500 mb-2">วัตถุดิบที่ต้องใช้ (ทยอยส่งได้):</div>
                        <div class="space-y-1 mb-3">
                            <div class="flex flex-col bg-white/60 p-2 rounded-xl text-sm mb-2 gap-2">
                                <div class="flex items-center justify-between">
                                    <span class="flex items-center gap-2">🪙 เหรียญทอง</span>
                                    <span class="${state.gold >= nextUpg.reqGold ? 'text-amber-600' : 'text-red-500'} font-bold">${state.gold}/${nextUpg.reqGold}</span>
                                </div>
                                <div class="text-xs text-gray-400">เงินจะถูกหักเมื่อกดอัปเกรด</div>
                            </div>
                            ${reqHtml}
                        </div>
                    </div>
                    
                    <button onclick="upgradeBarn()" class="w-full py-3 rounded-xl font-bold shadow-md transition ${canUpgrade ? 'bg-blue-500 text-white hover:bg-blue-600' : 'bg-gray-200 text-gray-400 cursor-not-allowed'}">
                        อัปเกรดเลย!
                    </button>
                `;"""

content = content.replace(old_modal, new_modal)

old_upgrade = """        function upgradeBarn() {
            const lvl = state.inventory.barnLevel || 1;
            if (lvl >= 10) return;
            
            const nextUpg = BARN_UPGRADES.find(u => u.level === lvl + 1);
            
            // Check again
            if (state.gold < nextUpg.reqGold) return;
            let canUpgrade = true;
            Object.entries(nextUpg.reqItems).forEach(([reqId, reqQty]) => {
                if ((state.inventory.products[reqId] || 0) < reqQty) canUpgrade = false;
            });
            
            if (!canUpgrade) return;
            
            // Deduct
            state.gold -= nextUpg.reqGold;
            Object.entries(nextUpg.reqItems).forEach(([reqId, reqQty]) => {
                state.inventory.products[reqId] -= reqQty;
            });
            
            // Upgrade
            state.inventory.barnLevel = lvl + 1;"""

new_upgrade = """        function submitBarnItem(reqId, amount) {
            if (amount <= 0) return;
            if (!state.inventory.barnSubmissions) state.inventory.barnSubmissions = {};
            
            state.inventory.products[reqId] -= amount;
            state.inventory.barnSubmissions[reqId] = (state.inventory.barnSubmissions[reqId] || 0) + amount;
            
            // Refresh modal
            openBarnUpgradeModal();
            updateUI();
        }

        function upgradeBarn() {
            const lvl = state.inventory.barnLevel || 1;
            if (lvl >= 10) return;
            
            const nextUpg = BARN_UPGRADES.find(u => u.level === lvl + 1);
            if (!state.inventory.barnSubmissions) state.inventory.barnSubmissions = {};
            
            // Check again
            if (state.gold < nextUpg.reqGold) return;
            let canUpgrade = true;
            Object.entries(nextUpg.reqItems).forEach(([reqId, reqQty]) => {
                if ((state.inventory.barnSubmissions[reqId] || 0) < reqQty) canUpgrade = false;
            });
            
            if (!canUpgrade) return;
            
            // Deduct Gold
            state.gold -= nextUpg.reqGold;
            
            // Upgrade
            state.inventory.barnLevel = lvl + 1;
            
            // Clear submissions for next level
            state.inventory.barnSubmissions = {};"""

content = content.replace(old_upgrade, new_upgrade)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

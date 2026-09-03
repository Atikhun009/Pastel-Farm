import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

barn_modal = """    <!-- Barn Upgrade Modal -->
    <div id="modal-barn-upgrade" class="fixed inset-0 bg-blue-900/40 backdrop-blur-md z-50 flex items-center justify-center transition-all duration-300 hidden-scale">
        <div class="bg-gradient-to-b from-white to-blue-50/95 backdrop-blur-xl p-6 md:p-8 rounded-[2.5rem] max-w-md w-full mx-4 shadow-[0_20px_60px_-15px_rgba(0,0,0,0.3)] shadow-blue-900/20 border-[3px] border-white/70">
            <div class="flex justify-between items-center mb-6">
                <h3 class="text-xl font-bold text-blue-900 flex items-center gap-2"><span class="text-2xl">📦</span> อัปเกรดโรงนา</h3>
                <button onclick="closeBarnUpgradeModal()" class="w-8 h-8 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-full text-gray-500 transition">✕</button>
            </div>
            
            <div id="barn-upgrade-content" class="space-y-4">
                <!-- Dynamic Content Here -->
            </div>
        </div>
    </div>
"""

content = content.replace("    <!-- JavaScript Game Logic -->", barn_modal + "\n    <!-- JavaScript Game Logic -->")


barn_functions = """        function openBarnUpgradeModal() {
            const modal = document.getElementById('modal-barn-upgrade');
            const content = document.getElementById('barn-upgrade-content');
            
            const lvl = state.inventory.barnLevel || 1;
            
            if (lvl >= 10) {
                content.innerHTML = `
                    <div class="text-center py-6">
                        <div class="text-4xl mb-3">👑</div>
                        <div class="font-bold text-xl text-blue-900 mb-2">โรงนาเลเวลสูงสุดแล้ว!</div>
                        <div class="text-gray-500 text-sm">คุณมีพื้นที่เก็บของแบบไม่จำกัด</div>
                    </div>
                `;
            } else {
                const curUpg = BARN_UPGRADES.find(u => u.level === lvl);
                const nextUpg = BARN_UPGRADES.find(u => u.level === lvl + 1);
                
                let canUpgrade = true;
                if (state.gold < nextUpg.reqGold) canUpgrade = false;
                
                let reqHtml = Object.entries(nextUpg.reqItems).map(([reqId, reqQty]) => {
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
                        <div class="text-blue-500">➡️</div>
                        <div class="text-center bg-blue-100 p-3 rounded-2xl flex-1 border-2 border-blue-200">
                            <div class="text-xs text-blue-600">ระดับถัดไป Lv.${lvl+1}</div>
                            <div class="font-bold text-lg text-blue-900">${nextUpg.capacity >= 999999 ? 'MAX' : nextUpg.capacity} <span class="text-xs">ชิ้น</span></div>
                        </div>
                    </div>
                    
                    <div class="mt-4">
                        <h4 class="text-xs font-bold text-gray-500 uppercase mb-2">เงื่อนไขการอัปเกรด:</h4>
                        <div class="space-y-2 mb-4">
                            <div class="flex items-center justify-between bg-white/60 p-2 rounded-xl text-sm">
                                <span class="flex items-center gap-2">🪙 ทองคำ</span>
                                <span class="${state.gold >= nextUpg.reqGold ? 'text-green-600' : 'text-red-500'} font-bold">${state.gold}/${nextUpg.reqGold}</span>
                            </div>
                            ${reqHtml}
                        </div>
                        
                        <button onclick="upgradeBarn()" class="w-full glass-btn ${canUpgrade ? 'bg-blue-500 hover:bg-blue-600 text-white border-blue-400' : 'bg-gray-200 text-gray-500'} py-3 rounded-xl font-bold shadow-sm" ${!canUpgrade ? 'disabled' : ''}>
                            อัปเกรดเลย!
                        </button>
                    </div>
                `;
            }
            
            modal.classList.remove('hidden-scale');
            modal.classList.add('visible-scale');
        }
        
        function closeBarnUpgradeModal() {
            const modal = document.getElementById('modal-barn-upgrade');
            modal.classList.remove('visible-scale');
            modal.classList.add('hidden-scale');
        }
        
        function upgradeBarn() {
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
            state.inventory.barnLevel = lvl + 1;
            
            closeBarnUpgradeModal();
            updateUI();
            
            showAlert('อัปเกรดโรงนาสำเร็จ!', `ยินดีด้วย! พื้นที่เก็บของเพิ่มเป็น ${nextUpg.capacity >= 999999 ? 'MAX' : nextUpg.capacity} ชิ้นแล้ว`, '🎉');
            if (typeof fireConfetti === 'function') fireConfetti();
        }"""

content = content.replace("        function closeAnimalModal() {", barn_functions + "\n        function closeAnimalModal() {")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

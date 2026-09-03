import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add quick upgrade container to market-sec-upgrades
old_market_upgrades = """                        <div id="market-sec-upgrades" class="market-section hidden">
                            <div id="market-upgrades" class="space-y-3"></div>"""

new_market_upgrades = """                        <div id="market-sec-upgrades" class="market-section hidden">
                            <div id="quick-upgrade-container" class="flex items-center justify-between bg-white/40 p-2 rounded-xl mb-4">
                                <span class="text-sm font-bold text-purple-900">อัปเกรด:</span>
                                <div class="flex gap-1">
                                    <button onclick="setQuickUpgrade(1)" id="qu-1" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-purple-500 text-white shadow">x1</button>
                                    <button onclick="setQuickUpgrade(5)" id="qu-5" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x5</button>
                                    <button onclick="setQuickUpgrade(10)" id="qu-10" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x10</button>
                                </div>
                            </div>
                            <div id="market-upgrades" class="space-y-3"></div>"""
if old_market_upgrades in content:
    content = content.replace(old_market_upgrades, new_market_upgrades)
    print("Market upgrades UI updated")

# 2. Add setQuickUpgrade and quickUpgradeAmount
old_set_qb = """        let quickCookAmount = 1;

        function setQuickCook(amt) {"""
new_set_qb = """        let quickUpgradeAmount = 1;
        
        function setQuickUpgrade(amt) {
            quickUpgradeAmount = amt;
            if(!document.getElementById('qu-1')) return;
            document.getElementById('qu-1').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickUpgradeAmount === 1 ? 'bg-purple-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            document.getElementById('qu-5').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickUpgradeAmount === 5 ? 'bg-purple-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            document.getElementById('qu-10').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickUpgradeAmount === 10 ? 'bg-purple-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            renderMarket();
        }
        
        let quickCookAmount = 1;

        function setQuickCook(amt) {"""
if old_set_qb in content:
    content = content.replace(old_set_qb, new_set_qb)
    print("setQuickUpgrade function added")

# 3. Update renderMarket to calculate cost for quickUpgradeAmount
old_render_market_upgrades = """            let upgradesHtml = Object.values(UPGRADES).map(u => {
                const curLevel = state.upgrades[u.id] || 0;
                const isMax = curLevel >= u.maxLevel;
                let nextPrice = Math.floor(u.buyPrice * Math.pow(u.priceMult, curLevel));
                if (state.upgrades && state.upgrades.upgrade_discount) {
                    nextPrice = Math.floor(nextPrice * (1 - (state.upgrades.upgrade_discount * 0.005)));
                }
                return `
                <div class="glass p-3 rounded-xl flex justify-between items-center ${isMax ? 'bg-gray-50/50 opacity-60' : 'hover:bg-white/60'} transition">
                    <div class="flex items-center gap-3">
                        <span class="text-3xl bg-white/50 p-2 rounded-lg shadow-sm">${u.emoji}</span>
                        <div>
                            <div class="font-bold text-gray-800">${u.name} ${curLevel > 0 ? `<span class="text-xs text-purple-600 font-bold ml-1">Lv.${curLevel}</span>` : ''}</div>
                            <div class="text-xs font-semibold text-gray-500">${u.desc}</div>
                        </div>
                    </div>
                    ${isMax ? `<span class="text-sm font-bold text-gray-500 px-4 py-2">MAX</span>` 
                    : `<button onclick="buyDynamicUpgrade('${u.id}')" class="relative group glass-btn px-4 py-2 rounded-xl text-sm font-bold text-purple-700 shadow-sm whitespace-nowrap" ${state.gold < nextPrice ? 'disabled' : ''}>
                        ${nextPrice} 🪙
                    </button>`}
                </div>
                `;
            }).join('');"""

new_render_market_upgrades = """            let upgradesHtml = Object.values(UPGRADES).map(u => {
                const curLevel = state.upgrades[u.id] || 0;
                const isMax = curLevel >= u.maxLevel;
                
                let targetQty = Math.min(quickUpgradeAmount, u.maxLevel - curLevel);
                if(targetQty < 1) targetQty = 1;
                
                let nextPrice = 0;
                let actualQty = 0;
                
                for(let i = 0; i < targetQty; i++) {
                    let cost = Math.floor(u.buyPrice * Math.pow(u.priceMult, curLevel + i));
                    if (state.upgrades && state.upgrades.upgrade_discount) {
                        cost = Math.floor(cost * (1 - (state.upgrades.upgrade_discount * 0.005)));
                    }
                    if (state.gold < nextPrice + cost && i > 0) break; // if can't afford next level but already bought some, stop calculating
                    nextPrice += cost;
                    actualQty++;
                }

                const canAfford = state.gold >= nextPrice && nextPrice > 0;
                
                return `
                <div class="glass p-3 rounded-xl flex justify-between items-center ${isMax ? 'bg-gray-50/50 opacity-60' : 'hover:bg-white/60'} transition">
                    <div class="flex items-center gap-3">
                        <span class="text-3xl bg-white/50 p-2 rounded-lg shadow-sm">${u.emoji}</span>
                        <div>
                            <div class="font-bold text-gray-800">${u.name} ${curLevel > 0 ? `<span class="text-xs text-purple-600 font-bold ml-1">Lv.${curLevel}</span>` : ''}</div>
                            <div class="text-xs font-semibold text-gray-500">${u.desc}</div>
                        </div>
                    </div>
                    ${isMax ? `<span class="text-sm font-bold text-gray-500 px-4 py-2">MAX</span>` 
                    : `<button onclick="buyDynamicUpgrade('${u.id}', ${actualQty})" class="relative flex flex-col items-center group glass-btn px-4 py-1.5 rounded-xl text-sm font-bold text-purple-700 shadow-sm whitespace-nowrap" ${!canAfford ? 'disabled' : ''}>
                        <span class="text-[10px] text-purple-500 mr-1">อัป x${actualQty}</span>
                        <span>${nextPrice} 🪙</span>
                    </button>`}
                </div>
                `;
            }).join('');"""

if old_render_market_upgrades in content:
    content = content.replace(old_render_market_upgrades, new_render_market_upgrades)
    print("renderMarket logic for upgrades updated")

# 4. Update buyDynamicUpgrade
old_buy_dynamic = """        function buyDynamicUpgrade(id) {
            const u = UPGRADES[id];
            const curLevel = state.upgrades[id] || 0;
            if (curLevel >= u.maxLevel) return;
            let nextPrice = Math.floor(u.buyPrice * Math.pow(u.priceMult, curLevel));
                if (state.upgrades && state.upgrades.upgrade_discount) {
                    nextPrice = Math.floor(nextPrice * (1 - (state.upgrades.upgrade_discount * 0.005)));
                }
            
            if (state.gold >= nextPrice) {
                state.gold -= nextPrice;
                state.upgrades[id] = curLevel + 1;
                showAlert('ซื้อสำเร็จ', `อัปเกรด ${u.name} เป็นเลเวล ${curLevel + 1} แล้ว!`, u.emoji);"""

new_buy_dynamic = """        function buyDynamicUpgrade(id, targetQty = 1) {
            const u = UPGRADES[id];
            const curLevel = state.upgrades[id] || 0;
            if (curLevel >= u.maxLevel) return;
            
            let totalPrice = 0;
            let finalQty = 0;
            for(let i = 0; i < targetQty; i++) {
                if (curLevel + i >= u.maxLevel) break;
                let cost = Math.floor(u.buyPrice * Math.pow(u.priceMult, curLevel + i));
                if (state.upgrades && state.upgrades.upgrade_discount) {
                    cost = Math.floor(cost * (1 - (state.upgrades.upgrade_discount * 0.005)));
                }
                if (state.gold < totalPrice + cost) break;
                totalPrice += cost;
                finalQty++;
            }
            
            if (finalQty > 0 && state.gold >= totalPrice) {
                state.gold -= totalPrice;
                state.upgrades[id] = curLevel + finalQty;
                showToast('อัปเกรดสำเร็จ', `อัปเกรด ${u.name} ขึ้น ${finalQty} เลเวล (รวมLv.${curLevel + finalQty})`, u.emoji);"""

if old_buy_dynamic in content:
    content = content.replace(old_buy_dynamic, new_buy_dynamic)
    print("buyDynamicUpgrade updated")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

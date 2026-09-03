import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_inv = """            const prodEntries = Object.entries(state.inventory.products).filter(([_, qty]) => qty > 0);
            if (prodEntries.length === 0) {
                document.getElementById('inv-products').innerHTML = '<div class="text-sm text-gray-500 text-center py-8 bg-white/30 rounded-xl">ยังไม่มีผลผลิต<br/><span class="text-xs">ปลูกผัก, เลี้ยงสัตว์ หรือทำอาหารเพื่อนำมาขาย</span></div>';
            } else {
                document.getElementById('inv-products').innerHTML = prodEntries.map(([id, qty]) => {
                    const prod = PRODUCTS[id];
                    const mult = state.marketMultipliers[id] || 1;
                    const sellPrice = Math.floor(prod.basePrice * mult);
                    const totalValue = sellPrice * qty;
                    
                    let trendIcon = '➖';
                    let trendColor = 'text-gray-500';
                    if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-red-500'; } 
                    else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-green-600'; }

                    return `
                    <div class="glass p-3 rounded-xl flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <span class="text-3xl">${prod.emoji}</span>
                            <div>
                                <div class="font-bold text-sm text-gray-800">${prod.name}</div>
                                <div class="text-[10px] text-gray-500 font-semibold"><span class="${trendColor}">${trendIcon}</span> ชิ้นละ ${sellPrice} 🪙</div>
                            </div>
                        </div>
                        <div class="text-right">
                            <div class="text-lg font-bold text-amber-600">x${qty}</div>
                            <button onclick="sellProduct('${id}', ${qty}, ${totalValue})" class="text-xs bg-amber-100 text-amber-700 font-bold px-2 py-1 rounded shadow-sm hover:bg-amber-200 transition">
                                ขาย (+${totalValue} 🪙)
                            </button>
                        </div>
                    </div>
                    `;
                }).join('');
            }"""

new_inv = """            const prodEntries = Object.entries(state.inventory.products).filter(([_, qty]) => qty > 0);
            if (prodEntries.length === 0) {
                document.getElementById('inv-products').innerHTML = '<div class="text-sm text-gray-500 text-center py-8 bg-white/30 rounded-xl">ยังไม่มีผลผลิต<br/><span class="text-xs">ปลูกผัก, เลี้ยงสัตว์ หรือทำอาหารเพื่อนำมาขาย</span></div>';
            } else {
                let cropHtml = '<h4 class="text-xs font-bold text-gray-500 mb-2 mt-2">🌾 พืชผล</h4>';
                let animalHtml = '<h4 class="text-xs font-bold text-gray-500 mb-2 mt-4">🐾 ผลผลิตจากสัตว์</h4>';
                let foodHtml = '<h4 class="text-xs font-bold text-gray-500 mb-2 mt-4">🍳 อาหาร</h4>';
                
                let hasCrops = false;
                let hasAnimals = false;
                let hasFoods = false;

                const renderItem = ([id, qty]) => {
                    let prod = PRODUCTS[id] || RECIPES[id];
                    if (!prod) return '';
                    const basePrice = prod.basePrice || (prod.shopPrice * 1.5) || 100;
                    const mult = state.marketMultipliers[id] || 1;
                    const sellPrice = Math.floor(basePrice * mult);
                    const totalValue = sellPrice * qty;
                    
                    let trendIcon = '➖';
                    let trendColor = 'text-gray-500';
                    if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-red-500'; } 
                    else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-green-600'; }

                    return `
                    <div class="glass p-3 rounded-xl flex items-center justify-between mb-2">
                        <div class="flex items-center gap-3">
                            <span class="text-3xl">${prod.emoji}</span>
                            <div>
                                <div class="font-bold text-sm text-gray-800">${prod.name}</div>
                                <div class="text-[10px] text-gray-500 font-semibold"><span class="${trendColor}">${trendIcon}</span> ชิ้นละ ${sellPrice} 🪙</div>
                            </div>
                        </div>
                        <div class="text-right">
                            <div class="text-lg font-bold text-amber-600">x${qty}</div>
                            <button onclick="sellProduct('${id}', ${qty}, ${totalValue})" class="text-xs bg-amber-100 text-amber-700 font-bold px-2 py-1 rounded shadow-sm hover:bg-amber-200 transition">
                                ขาย (+${totalValue} 🪙)
                            </button>
                        </div>
                    </div>
                    `;
                };

                prodEntries.forEach(entry => {
                    const id = entry[0];
                    if (RECIPES[id]) {
                        foodHtml += renderItem(entry);
                        hasFoods = true;
                    } else if (Object.values(ANIMALS).some(a => a.produces === id)) {
                        animalHtml += renderItem(entry);
                        hasAnimals = true;
                    } else {
                        cropHtml += renderItem(entry);
                        hasCrops = true;
                    }
                });
                
                document.getElementById('inv-products').innerHTML = 
                    (hasCrops ? cropHtml : '') + 
                    (hasAnimals ? animalHtml : '') + 
                    (hasFoods ? foodHtml : '');
            }"""
            
content = content.replace(old_inv, new_inv)

# also fix sellAllInventory logic to calculate correctly for food which doesn't exist in PRODUCTS
old_sellAll = """            prodEntries.forEach(([id, qty]) => {
                const prod = PRODUCTS[id];
                const mult = state.marketMultipliers[id] || 1;
                const sellPrice = Math.floor(prod.basePrice * mult);
                totalValue += sellPrice * qty;
                totalItems += qty;
                state.inventory.products[id] = 0;
            });"""
new_sellAll = """            prodEntries.forEach(([id, qty]) => {
                const prod = PRODUCTS[id] || RECIPES[id];
                const basePrice = prod.basePrice || (prod.shopPrice * 1.5) || 100;
                const mult = state.marketMultipliers[id] || 1;
                const sellPrice = Math.floor(basePrice * mult);
                totalValue += sellPrice * qty;
                totalItems += qty;
                state.inventory.products[id] = 0;
            });"""
content = content.replace(old_sellAll, new_sellAll)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

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
                    if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-green-600'; }
                    else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-red-500'; }

                    return `
                    <div class="glass p-3 rounded-xl flex justify-between items-center">
                        <div class="flex items-center gap-3">
                            <span class="text-3xl bg-white/50 p-2 rounded-lg shadow-sm">${prod.emoji}</span>
                            <div>
                                <div class="font-bold text-gray-800">${prod.name} <span class="text-green-600 ml-1">x${qty}</span></div>
                                <div class="text-[10px] font-semibold text-gray-500 flex items-center gap-1">
                                    ราคา: ${sellPrice} 🪙 <span class="${trendColor}">${trendIcon}</span>
                                </div>
                            </div>
                        </div>
                        <button onclick="openSellModal('${id}')" class="relative group glass-btn px-4 py-2 bg-yellow-50 rounded-xl text-sm font-bold text-amber-700 shadow-sm border border-yellow-200">
                            ขาย (+${totalValue})
                            <div class="absolute bottom-full mb-2 right-0 bg-gray-900/90 text-white text-xs px-2 py-1.5 rounded opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap z-50 font-normal">
                                <span class="text-amber-300 font-bold">คลิก</span> เพื่อขายทีละชิ้น<br>
                                <span class="text-blue-300 font-bold">กดค้าง</span> เพื่อระบุจำนวน
                            </div>
                        </button>
                    </div>
                    `;
                }).join('');
            }"""

new_inv = """            const prodEntries = Object.entries(state.inventory.products).filter(([_, qty]) => qty > 0);
            if (prodEntries.length === 0) {
                document.getElementById('inv-products').innerHTML = '<div class="text-sm text-gray-500 text-center py-8 bg-white/30 rounded-xl">ยังไม่มีผลผลิต<br/><span class="text-xs">ปลูกผัก, เลี้ยงสัตว์ หรือทำอาหารเพื่อนำมาขาย</span></div>';
            } else {
                let cropHtml = '<h4 class="text-xs font-bold text-gray-500 mb-2 mt-2 border-b border-gray-200 pb-1">🌾 พืชผล</h4>';
                let animalHtml = '<h4 class="text-xs font-bold text-gray-500 mb-2 mt-4 border-b border-gray-200 pb-1">🐾 ผลผลิตจากสัตว์</h4>';
                let foodHtml = '<h4 class="text-xs font-bold text-gray-500 mb-2 mt-4 border-b border-gray-200 pb-1">🍳 อาหาร</h4>';
                
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
                    if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-green-600'; }
                    else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-red-500'; }

                    return `
                    <div class="glass p-3 rounded-xl flex justify-between items-center mb-2">
                        <div class="flex items-center gap-3">
                            <span class="text-3xl bg-white/50 p-2 rounded-lg shadow-sm">${prod.emoji}</span>
                            <div>
                                <div class="font-bold text-gray-800">${prod.name} <span class="text-green-600 ml-1">x${qty}</span></div>
                                <div class="text-[10px] font-semibold text-gray-500 flex items-center gap-1">
                                    ราคา: ${sellPrice} 🪙 <span class="${trendColor}">${trendIcon}</span>
                                </div>
                            </div>
                        </div>
                        <button onclick="openSellModal('${id}')" class="relative group glass-btn px-4 py-2 bg-yellow-50 rounded-xl text-sm font-bold text-amber-700 shadow-sm border border-yellow-200">
                            ขาย (+${totalValue})
                        </button>
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

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

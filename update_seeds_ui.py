import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_seed_render = """                document.getElementById('inv-seeds').innerHTML = seedEntries.map(([id, qty]) => {
                    const seed = SEEDS[id];
                    return `
                    <div class="glass p-3 rounded-xl flex items-center gap-3">
                        <span class="text-3xl">${seed.emoji}</span>
                        <div class="flex-1">
                            <div class="font-bold text-sm text-gray-800">${seed.name}</div>
                            <div class="text-xs font-bold text-green-600">x${qty}</div>
                        </div>
                    </div>
                    `;
                }).join('');"""

new_seed_render = """                document.getElementById('inv-seeds').innerHTML = seedEntries.map(([id, qty]) => {
                    const seed = SEEDS[id];
                    const sellPrice = Math.floor(seed.buyPrice * 0.5);
                    return `
                    <div class="glass p-3 rounded-xl flex items-center justify-between gap-2">
                        <div class="flex items-center gap-2">
                            <span class="text-3xl">${seed.emoji}</span>
                            <div class="flex-1">
                                <div class="font-bold text-sm text-gray-800">${seed.name}</div>
                                <div class="text-xs font-bold text-green-600">x${qty}</div>
                            </div>
                        </div>
                        <button onclick="sellSeed('${id}')" class="text-xs bg-red-50 text-red-600 hover:bg-red-100 font-bold px-2 py-1 rounded-lg transition shadow-sm border border-red-200 whitespace-nowrap">
                            ขาย (-50%)
                        </button>
                    </div>
                    `;
                }).join('');"""

content = content.replace(old_seed_render, new_seed_render)

sell_seed_func = """
        function sellSeed(id) {
            const qty = state.inventory.seeds[id] || 0;
            if (qty > 0) {
                const seed = SEEDS[id];
                const totalValue = Math.floor(seed.buyPrice * 0.5) * qty;
                state.gold += totalValue;
                state.inventory.seeds[id] = 0;
                
                updateUI();
                showAlert('ขายเมล็ดพันธุ์สำเร็จ!', `ขายเมล็ด ${seed.name} ${qty} ถุง ได้รับเงิน ${totalValue} 🪙`, '💰');
                if (typeof fireConfetti === 'function') fireConfetti();
            }
        }
"""

content = content.replace("        function sellAllInventory() {", sell_seed_func + "\n        function sellAllInventory() {")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

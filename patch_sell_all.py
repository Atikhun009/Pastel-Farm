import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the inventory products header
old_inv_header = r"<h3 class=\"text-sm font-bold text-green-900/60 mb-3 uppercase tracking-wider flex items-center gap-1\">\s*<span>🧺</span> ผลผลิต \(ขายตามราคาตลาด\)\s*</h3>"
new_inv_header = """<div class="flex justify-between items-center mb-3">
                                <h3 class="text-sm font-bold text-green-900/60 uppercase tracking-wider flex items-center gap-1">
                                    <span>🧺</span> ผลผลิต
                                </h3>
                                <button onclick="sellAllInventory()" class="text-xs bg-red-50 text-red-600 hover:bg-red-100 font-bold px-3 py-1.5 rounded-lg transition shadow-sm border border-red-200">
                                    ⚡ ขายทั้งหมด (-5%)
                                </button>
                            </div>"""
content = re.sub(old_inv_header, new_inv_header, content)

# Add sellAllInventory function
sell_all_script = """        function sellAllInventory() {
            const prodEntries = Object.entries(state.inventory.products).filter(([_, qty]) => qty > 0);
            if (prodEntries.length === 0) {
                showAlert('ไม่มีผลผลิต', 'คุณยังไม่มีผลผลิตให้ขายเลย', '🤷');
                return;
            }

            let totalValue = 0;
            let totalItems = 0;

            prodEntries.forEach(([id, qty]) => {
                const prod = PRODUCTS[id];
                const mult = state.marketMultipliers[id] || 1;
                const sellPrice = Math.floor(prod.basePrice * mult);
                totalValue += sellPrice * qty;
                totalItems += qty;
                state.inventory.products[id] = 0;
            });

            const finalValue = Math.floor(totalValue * 0.95);
            state.gold += finalValue;
            
            updateUI();
            showAlert('ขายทั้งหมดสำเร็จ!', `ขายผลผลิต ${totalItems} ชิ้น ได้รับเงิน ${finalValue} 🪙\\n(มูลค่าเดิม ${totalValue} หักค่าธรรมเนียม 5%)`, '💰');
            if (typeof fireConfetti === 'function') fireConfetti();
        }
"""
# Insert before updateUI function
update_ui_idx = content.find("function updateUI()")
content = content[:update_ui_idx] + sell_all_script + "\n" + content[update_ui_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


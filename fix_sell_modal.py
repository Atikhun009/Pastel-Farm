import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix openSellModal
old_open_sell = """        function openSellModal(productId) {
            const qty = state.inventory.products[productId] || 0;
            if (qty <= 0) return;

            const prod = PRODUCTS[productId];
            const mult = state.marketMultipliers[productId] || 1;
            const sellPrice = Math.floor(prod.basePrice * mult);"""

new_open_sell = """        function openSellModal(productId) {
            const qty = state.inventory.products[productId] || 0;
            if (qty <= 0) return;

            const prod = PRODUCTS[productId] || RECIPES[productId];
            const mult = state.marketMultipliers[productId] || 1;
            const basePrice = prod.basePrice || (prod.shopPrice ? prod.shopPrice * 1.5 : 100);
            const sellPrice = Math.floor(basePrice * mult);"""

content = content.replace(old_open_sell, new_open_sell)

# Fix executeSell
old_exec_sell = """            if (qty > 0) {
                const prod = PRODUCTS[productId];
                const mult = state.marketMultipliers[productId] || 1;
                let sellPrice = Math.floor(prod.basePrice * mult);
                let multiplierBonus = 1.0;"""

new_exec_sell = """            if (qty > 0) {
                const prod = PRODUCTS[productId] || RECIPES[productId];
                const mult = state.marketMultipliers[productId] || 1;
                const basePrice = prod.basePrice || (prod.shopPrice ? prod.shopPrice * 1.5 : 100);
                let sellPrice = Math.floor(basePrice * mult);
                let multiplierBonus = 1.0;"""

content = content.replace(old_exec_sell, new_exec_sell)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

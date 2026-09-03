import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_render = """                document.getElementById('inv-products').innerHTML = prodEntries.map(([id, qty]) => {
                    const prod = PRODUCTS[id];
                    const mult = state.marketMultipliers[id] || 1;
                    const sellPrice = Math.floor(prod.basePrice * mult);
                    const totalValue = sellPrice * qty;"""

new_render = """                document.getElementById('inv-products').innerHTML = prodEntries.map(([id, qty]) => {
                    const prod = PRODUCTS[id] || RECIPES[id];
                    const mult = state.marketMultipliers[id] || 1;
                    const basePrice = prod.basePrice || (prod.shopPrice ? prod.shopPrice * 1.5 : 100);
                    const sellPrice = Math.floor(basePrice * mult);
                    const totalValue = sellPrice * qty;"""

content = content.replace(old_render, new_render)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

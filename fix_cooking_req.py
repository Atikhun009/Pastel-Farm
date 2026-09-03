import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_req = """                const reqHtml = Object.entries(recipe.req).map(([reqId, reqQty]) => {
                    const hasQty = state.inventory.products[reqId] || 0;
                    if (hasQty < reqQty) canCook = false;
                    const pItem = PRODUCTS[reqId];
                    return `<span class="inline-flex items-center gap-1 bg-white/50 px-2 py-0.5 rounded text-[10px] ${hasQty >= reqQty ? 'text-green-700' : 'text-red-600 font-bold'}">
                        ${pItem.emoji} ${hasQty}/${reqQty}
                    </span>`;
                }).join(' ');"""

new_req = """                const reqHtml = Object.entries(recipe.req).map(([reqId, reqQty]) => {
                    const hasQty = state.inventory.products[reqId] || 0;
                    if (hasQty < reqQty) canCook = false;
                    const pItem = PRODUCTS[reqId] || RECIPES[reqId];
                    return `<span class="inline-flex items-center gap-1 bg-white/50 px-2 py-0.5 rounded text-[10px] ${hasQty >= reqQty ? 'text-green-700' : 'text-red-600 font-bold'}">
                        ${pItem ? pItem.emoji : '❓'} ${hasQty}/${reqQty}
                    </span>`;
                }).join(' ');"""

content = content.replace(old_req, new_req)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

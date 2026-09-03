import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update setQuickBuy
old_set_qb = """        function setQuickBuy(amt) {
            quickBuyAmount = amt;
            if(!document.getElementById('qb-1')) return;
            document.getElementById('qb-1').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickBuyAmount === 1 ? 'bg-green-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            document.getElementById('qb-10').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickBuyAmount === 10 ? 'bg-green-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            document.getElementById('qb-100').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickBuyAmount === 100 ? 'bg-green-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            renderMarket();
        }"""
new_set_qb = """        let quickCookAmount = 1;

        function setQuickCook(amt) {
            quickCookAmount = amt;
            if(!document.getElementById('qc-1')) return;
            document.getElementById('qc-1').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickCookAmount === 1 ? 'bg-blue-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            document.getElementById('qc-10').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickCookAmount === 10 ? 'bg-blue-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            document.getElementById('qc-100').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickCookAmount === 100 ? 'bg-blue-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            document.getElementById('qc-1000').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickCookAmount === 1000 ? 'bg-blue-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            renderCooking();
        }

        function setQuickBuy(amt) {
            quickBuyAmount = amt;
            if(!document.getElementById('qb-1')) return;
            document.getElementById('qb-1').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickBuyAmount === 1 ? 'bg-green-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            document.getElementById('qb-10').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickBuyAmount === 10 ? 'bg-green-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            document.getElementById('qb-100').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickBuyAmount === 100 ? 'bg-green-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            document.getElementById('qb-1000').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickBuyAmount === 1000 ? 'bg-green-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            renderMarket();
        }"""

if old_set_qb in content:
    content = content.replace(old_set_qb, new_set_qb)
    print("setQuickBuy updated")
else:
    print("setQuickBuy NOT FOUND")

# 2. Update renderCooking to use quickCookAmount instead of input
old_render_cooking = """                        <div class="flex items-center gap-2">
                            <input type="number" id="qty-${recipe.id}" value="1" min="1" class="w-16 rounded-xl border-gray-300 shadow-sm px-2 py-2 text-sm text-center" ${isLocked || !canCook ? 'disabled' : ''}>
                            <button onclick="cookRecipe('${recipe.id}')" class="glass-btn px-4 py-2.5 rounded-xl text-sm font-bold text-blue-700 shadow-sm whitespace-nowrap bg-blue-50/50" ${isLocked || !canCook ? 'disabled' : ''}>
                                ทำอาหาร
                            </button>
                        </div>"""
new_render_cooking = """                        <div class="flex items-center gap-2">
                            <button onclick="cookRecipe('${recipe.id}')" class="glass-btn px-4 py-2.5 rounded-xl text-sm font-bold text-blue-700 shadow-sm whitespace-nowrap bg-blue-50/50" ${isLocked || !canCook ? 'disabled' : ''}>
                                <span class="text-[10px] text-blue-500 mr-1">x${quickCookAmount}</span>ทำอาหาร
                            </button>
                        </div>"""

if old_render_cooking in content:
    content = content.replace(old_render_cooking, new_render_cooking)
    print("renderCooking UI updated")
else:
    print("renderCooking UI NOT FOUND")

# 3. Update the reqHtml in renderCooking to reflect quickCookAmount multiplied
# We need to change:
# const hasQty = state.inventory.products[reqId] || 0;
# if (hasQty < reqQty) canCook = false;
# to:
# const hasQty = state.inventory.products[reqId] || 0;
# if (hasQty < reqQty * quickCookAmount) canCook = false;

old_req_check = """                let canCook = true;
                const reqHtml = Object.entries(recipe.req).map(([reqId, reqQty]) => {
                    const hasQty = state.inventory.products[reqId] || 0;
                    if (hasQty < reqQty) canCook = false;
                    const pItem = PRODUCTS[reqId] || RECIPES[reqId];
                    return `<span class="inline-flex items-center gap-1 bg-white/50 px-2 py-0.5 rounded text-[10px] ${hasQty >= reqQty ? 'text-green-700' : 'text-red-600 font-bold'}">
                        ${pItem ? pItem.emoji : '❓'} ${hasQty}/${reqQty}
                    </span>`;
                }).join(' ');"""

new_req_check = """                let canCook = true;
                const reqHtml = Object.entries(recipe.req).map(([reqId, reqQty]) => {
                    const hasQty = state.inventory.products[reqId] || 0;
                    const totalReq = reqQty * quickCookAmount;
                    if (hasQty < totalReq) canCook = false;
                    const pItem = PRODUCTS[reqId] || RECIPES[reqId];
                    return `<span class="inline-flex items-center gap-1 bg-white/50 px-2 py-0.5 rounded text-[10px] ${hasQty >= totalReq ? 'text-green-700' : 'text-red-600 font-bold'}">
                        ${pItem ? pItem.emoji : '❓'} ${hasQty}/${totalReq}
                    </span>`;
                }).join(' ');"""

if old_req_check in content:
    content = content.replace(old_req_check, new_req_check)
    print("renderCooking Logic updated")
else:
    print("renderCooking Logic NOT FOUND")

# 4. Update cookRecipe function to use quickCookAmount
old_cook_recipe = """        function cookRecipe(recipeId) {
            const recipe = RECIPES[recipeId];
            if (!recipe) return;
            const qtyInput = document.getElementById(`qty-${recipeId}`);
            const qty = parseInt(qtyInput ? qtyInput.value : 1) || 1;
            if (qty < 1) return;"""

new_cook_recipe = """        function cookRecipe(recipeId) {
            const recipe = RECIPES[recipeId];
            if (!recipe) return;
            const qty = quickCookAmount;
            if (qty < 1) return;"""

if old_cook_recipe in content:
    content = content.replace(old_cook_recipe, new_cook_recipe)
    print("cookRecipe updated")
else:
    print("cookRecipe NOT FOUND")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


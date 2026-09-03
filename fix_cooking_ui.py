import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_render_cooking = """        // Generate Cooking Content
        function renderCooking() {
            // Render Cooking Slots
            const slotsContainer = document.getElementById('cooking-slots-container');
            if (slotsContainer && state.cookingSlots) {
                slotsContainer.innerHTML = state.cookingSlots.map(slot => {
                    if (!slot.recipeId) {
                        return `<div class="glass p-4 rounded-xl flex items-center justify-center text-gray-400 border border-dashed border-gray-300 h-24">เตาว่าง</div>`;
                    }
                    const recipe = RECIPES[slot.recipeId];
                    const now = Date.now();
                    const progress = Math.min((now - slot.startTime) / slot.cookTime, 1);
                    const isDone = progress >= 1;
                    
                    return `
                    <div class="glass p-3 rounded-xl flex flex-col gap-2 relative overflow-hidden">
                        <div class="flex justify-between items-center z-10 relative">
                            <div class="flex items-center gap-2">
                                <span class="text-2xl">${recipe.emoji}</span>
                                <div>
                                    <div class="font-bold text-gray-800 text-sm">${recipe.name} x${slot.qty}</div>
                                    <div class="text-[10px] text-gray-500">${isDone ? 'เสร็จแล้ว!' : 'กำลังปรุง...'}</div>
                                </div>
                            </div>
                            ${isDone ? `<button onclick="collectFood(${slot.id})" class="text-xs font-bold bg-green-500 hover:bg-green-600 text-white px-3 py-1.5 rounded-lg shadow-sm transition animate-pulse">เก็บ</button>` : ''}
                        </div>
                        <div class="h-1.5 bg-gray-200 rounded-full overflow-hidden z-10 relative">
                            <div class="h-full bg-orange-400 transition-all duration-1000" style="width: ${progress * 100}%"></div>
                        </div>
                    </div>`;
                }).join('');
            }"""

new_render_cooking = """        // Generate Cooking Content
        function renderCooking() {
            // Cooking slots removed"""

if old_render_cooking in content:
    content = content.replace(old_render_cooking, new_render_cooking)
    print("Replaced renderCooking")
else:
    print("Could not find renderCooking")

# Let's remove the HTML for cooking slots if it exists. We might not need to if it doesn't exist, but it's safe to check.
old_cooking_html = """                    <div id="view-cooking" class="flex-1 overflow-y-auto pr-2 space-y-6 hidden">
                        <div class="bg-blue-50/80 rounded-xl p-3 mb-4 text-xs font-semibold text-blue-800 border border-blue-200">
                            👨‍🍳 นำผลผลิตมาทำอาหารเพื่อขายได้ราคาที่สูงกว่าและได้ XP เพิ่ม!
                        </div>
                        <div id="cooking-slots-container" class="grid grid-cols-1 md:grid-cols-3 gap-3 mb-6"></div>
                        <div id="cooking-recipes" class="space-y-3"></div>
                    </div>"""

new_cooking_html = """                    <div id="view-cooking" class="flex-1 overflow-y-auto pr-2 space-y-6 hidden">
                        <div class="bg-blue-50/80 rounded-xl p-3 mb-4 text-xs font-semibold text-blue-800 border border-blue-200">
                            👨‍🍳 นำผลผลิตมาทำอาหารได้อย่างรวดเร็วทันใจ ได้ทั้งราคาที่สูงขึ้นและ XP!
                        </div>
                        <div id="cooking-recipes" class="space-y-3"></div>
                    </div>"""

if "id=\"cooking-slots-container\"" in content:
    content = re.sub(r'<div id="cooking-slots-container".*?</div>\s*', '', content)
    print("Removed cooking-slots-container HTML")
    
# Remove state.cookingSlots initialization to clean up
old_init = """                    if (!state.cookingSlots) {
                        state.cookingSlots = [
                            { id: 0, recipeId: null, startTime: null, qty: 0, cookTime: 0 },
                            { id: 1, recipeId: null, startTime: null, qty: 0, cookTime: 0 },
                            { id: 2, recipeId: null, startTime: null, qty: 0, cookTime: 0 }
                        ];
                    }"""
content = content.replace(old_init, "")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


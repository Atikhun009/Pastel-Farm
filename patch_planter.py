import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add auto_planter to UPGRADES
content = re.sub(r"(const UPGRADES = \{)", r"\1\n            auto_planter: { id: 'auto_planter', name: 'หุ่นยนต์ปลูกผัก', emoji: '🌱', desc: 'ปลูกเมล็ดพันธุ์เดิมอัตโนมัติ (ถ้ามี)', buyPrice: 4000, maxLevel: 1, priceMult: 1, type: 'feature' },", content)

# 2. Add UI for Planter button next to Harvester button
old_buttons = """<div class="flex items-center gap-3">
                            <h2 class="text-xl font-bold text-green-900 flex items-center gap-2">
                                <span class="text-2xl">🌱</span> แปลงเพาะปลูก
                            </h2>
                            <button id="btn-toggle-auto" onclick="toggleAutoHarvester()" class="hidden text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600">
                                🤖 ออโต้: <span id="ui-auto-status" class="text-white">เปิด</span>
                            </button>
                        </div>"""
new_buttons = """<div class="flex items-center gap-2 flex-wrap">
                            <h2 class="text-xl font-bold text-green-900 flex items-center gap-1 mr-2">
                                <span class="text-2xl">🌱</span> แปลงเพาะปลูก
                            </h2>
                            <button id="btn-toggle-auto" onclick="toggleAutoHarvester()" class="hidden text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600">
                                🤖 เก็บเกี่ยว: <span id="ui-auto-status" class="text-white">เปิด</span>
                            </button>
                            <button id="btn-toggle-planter" onclick="toggleAutoPlanter()" class="hidden text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600">
                                🌱 ปลูกซ้ำ: <span id="ui-planter-status" class="text-white">เปิด</span>
                            </button>
                        </div>"""
content = content.replace(old_buttons, new_buttons)

# 3. Add toggleAutoPlanter script
toggle_planter_script = """        function toggleAutoPlanter() {
            state.autoPlanterActive = state.autoPlanterActive === false ? true : false;
            updateUI();
        }"""
content = content.replace("function toggleAutoHarvester() {", toggle_planter_script + "\n        function toggleAutoHarvester() {")

# 4. Add updateUI logic
update_planter_ui = """// Auto Planter Button
            const togglePlanterBtn = document.getElementById('btn-toggle-planter');
            if (togglePlanterBtn) {
                if (state.upgrades && state.upgrades.auto_planter) {
                    togglePlanterBtn.classList.remove('hidden');
                    const isActive = state.autoPlanterActive !== false;
                    document.getElementById('ui-planter-status').innerText = isActive ? 'เปิด' : 'ปิด';
                    document.getElementById('ui-planter-status').className = isActive ? 'text-white' : 'text-red-100';
                    togglePlanterBtn.className = isActive 
                        ? 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600'
                        : 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-red-400 text-white hover:bg-red-500';
                } else {
                    togglePlanterBtn.classList.add('hidden');
                }
            }
"""
content = content.replace("document.getElementById('ui-gold').innerText = state.gold;", update_planter_ui + "\n            document.getElementById('ui-gold').innerText = state.gold;")

# 5. Modify harvest() function
old_harvest_end = """showFloatingText(`plot-${plotId}`, `+${amount} ${PRODUCTS[product].emoji}${bonusStr}  +${seed.xp * amount} XP`, 'text-green-600');
                
                plot.seedId = null;
                plot.plantedAt = null;
                
                updateUI();"""

new_harvest_end = """showFloatingText(`plot-${plotId}`, `+${amount} ${PRODUCTS[product].emoji}${bonusStr}  +${seed.xp * amount} XP`, 'text-green-600');
                
                let replanted = false;
                if (state.autoPlanterActive !== false && state.upgrades && state.upgrades.auto_planter) {
                    if (state.inventory.seeds[plot.seedId] > 0) {
                        state.inventory.seeds[plot.seedId]--;
                        plot.plantedAt = Date.now();
                        replanted = true;
                        setTimeout(() => showFloatingText(`plot-${plotId}`, `🌱 ปลูกใหม่!`, 'text-green-500'), 500);
                    }
                }
                
                if (!replanted) {
                    plot.seedId = null;
                    plot.plantedAt = null;
                }
                
                updateUI();"""
content = content.replace(old_harvest_end, new_harvest_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


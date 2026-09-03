import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Level Gating the Tabs
old_tabs_menu = """        <nav class="glass-panel p-2 md:p-3 rounded-2xl relative z-10 w-full mb-6">
            <div class="flex gap-2 overflow-x-auto whitespace-nowrap hide-scroll">
                
                        <button id="tab-farm" onclick="switchTab('farm')" class="px-4 py-2.5 rounded-xl text-sm font-bold bg-white shadow-sm text-green-900 transition flex-1">
                            🚜 ฟาร์ม
                        </button>
                        <button id="tab-market" onclick="switchTab('market')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🛒 ร้านค้า
                        </button>
                        <button id="tab-inventory" onclick="switchTab('inventory')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🎒 กระเป๋า
                        </button>
                        <button id="tab-cooking" onclick="switchTab('cooking')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🍳 อาหาร
                        </button>
                        <button id="tab-quests" onclick="switchTab('quests')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            📜 ภารกิจ
                        </button>
                        <button id="tab-orders" onclick="switchTab('orders')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            📋 ส่งของ
                        </button>
                        
                        <button id="tab-achievements" onclick="switchTab('achievements')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🏆 ความสำเร็จ
                        </button>
            </div>
        </nav>"""
        
new_tabs_menu = """        <nav class="glass-panel p-2 md:p-3 rounded-2xl relative z-10 w-full mb-6">
            <div class="flex gap-2 overflow-x-auto whitespace-nowrap hide-scroll">
                
                        <button id="tab-farm" onclick="switchTab('farm')" class="px-4 py-2.5 rounded-xl text-sm font-bold bg-white shadow-sm text-green-900 transition flex-1">
                            🚜 ฟาร์ม
                        </button>
                        <button id="tab-market" onclick="switchTab('market')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🛒 ร้านค้า
                        </button>
                        <button id="tab-inventory" onclick="switchTab('inventory')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🎒 กระเป๋า
                        </button>
                        <button id="tab-cooking" onclick="switchTab('cooking')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🍳 อาหาร <span id="lock-cooking" class="text-xs text-red-500 hidden">Lv.3</span>
                        </button>
                        <button id="tab-quests" onclick="switchTab('quests')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            📜 ภารกิจ
                        </button>
                        <button id="tab-orders" onclick="switchTab('orders')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            📋 ส่งของ <span id="lock-orders" class="text-xs text-red-500 hidden">Lv.5</span>
                        </button>
                        
                        <button id="tab-achievements" onclick="switchTab('achievements')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🏆 ความสำเร็จ
                        </button>
            </div>
        </nav>"""
content = content.replace(old_tabs_menu, new_tabs_menu)

# Ensure switchTab logic checks level
old_switch = """        function switchTab(tabId) {
            const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements'];"""
            
new_switch = """        function switchTab(tabId) {
            if (tabId === 'cooking' && state.level < 3) {
                showAlert('ระดับไม่ถึง', 'เมนูอาหารจะปลดล็อกเมื่อเลเวล 3', '🔒');
                return;
            }
            if (tabId === 'orders' && state.level < 5) {
                showAlert('ระดับไม่ถึง', 'เมนูส่งของจะปลดล็อกเมื่อเลเวล 5', '🔒');
                return;
            }
            const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements'];"""
content = content.replace(old_switch, new_switch)

# Add level check UI updates
# in updateUI()
old_level_ui = "document.getElementById('ui-level').innerText = state.level;"
new_level_ui = """document.getElementById('ui-level').innerText = state.level;
            const lockC = document.getElementById('lock-cooking');
            const lockO = document.getElementById('lock-orders');
            if (lockC) { if (state.level >= 3) lockC.classList.add('hidden'); else lockC.classList.remove('hidden'); }
            if (lockO) { if (state.level >= 5) lockO.classList.add('hidden'); else lockO.classList.remove('hidden'); }"""
content = content.replace(old_level_ui, new_level_ui)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

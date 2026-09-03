import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add nav button
nav_old = """                        <button id="tab-orders" onclick="switchTab('orders')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            📋 ส่งของ
                        </button>"""
nav_new = """                        <button id="tab-orders" onclick="switchTab('orders')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            📋 ส่งของ
                        </button>
                        <button id="tab-redeem" onclick="switchTab('redeem')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🎟️ โค้ด
                        </button>"""
content = content.replace(nav_old, nav_new)

# 2. Add view-redeem
view_orders = """                    <div id="view-orders" class="flex-1 overflow-y-auto pr-2 space-y-6 hidden">"""
view_redeem = """                    <div id="view-redeem" class="flex-1 overflow-y-auto pr-2 space-y-6 hidden">
                        <div class="bg-blue-50/80 rounded-xl p-3 mb-4 text-xs font-semibold text-blue-800 border border-blue-200">
                            🎟️ กรอกโค้ดลับเพื่อรับของรางวัลพิเศษ!
                        </div>
                        <div class="glass p-4 rounded-2xl">
                            <input type="text" id="redeem-code-input" placeholder="ใส่โค้ดที่นี่ (เช่น PASTELFARM2025)" class="w-full mb-3 px-4 py-2 rounded-xl bg-white/50 border border-white/50 focus:outline-none focus:ring-2 focus:ring-green-400 font-bold text-center text-gray-700 uppercase">
                            <button onclick="redeemCode()" class="w-full bg-green-500 hover:bg-green-600 text-white font-bold py-3 rounded-xl shadow-md transition transform hover:scale-105">
                                รับรางวัล
                            </button>
                        </div>
                    </div>
                    <div id="view-orders" class="flex-1 overflow-y-auto pr-2 space-y-6 hidden">"""
content = content.replace(view_orders, view_redeem)

# 3. Add to switchTab
switchTab_old = """const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements'];"""
switchTab_new = """const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements', 'redeem'];"""
content = content.replace(switchTab_old, switchTab_new)

# 4. Add reset coupon UI
barn_buttons_old = """                                    <button onclick="sellAllInventory()" class="text-xs bg-red-50 text-red-600 hover:bg-red-100 font-bold px-3 py-1.5 rounded-xl transition shadow-sm border border-red-200 flex-none text-center">
                                        ⚡ ขายหมด (-5%)
                                    </button>"""
barn_buttons_new = """                                    <button onclick="sellAllInventory()" class="text-xs bg-red-50 text-red-600 hover:bg-red-100 font-bold px-3 py-1.5 rounded-xl transition shadow-sm border border-red-200 flex-none text-center">
                                        ⚡ ขายหมด (-5%)
                                    </button>
                                    <button id="ui-barn-reset-btn" onclick="useBarnResetCoupon()" class="text-xs bg-purple-50 text-purple-600 hover:bg-purple-100 font-bold px-3 py-1.5 rounded-xl transition shadow-sm border border-purple-200 flex-none text-center hidden">
                                        🎫 ล้างโรงนา (0)
                                    </button>"""
content = content.replace(barn_buttons_old, barn_buttons_new)

# 5. Add UI logic in renderInventory
render_inv_old = """                if (percent >= 90) {
                    uiBarnFill.className = "h-full bg-red-500 transition-all duration-300";
                    uiBarnCur.className = "text-red-600 font-black animate-pulse";
                } else if (percent >= 70) {
                    uiBarnFill.className = "h-full bg-orange-400 transition-all duration-300";
                    uiBarnCur.className = "text-orange-600 font-bold";
                } else {
                    uiBarnFill.className = "h-full bg-green-500 transition-all duration-300";
                    uiBarnCur.className = "";
                }
            }"""
render_inv_new = """                if (percent >= 90) {
                    uiBarnFill.className = "h-full bg-red-500 transition-all duration-300";
                    uiBarnCur.className = "text-red-600 font-black animate-pulse";
                } else if (percent >= 70) {
                    uiBarnFill.className = "h-full bg-orange-400 transition-all duration-300";
                    uiBarnCur.className = "text-orange-600 font-bold";
                } else {
                    uiBarnFill.className = "h-full bg-green-500 transition-all duration-300";
                    uiBarnCur.className = "";
                }
                
                const uiBarnResetBtn = document.getElementById('ui-barn-reset-btn');
                if (uiBarnResetBtn) {
                    if (state.inventory.barnResetCoupons > 0) {
                        uiBarnResetBtn.classList.remove('hidden');
                        uiBarnResetBtn.innerText = `🎫 ล้างโรงนา (${state.inventory.barnResetCoupons})`;
                    } else {
                        uiBarnResetBtn.classList.add('hidden');
                    }
                }
            }"""
content = content.replace(render_inv_old, render_inv_new)

# 6. Add fallbacks
load_game_old = """                    // Fallbacks for new features
                    if (!state.inventory) state.inventory = {};"""
load_game_new = """                    // Fallbacks for new features
                    if (!state.redeemedCodes) state.redeemedCodes = [];
                    if (!state.activeBuffs) state.activeBuffs = { cropSpeedEnd: 0, goldMultEnd: 0 };
                    if (!state.inventory) state.inventory = {};
                    if (state.inventory.barnResetCoupons === undefined) state.inventory.barnResetCoupons = 0;"""
content = content.replace(load_game_old, load_game_new)

# 7. Add redeem functions
funcs = """
        function redeemCode() {
            const inputEl = document.getElementById('redeem-code-input');
            if (!inputEl) return;
            const code = inputEl.value.trim().toUpperCase();
            
            if (!code) return;
            
            if (!state.redeemedCodes) state.redeemedCodes = [];
            if (!state.activeBuffs) state.activeBuffs = { cropSpeedEnd: 0, goldMultEnd: 0 };
            
            if (state.redeemedCodes.includes(code)) {
                showAlert('ใช้โค้ดไปแล้ว', 'คุณได้ใช้งานโค้ดนี้ไปแล้วนะ!', '🚫');
                return;
            }
            
            if (code === 'PASTELFARM2025') {
                state.gold += 2000000;
                state.inventory.barnResetCoupons = (state.inventory.barnResetCoupons || 0) + 2;
                
                state.activeBuffs.cropSpeedEnd = Math.max(state.activeBuffs.cropSpeedEnd || 0, Date.now()) + 60000; // 1 min
                state.activeBuffs.goldMultEnd = Math.max(state.activeBuffs.goldMultEnd || 0, Date.now()) + 120000; // 2 mins
                
                state.redeemedCodes.push(code);
                
                updateUI();
                inputEl.value = '';
                showAlert('รับรางวัลสำเร็จ!', 'ได้รับเงิน 2,000,000 🪙\\nคูปองล้างโรงนา x2\\nพืชโตไว 2x (1 นาที)\\nเงินขาย 1.5x (2 นาที)', '🎉');
                if (typeof fireConfetti === 'function') fireConfetti();
                return;
            }
            
            showAlert('โค้ดไม่ถูกต้อง', 'โค้ดนี้ไม่มีอยู่จริง หรือหมดอายุไปแล้ว', '❌');
        }
        
        function useBarnResetCoupon() {
            if (state.inventory.barnResetCoupons > 0) {
                state.inventory.products = {};
                state.inventory.seeds = {};
                state.inventory.fertilizer = 0;
                state.inventory.barnResetCoupons -= 1;
                updateUI();
                showAlert('ล้างโรงนาสำเร็จ!', 'โรงนาของคุณถูกลบของทั้งหมดกลายเป็น 0 แล้ว มีพื้นที่ว่างเหลือเฟือ!', '🎫');
            } else {
                showAlert('ไม่มีคูปอง', 'คุณไม่มีคูปองล้างโรงนา', '🚫');
            }
        }
"""
# insert before updateGameLoop
update_loop_regex = r'function updateGameLoop\(\) \{'
content = re.sub(update_loop_regex, funcs + '\n        function updateGameLoop() {', content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


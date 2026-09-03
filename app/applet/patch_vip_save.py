import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Save Manager Modal before </body>
save_modal = """
    <!-- Save Manager Modal -->
    <div id="save-manager-modal" class="fixed inset-0 bg-black/60 z-50 hidden flex items-center justify-center p-4 backdrop-blur-sm">
        <div class="bg-white rounded-3xl w-full max-w-md p-6 shadow-2xl">
            <h3 class="text-xl font-bold text-gray-800 mb-4 text-center">💾 จัดการข้อมูลเซฟ</h3>
            <p class="text-sm text-gray-600 mb-4 text-center">นำออก (Export) เซฟไปเล่นเครื่องอื่น หรือ นำเข้า (Import) เซฟเดิมกลับมา</p>
            
            <div class="space-y-3">
                <button onclick="exportSave()" class="w-full py-3 bg-blue-500 hover:bg-blue-600 text-white rounded-xl font-bold transition shadow-md">📤 นำออกเซฟ (Export JSON)</button>
                <div class="relative">
                    <input type="file" id="import-save-input" accept=".json" class="hidden" onchange="importSave(event)">
                    <label for="import-save-input" class="block w-full py-3 bg-green-500 hover:bg-green-600 text-white rounded-xl font-bold transition text-center cursor-pointer shadow-md">📥 นำเข้าเซฟ (Import JSON)</label>
                </div>
                
                <button onclick="closeSaveManager()" class="w-full py-3 bg-gray-200 hover:bg-gray-300 text-gray-700 rounded-xl font-bold transition mt-4">ปิดหน้าต่าง</button>
            </div>
        </div>
    </div>
    <div id="toast-container" """

content = content.replace('<div id="toast-container"', save_modal)

# 2. Add Save button to header
header_btn_old = """                <button onclick="toggleBGM()" id="btn-play-music" class="flex items-center gap-2 bg-white/60 hover:bg-white/80 transition-colors px-4 py-3 rounded-2xl border border-white shadow-sm">
                    <span id="bgm-icon" class="text-xl">🔇</span>
                    <span id="bgm-text" class="text-sm font-bold text-gray-700">เปิดเพลง (เศร้าๆ ซึมๆ อ่านหนังสือ)</span>
                </button>"""

header_btn_new = """                <button onclick="toggleBGM()" id="btn-play-music" class="flex items-center gap-2 bg-white/60 hover:bg-white/80 transition-colors px-4 py-3 rounded-2xl border border-white shadow-sm">
                    <span id="bgm-icon" class="text-xl">🔇</span>
                    <span id="bgm-text" class="text-sm font-bold text-gray-700 hidden md:inline">เปิดเพลง</span>
                </button>
                <button onclick="openSaveManager()" class="flex items-center gap-2 bg-white/60 hover:bg-white/80 transition-colors px-4 py-3 rounded-2xl border border-white shadow-sm" title="จัดการเซฟ">
                    <span class="text-xl">💾</span>
                    <span class="text-sm font-bold text-gray-700 hidden md:inline">เซฟ</span>
                </button>"""

content = content.replace(header_btn_old, header_btn_new)


# 3. Add Level 100 Coupon button to inventory
inv_btn_old = """                                    <button id="ui-barn-reset-btn" onclick="useBarnResetCoupon()" class="text-xs bg-purple-50 text-purple-600 hover:bg-purple-100 font-bold px-3 py-1.5 rounded-xl transition shadow-sm border border-purple-200 flex-none text-center hidden">
                                        🎫 ล้างโรงนา (0)
                                    </button>"""

inv_btn_new = """                                    <button id="ui-barn-reset-btn" onclick="useBarnResetCoupon()" class="text-xs bg-purple-50 text-purple-600 hover:bg-purple-100 font-bold px-3 py-1.5 rounded-xl transition shadow-sm border border-purple-200 flex-none text-center hidden">
                                        🎫 ล้างโรงนา (0)
                                    </button>
                                    <button id="ui-lvl100-btn" onclick="useLevel100Coupon()" class="text-xs bg-yellow-50 text-yellow-600 hover:bg-yellow-100 font-bold px-3 py-1.5 rounded-xl transition shadow-sm border border-yellow-200 flex-none text-center hidden">
                                        🎟️ อัปเลเวล 100
                                    </button>"""

content = content.replace(inv_btn_old, inv_btn_new)

# 4. Add logic for updating the level 100 button in updateUI
update_ui_old = """                const uiBarnResetBtn = document.getElementById('ui-barn-reset-btn');
                if (uiBarnResetBtn) {
                    if (state.inventory.barnResetCoupons > 0) {
                        uiBarnResetBtn.classList.remove('hidden');
                        uiBarnResetBtn.innerText = `🎫 ล้างโรงนา (${state.inventory.barnResetCoupons})`;
                    } else {
                        uiBarnResetBtn.classList.add('hidden');
                    }
                }"""

update_ui_new = """                const uiBarnResetBtn = document.getElementById('ui-barn-reset-btn');
                if (uiBarnResetBtn) {
                    if (state.inventory.barnResetCoupons > 0) {
                        uiBarnResetBtn.classList.remove('hidden');
                        uiBarnResetBtn.innerText = `🎫 ล้างโรงนา (${state.inventory.barnResetCoupons})`;
                    } else {
                        uiBarnResetBtn.classList.add('hidden');
                    }
                }
                const uiLvl100Btn = document.getElementById('ui-lvl100-btn');
                if (uiLvl100Btn) {
                    if ((state.inventory.level100Coupons || 0) > 0) {
                        uiLvl100Btn.classList.remove('hidden');
                        uiLvl100Btn.innerText = `🎟️ อัปเลเวล 100 (${state.inventory.level100Coupons})`;
                    } else {
                        uiLvl100Btn.classList.add('hidden');
                    }
                }"""

content = content.replace(update_ui_old, update_ui_new)

# 5. Add Redeem code LEVELUPVIP
redeem_code_logic = """            if (code === 'WELCOMEBUFF') {"""

redeem_code_new = """            if (code === 'LEVELUPVIP') {
                state.gold += 50000000;
                state.diamonds = (state.diamonds || 0) + 8000;
                state.inventory.barnFreeUpgradeCoupons = (state.inventory.barnFreeUpgradeCoupons || 0) + 5;
                state.inventory.level100Coupons = (state.inventory.level100Coupons || 0) + 1;
                
                state.redeemedCodes.push(code);
                
                updateUI();
                inputEl.value = '';
                showAlert('รับรางวัล VIP สำเร็จ!', 'ได้รับเงิน 50,000,000 🪙\\nเพชร 8,000 💎\\nคูปองอัปเกรดโรงนาฟรี x5\\nคูปองเลื่อนเลเวล 100 ฟรี x1', '🎉');
                if (typeof fireConfetti === 'function') fireConfetti();
                return;
            }
            
            if (code === 'WELCOMEBUFF') {"""

content = content.replace(redeem_code_logic, redeem_code_new)

# 6. Add JS Functions
js_funcs = """        function useBarnResetCoupon() {
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
        }"""

js_funcs_new = js_funcs + """
        
        function useLevel100Coupon() {
            if ((state.inventory.level100Coupons || 0) > 0) {
                if (state.level >= 100) {
                    showAlert('ใช้ไม่ได้', 'เลเวลของคุณถึง 100 หรือมากกว่าแล้ว', '🚫');
                    return;
                }
                state.inventory.level100Coupons -= 1;
                state.level = 100;
                state.xp = 0; // Reset XP for new level
                
                updateUI();
                saveGame();
                showAlert('อัปเลเวลสำเร็จ!', 'คุณถูกเลื่อนขึ้นสู่เลเวล 100 แล้ว!', '🎉');
                if (typeof fireConfetti === 'function') fireConfetti();
            }
        }

        function openSaveManager() {
            document.getElementById('save-manager-modal').classList.remove('hidden');
        }

        function closeSaveManager() {
            document.getElementById('save-manager-modal').classList.add('hidden');
        }

        function exportSave() {
            const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(state));
            const dlAnchorElem = document.createElement('a');
            dlAnchorElem.setAttribute("href", dataStr);
            dlAnchorElem.setAttribute("download", `farm_save_${Date.now()}.json`);
            document.body.appendChild(dlAnchorElem);
            dlAnchorElem.click();
            document.body.removeChild(dlAnchorElem);
            showAlert('นำออกสำเร็จ', 'บันทึกไฟล์เซฟ .json ลงเครื่องของคุณแล้ว', '💾');
        }

        function importSave(event) {
            const file = event.target.files[0];
            if (!file) return;
            
            const reader = new FileReader();
            reader.onload = function(e) {
                try {
                    const importedState = JSON.parse(e.target.result);
                    if (importedState && typeof importedState === 'object') {
                        state = { ...state, ...importedState };
                        
                        // Handle backward compatibility
                        if (!state.redeemedCodes) state.redeemedCodes = [];
                        if (!state.activeBuffs) state.activeBuffs = { cropSpeedEnd: 0, goldMultEnd: 0 };
                        if (!state.inventory) state.inventory = {};
                        if (state.inventory.barnResetCoupons === undefined) state.inventory.barnResetCoupons = 0;
                        if (!state.inventory.unlockedRecipes) state.inventory.unlockedRecipes = ['fried_egg', 'bread', 'carrot_soup', 'corn_soup', 'cake', 'pizza', 'fries', 'salad'];
                        if (!state.achievements) state.achievements = { harvest_count: 0, earn_gold_total: 0, cook_count: 0, claimed: [] };
                        if (!state.achievements.claimed) state.achievements.claimed = [];
                        if (!state.inventory.fertilizer) state.inventory.fertilizer = 0;
                        if (!state.inventory.barnSubmissions) state.inventory.barnSubmissions = {};
                        if (!state.claimedQuests) state.claimedQuests = [];
                        if (!state.upgrades) state.upgrades = {};
                        if (!state.decorations) state.decorations = [];
                        if (!state.npcOrders) state.npcOrders = [];
                        if (!state.season) { state.season = 'spring'; state.seasonStartTime = Date.now(); }

                        saveGame();
                        updateUI();
                        closeSaveManager();
                        showAlert('นำเข้าสำเร็จ', 'โหลดเซฟจากไฟล์เรียบร้อยแล้ว!', '🎉');
                    } else {
                        throw new Error('Invalid save data');
                    }
                } catch (err) {
                    console.error(err);
                    showAlert('เกิดข้อผิดพลาด', 'ไฟล์เซฟไม่ถูกต้องหรือไม่สามารถอ่านได้', '❌');
                }
                event.target.value = ''; // Reset input
            };
            reader.readAsText(file);
        }
"""

content = content.replace(js_funcs, js_funcs_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")

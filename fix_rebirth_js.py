import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update switchTab
old_tabs = "const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements', 'redeem', 'diamond'];"
new_tabs = "const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements', 'redeem', 'diamond', 'rebirth'];"
content = content.replace(old_tabs, new_tabs)

old_btn = """                    if (t === 'diamond') {
                        btn.classList.add('hover:bg-white/70', 'text-blue-700');
                    } else {"""
new_btn = """                    if (t === 'diamond') {
                        btn.classList.add('hover:bg-white/70', 'text-blue-700');
                    } else if (t === 'rebirth') {
                        btn.classList.add('hover:bg-white/70', 'text-purple-700');
                    } else {"""
content = content.replace(old_btn, new_btn)

old_active = """                if (tabId === 'diamond') {
                    activeBtn.classList.add('bg-white', 'text-blue-900', 'shadow-sm');
                    activeBtn.classList.remove('hover:bg-white/70', 'text-blue-700');
                } else {"""
new_active = """                if (tabId === 'diamond') {
                    activeBtn.classList.add('bg-white', 'text-blue-900', 'shadow-sm');
                    activeBtn.classList.remove('hover:bg-white/70', 'text-blue-700');
                } else if (tabId === 'rebirth') {
                    activeBtn.classList.add('bg-white', 'text-purple-900', 'shadow-sm');
                    activeBtn.classList.remove('hover:bg-white/70', 'text-purple-700');
                } else {"""
content = content.replace(old_active, new_active)

# performRebirth function
perform_rebirth_func = """
        function performRebirth() {
            if (state.level < 500) {
                showAlert('เลเวลไม่ถึง!', 'คุณต้องมีเลเวล 500 ขึ้นไปจึงจะจุติได้', '⚠️');
                return;
            }
            
            // Increment rebirth
            state.rebirths = (state.rebirths || 0) + 1;
            
            // Grant rewards
            state.diamonds = (state.diamonds || 0) + 500;
            
            // Reset state
            state.gold = 0;
            state.level = 1;
            state.xp = 0;
            state.inventory = { products: {}, seeds: { potato: 3, onion: 1 }, fertilizer: 0, barnLevel: 1, barnSubmissions: {}, unlockedRecipes: ['fried_egg', 'bread', 'carrot_soup', 'corn_soup', 'cake', 'pizza', 'fries', 'salad'] };
            state.plots = [
                { id: 1, unlocked: true, seedId: null, plantedAt: null, watered: false, fertilized: false },
                { id: 2, unlocked: true, seedId: null, plantedAt: null, watered: false, fertilized: false },
                { id: 3, unlocked: false, seedId: null, plantedAt: null, watered: false, fertilized: false },
                { id: 4, unlocked: false, seedId: null, plantedAt: null, watered: false, fertilized: false },
                { id: 5, unlocked: false, seedId: null, plantedAt: null, watered: false, fertilized: false },
                { id: 6, unlocked: false, seedId: null, plantedAt: null, watered: false, fertilized: false },
                { id: 7, unlocked: false, seedId: null, plantedAt: null, watered: false, fertilized: false },
                { id: 8, unlocked: false, seedId: null, plantedAt: null, watered: false, fertilized: false }
            ];
            state.pens = [
                { id: 1, unlocked: true, animalId: null, lastCollected: null, happiness: 0 },
                { id: 2, unlocked: false, animalId: null, lastCollected: null, happiness: 0 },
                { id: 3, unlocked: false, animalId: null, lastCollected: null, happiness: 0 },
                { id: 4, unlocked: false, animalId: null, lastCollected: null, happiness: 0 }
            ];
            state.upgrades = {};
            state.claimedLevelRewards = 1;
            state.npcOrders = [];
            
            saveGame();
            switchTab('farm');
            updateUI();
            
            showAlert('🔥 จุติสำเร็จ!', `ยินดีต้อนรับสู่รอบจุติที่ ${state.rebirths}!\\nคุณได้รับ +100% โบนัสถาวร และ 500 💎`, '✨');
            if (typeof fireConfetti === 'function') fireConfetti();
        }
"""
content = content.replace("function switchTab(tabId) {", perform_rebirth_func + "\n        function switchTab(tabId) {")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

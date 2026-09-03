import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Quests UI
old_quests = """                    <!-- Quests Content -->
                    <div id="view-quests" class="flex-1 overflow-y-auto pr-2 space-y-6 hidden">
                        <div class="bg-purple-50/80 rounded-xl p-3 mb-4 text-xs font-semibold text-purple-800 border border-purple-200">
                            ⭐ ทำภารกิจให้สำเร็จเพื่อรับรางวัลเหรียญทองและค่าประสบการณ์พิเศษ
                        </div>
                        <div id="quests-list" class="space-y-3"></div>
                    </div>"""
new_quests = """                    <!-- Quests Content -->
                    <div id="view-quests" class="flex-1 overflow-y-auto pr-2 space-y-6 hidden">
                        <div class="bg-purple-50/80 rounded-xl p-3 mb-4 text-xs font-semibold text-purple-800 border border-purple-200">
                            ⭐ ทำภารกิจให้สำเร็จเพื่อรับรางวัลเหรียญทองและค่าประสบการณ์พิเศษ
                        </div>
                        
                        <!-- Seasonal Event Section -->
                        <div class="glass p-4 rounded-xl border-2 border-pink-200 mb-6 bg-pink-50/30">
                            <h3 class="text-lg font-bold text-pink-800 mb-2 flex items-center gap-2">
                                <span id="event-icon" class="text-2xl animate-bounce">🌸</span> อีเวนต์ประจำฤดูกาล
                            </h3>
                            <p class="text-xs text-pink-700 mb-4 font-semibold" id="event-desc">ทำภารกิจพิเศษในช่วงฤดูใบไม้ผลิเพื่อรับรางวัลมหาศาล!</p>
                            <div id="event-quests-list" class="space-y-3"></div>
                        </div>
                        
                        <h3 class="text-sm font-bold text-gray-500 uppercase tracking-wider mb-2">ภารกิจทั่วไป</h3>
                        <div id="quests-list" class="space-y-3"></div>
                    </div>"""
content = content.replace(old_quests, new_quests)

# 2. Add Event Quests logic
# Define EVENT_QUESTS
# Let's insert them right after QUESTS
old_quests_data = "        const QUESTS = ["
new_quests_data = """        const EVENT_QUESTS = {
            spring: [
                { id: 'eq_sp_1', name: 'เทศกาลดอกไม้ 🌸', desc: 'ปลูกและเก็บเกี่ยวแครอท 50 ชิ้น', action: 'harvest_carrot', reqAmt: 50, reward: { gold: 2000, xp: 1000 } },
                { id: 'eq_sp_2', name: 'งานเลี้ยงต้นฤดู', desc: 'ทำเมนูสลัดผัก 10 จาน', action: 'cook_salad', reqAmt: 10, reward: { gold: 3000, xp: 1500 } }
            ],
            summer: [
                { id: 'eq_su_1', name: 'ปาร์ตี้หน้าร้อน ☀️', desc: 'เก็บเกี่ยวข้าวโพด 50 ชิ้น', action: 'harvest_corn', reqAmt: 50, reward: { gold: 2500, xp: 1200 } },
                { id: 'eq_su_2', name: 'ดับกระหาย', desc: 'ขายมะเขือเทศ 100 ชิ้น', action: 'sell_tomato', reqAmt: 100, reward: { gold: 3500, xp: 1800 } }
            ],
            autumn: [
                { id: 'eq_au_1', name: 'ฤดูเก็บเกี่ยว 🍂', desc: 'เก็บเกี่ยวมันฝรั่ง 80 ชิ้น', action: 'harvest_potato', reqAmt: 80, reward: { gold: 4000, xp: 2000 } },
                { id: 'eq_au_2', name: 'อบอุ่นร่างกาย', desc: 'ทำซุปข้าวโพด 15 จาน', action: 'cook_corn_soup', reqAmt: 15, reward: { gold: 5000, xp: 2500 } }
            ],
            winter: [
                { id: 'eq_wi_1', name: 'ฝ่าลมหนาว ❄️', desc: 'เก็บเกี่ยวผลผลิตจากสัตว์ 50 ชิ้น', action: 'collect_animal', reqAmt: 50, reward: { gold: 4500, xp: 2500 } },
                { id: 'eq_wi_2', name: 'คริสต์มาส', desc: 'อบเค้ก 15 ก้อน', action: 'cook_cake', reqAmt: 15, reward: { gold: 6000, xp: 3000 } }
            ]
        };
        
        const QUESTS = ["""
content = content.replace(old_quests_data, new_quests_data)

# 3. Add to renderQuests
old_render_quests = """        function renderQuests() {
            let html = '';
            QUESTS.forEach(quest => {"""
new_render_quests = """        function renderQuests() {
            // Render Event Quests
            let evHtml = '';
            const curEvent = EVENT_QUESTS[state.season] || [];
            
            const eventIcon = document.getElementById('event-icon');
            const eventDesc = document.getElementById('event-desc');
            if(eventIcon) eventIcon.innerText = SEASON_ICONS[state.season].split(' ')[0];
            if(eventDesc) eventDesc.innerText = `ทำภารกิจพิเศษในช่วง${SEASON_ICONS[state.season]}เพื่อรับรางวัลมหาศาล!`;
            
            curEvent.forEach(quest => {
                const isClaimed = state.claimedQuests.includes(quest.id);
                const progress = state.stats[quest.action] || 0;
                const progressPercent = Math.min((progress / quest.reqAmt) * 100, 100);
                const isDone = progress >= quest.reqAmt;
                
                evHtml += `
                <div class="glass p-3 rounded-xl ${isClaimed ? 'opacity-50 grayscale' : 'hover:bg-white/60 transition'}">
                    <div class="flex justify-between items-center mb-2">
                        <div>
                            <div class="font-bold text-pink-900">${quest.name}</div>
                            <div class="text-xs text-pink-700">${quest.desc}</div>
                        </div>
                        <div class="text-right">
                            <div class="text-[10px] font-bold text-amber-600">${quest.reward.gold} 🪙</div>
                            <div class="text-[10px] font-bold text-green-600">${quest.reward.xp} XP</div>
                        </div>
                    </div>
                    <div class="flex items-center gap-2">
                        <div class="flex-1 h-2 bg-pink-100 rounded-full overflow-hidden shadow-inner border border-pink-200">
                            <div class="h-full ${isDone ? 'bg-pink-500' : 'bg-pink-400'} transition-all" style="width: ${progressPercent}%"></div>
                        </div>
                        <span class="text-[10px] font-bold ${isDone ? 'text-pink-600' : 'text-gray-500'} w-8 text-right">${Math.min(progress, quest.reqAmt)}/${quest.reqAmt}</span>
                    </div>
                    ${!isClaimed && isDone ? `<button onclick="claimQuest('${quest.id}')" class="w-full mt-2 bg-pink-500 hover:bg-pink-600 text-white font-bold text-xs py-1.5 rounded-lg shadow-sm transition">รับรางวัล!</button>` : ''}
                    ${isClaimed ? `<div class="w-full mt-2 bg-gray-100 text-gray-500 text-center font-bold text-xs py-1.5 rounded-lg">รับแล้ว ✔️</div>` : ''}
                </div>`;
            });
            document.getElementById('event-quests-list').innerHTML = evHtml;

            let html = '';
            QUESTS.forEach(quest => {"""
content = content.replace(old_render_quests, new_render_quests)

# Fix claimQuest to support event quests
old_claimQuest = """        function claimQuest(questId) {
            if (state.claimedQuests.includes(questId)) return;
            const quest = QUESTS.find(q => q.id === questId);"""
new_claimQuest = """        function claimQuest(questId) {
            if (state.claimedQuests.includes(questId)) return;
            
            let quest = QUESTS.find(q => q.id === questId);
            if (!quest) {
                // Check event quests
                for (let key in EVENT_QUESTS) {
                    const found = EVENT_QUESTS[key].find(q => q.id === questId);
                    if (found) quest = found;
                }
            }
            if (!quest) return;"""
content = content.replace(old_claimQuest, new_claimQuest)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I need to add state.activeDynamicQuests initialization to loadGame
fallback_old = "if (!state.gameTime) state.gameTime = { year: 1, seasonIndex: 0, day: 1, minute: 360 };"
fallback_new = """if (!state.gameTime) state.gameTime = { year: 1, seasonIndex: 0, day: 1, minute: 360 };
                    if (!state.activeDynamicQuests) state.activeDynamicQuests = [];"""
content = content.replace(fallback_old, fallback_new)

# Add quest generator and modifier
funcs = """
        function generateRandomQuest() {
            const possibleCrops = Object.keys(SEEDS).filter(k => SEEDS[k].unlockLevel <= state.level);
            const possibleAnimals = Object.keys(ANIMALS).filter(k => ANIMALS[k].unlockLevel <= state.level);
            
            const types = ['harvest', 'collect'];
            const type = types[Math.floor(Math.random() * types.length)];
            
            let id = 'dq_' + Date.now() + '_' + Math.floor(Math.random() * 1000);
            let action, reqAmt, rewardGold, rewardXp, name, desc;
            
            if (type === 'harvest' && possibleCrops.length > 0) {
                const target = possibleCrops[Math.floor(Math.random() * possibleCrops.length)];
                action = 'harvest_' + SEEDS[target].produces;
                reqAmt = Math.floor(Math.random() * 20) + 10;
                rewardGold = reqAmt * PRODUCTS[SEEDS[target].produces].basePrice * 2;
                rewardXp = reqAmt * SEEDS[target].xp * 2;
                name = `คำสั่งซื้อ: ${SEEDS[target].name}`;
                desc = `เก็บเกี่ยว ${SEEDS[target].name} จำนวน ${reqAmt} ชิ้น`;
            } else if (type === 'collect' && possibleAnimals.length > 0) {
                const target = possibleAnimals[Math.floor(Math.random() * possibleAnimals.length)];
                action = 'collect_' + ANIMALS[target].produces;
                reqAmt = Math.floor(Math.random() * 10) + 5;
                rewardGold = reqAmt * PRODUCTS[ANIMALS[target].produces].basePrice * 2.5;
                rewardXp = reqAmt * ANIMALS[target].xp * 2.5;
                name = `ความต้องการ: ผลผลิตจาก${ANIMALS[target].name}`;
                desc = `เก็บ ${PRODUCTS[ANIMALS[target].produces].name} จำนวน ${reqAmt} ชิ้น`;
            } else {
                action = 'earn_gold';
                reqAmt = 1000 * state.level;
                rewardGold = 500;
                rewardXp = 500;
                name = 'หาเงินเข้าฟาร์ม';
                desc = `หาเงินให้ได้ ${reqAmt} 🪙`;
            }
            
            // Record current stats so we track progress from 0
            const currentStat = state.stats[action] || 0;
            
            return {
                id,
                name,
                desc,
                action,
                reqAmt,
                startStat: currentStat,
                reward: { gold: rewardGold, xp: rewardXp }
            };
        }
        
        function ensureDynamicQuests() {
            if (!state.activeDynamicQuests) state.activeDynamicQuests = [];
            while (state.activeDynamicQuests.length < 3) {
                state.activeDynamicQuests.push(generateRandomQuest());
            }
        }
        
        function resetQuests() {
            // Can be called daily to reset them all
            state.activeDynamicQuests = [];
            ensureDynamicQuests();
            updateUI();
        }
"""
content = content.replace("function claimQuest(questId) {", funcs + "\n        function claimQuest(questId) {")

# Modify claimQuest to handle dynamic quests
claim_old = """        function claimQuest(questId) {
            let quest = QUESTS.find(q => q.id === questId);
            if (!quest && EVENT_QUESTS[state.season]) {
                quest = EVENT_QUESTS[state.season].find(q => q.id === questId);
            }
            if (!quest || state.claimedQuests.includes(questId)) return;
            const progress = state.stats[quest.action] || 0;
            if (progress >= quest.reqAmt) {"""

claim_new = """        function claimQuest(questId) {
            let quest = QUESTS.find(q => q.id === questId);
            let isDynamic = false;
            if (!quest && state.activeDynamicQuests) {
                quest = state.activeDynamicQuests.find(q => q.id === questId);
                if (quest) isDynamic = true;
            }
            if (!quest || state.claimedQuests.includes(questId)) return;
            
            let progress = state.stats[quest.action] || 0;
            if (isDynamic && quest.startStat) {
                progress = progress - quest.startStat;
            }
            if (progress < 0) progress = 0;
            
            if (progress >= quest.reqAmt) {"""
content = content.replace(claim_old, claim_new)

# Modify the reward logic to replace quest
reward_old = """                state.gold += Math.floor(quest.reward.gold * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 1.5 : 1));
                addXP(quest.reward.xp);
                state.claimedQuests.push(questId);
                showAlert('ทำภารกิจสำเร็จ!', `คุณได้รับ ${quest.reward.gold} 🪙 และ ${quest.reward.xp} XP`, '🏅');
                if (typeof fireConfetti === 'function') fireConfetti();
                updateUI();
            }
        }"""
reward_new = """                state.gold += Math.floor(quest.reward.gold * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 1.5 : 1));
                addXP(quest.reward.xp);
                state.claimedQuests.push(questId);
                showAlert('ทำภารกิจสำเร็จ!', `คุณได้รับ ${quest.reward.gold} 🪙 และ ${quest.reward.xp} XP`, '🏅');
                if (typeof fireConfetti === 'function') fireConfetti();
                
                if (isDynamic) {
                    state.activeDynamicQuests = state.activeDynamicQuests.filter(q => q.id !== questId);
                    ensureDynamicQuests();
                }
                updateUI();
            }
        }"""
content = content.replace(reward_old, reward_new)

# Modify renderQuests to show dynamic quests instead of EVENT_QUESTS
render_quests_old = """            let qHtml = '';
            
            // 1. Seasonal Event Quests
            const curEvent = EVENT_QUESTS[state.season] || [];
            if (curEvent.length > 0) {
                qHtml += `<div class="bg-pink-50/80 rounded-xl p-4 border border-pink-200 mb-6">
                    <h3 class="font-bold text-pink-800 mb-3 flex items-center gap-2"><span>🌸</span> ภารกิจเทศกาลประจำฤดู (รีเซ็ตเมื่อเปลี่ยนฤดู)</h3>
                    <div class="space-y-3">`;
                curEvent.forEach(q => {
                    const isClaimed = state.claimedQuests.includes(q.id);
                    const progress = state.stats[q.action] || 0;
                    const percent = Math.min(100, (progress / q.reqAmt) * 100);
                    
                    qHtml += `<div class="bg-white/80 p-3 rounded-xl border border-pink-100 flex flex-col md:flex-row justify-between items-start md:items-center gap-3">
                        <div class="flex-1">
                            <div class="font-bold text-pink-900 flex items-center gap-2">${q.name} ${isClaimed ? '<span class="text-xs bg-green-100 text-green-700 px-2 py-0.5 rounded-full">เสร็จสิ้น</span>' : ''}</div>
                            <div class="text-xs text-pink-700 mb-2">${q.desc}</div>
                            <div class="w-full bg-pink-100 h-2 rounded-full overflow-hidden">
                                <div class="bg-pink-500 h-full transition-all duration-300" style="width: ${percent}%"></div>
                            </div>
                            <div class="text-[10px] text-pink-600 font-bold mt-1">${progress}/${q.reqAmt}</div>
                        </div>
                        <div class="flex flex-row md:flex-col items-center md:items-end gap-2 w-full md:w-auto">
                            <div class="text-xs font-bold text-amber-600 bg-amber-50 px-2 py-1 rounded-lg border border-amber-200">
                                รางวัล: ${q.reward.gold} 🪙 | ${q.reward.xp} XP
                            </div>
                            ${isClaimed ? 
                                `<button disabled class="w-full md:w-auto px-4 py-1.5 bg-gray-200 text-gray-500 rounded-lg text-xs font-bold cursor-not-allowed">รับแล้ว</button>` :
                                (progress >= q.reqAmt ? 
                                    `<button onclick="claimQuest('${q.id}')" class="w-full md:w-auto px-4 py-1.5 bg-pink-500 hover:bg-pink-600 text-white rounded-lg text-xs font-bold shadow-sm transition animate-pulse">รับรางวัล!</button>` :
                                    `<button disabled class="w-full md:w-auto px-4 py-1.5 bg-pink-100 text-pink-400 rounded-lg text-xs font-bold cursor-not-allowed">ยังไม่สำเร็จ</button>`
                                )
                            }
                        </div>
                    </div>`;
                });
                qHtml += `</div></div>`;
            }"""

render_quests_new = """            let qHtml = '';
            
            ensureDynamicQuests();
            if (state.activeDynamicQuests && state.activeDynamicQuests.length > 0) {
                qHtml += `<div class="bg-blue-50/80 rounded-xl p-4 border border-blue-200 mb-6">
                    <h3 class="font-bold text-blue-800 mb-3 flex items-center gap-2"><span>📋</span> ภารกิจกระดานหมู่บ้าน (ทำเสร็จแล้วมีใหม่มาเติมทันที)</h3>
                    <div class="space-y-3">`;
                state.activeDynamicQuests.forEach(q => {
                    const isClaimed = state.claimedQuests.includes(q.id);
                    let progress = state.stats[q.action] || 0;
                    if (q.startStat) progress = Math.max(0, progress - q.startStat);
                    const percent = Math.min(100, (progress / q.reqAmt) * 100);
                    
                    qHtml += `<div class="bg-white/80 p-3 rounded-xl border border-blue-100 flex flex-col md:flex-row justify-between items-start md:items-center gap-3 shadow-sm">
                        <div class="flex-1">
                            <div class="font-bold text-blue-900 flex items-center gap-2">${q.name} ${isClaimed ? '<span class="text-xs bg-green-100 text-green-700 px-2 py-0.5 rounded-full">เสร็จสิ้น</span>' : ''}</div>
                            <div class="text-xs text-blue-700 mb-2">${q.desc}</div>
                            <div class="w-full bg-blue-100 h-2 rounded-full overflow-hidden">
                                <div class="bg-blue-500 h-full transition-all duration-300" style="width: ${percent}%"></div>
                            </div>
                            <div class="text-[10px] text-blue-600 font-bold mt-1">${progress}/${q.reqAmt}</div>
                        </div>
                        <div class="flex flex-row md:flex-col items-center md:items-end gap-2 w-full md:w-auto">
                            <div class="text-xs font-bold text-amber-600 bg-amber-50 px-2 py-1 rounded-lg border border-amber-200 shadow-sm">
                                รางวัล: ${q.reward.gold} 🪙 | ${q.reward.xp} XP
                            </div>
                            ${isClaimed ? 
                                `<button disabled class="w-full md:w-auto px-4 py-1.5 bg-gray-200 text-gray-500 rounded-lg text-xs font-bold cursor-not-allowed">รับแล้ว</button>` :
                                (progress >= q.reqAmt ? 
                                    `<button onclick="claimQuest('${q.id}')" class="w-full md:w-auto px-4 py-1.5 bg-green-500 hover:bg-green-600 text-white rounded-lg text-xs font-bold shadow-sm transition animate-bounce">รับรางวัล!</button>` :
                                    `<button disabled class="w-full md:w-auto px-4 py-1.5 bg-blue-100 text-blue-400 rounded-lg text-xs font-bold cursor-not-allowed">กำลังทำ</button>`
                                )
                            }
                        </div>
                    </div>`;
                });
                qHtml += `</div></div>`;
            }"""
content = content.replace(render_quests_old, render_quests_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

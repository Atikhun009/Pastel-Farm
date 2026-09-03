import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_create = """            const goldReward = Math.floor(totalValue * (1.1 + Math.random() * 0.4));
            const xpReward = Math.floor(goldReward * 0.5);
            
            const npcs = ['👨‍🌾 ลุงฟาร์มเมอร์', '👩‍🍳 เจ๊ร้านข้าว', '🧙‍♂️ นักเวทย์ฝึกหัด', '👷 ช่างไม้'];
            return {
                id: 'order_'+id+'_'+Date.now(),
                npc: npcs[Math.floor(Math.random() * npcs.length)],
                reqs: reqs,
                reward: { gold: goldReward, xp: xpReward },
                completed: false
            };"""

new_create = """            const goldReward = Math.floor(totalValue * (1.1 + Math.random() * 0.4));
            const xpReward = Math.floor(goldReward * 0.5);
            const diamondReward = Math.floor(Math.random() * 3) + 1; // 1 to 3 diamonds
            
            const npcs = ['👨‍🌾 ลุงฟาร์มเมอร์', '👩‍🍳 เจ๊ร้านข้าว', '🧙‍♂️ นักเวทย์ฝึกหัด', '👷 ช่างไม้'];
            return {
                id: 'order_'+id+'_'+Date.now(),
                npc: npcs[Math.floor(Math.random() * npcs.length)],
                reqs: reqs,
                reward: { gold: goldReward, xp: xpReward, diamond: diamondReward },
                completed: false
            };"""

content = content.replace(old_create, new_create)

old_fulfill = """            state.gold += Math.floor(order.reward.gold * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 1.5 : 1));
            addXP(order.reward.xp);
            order.completed = true;
            
            showAlert('ส่งของสำเร็จ!', `คุณได้รับ ${order.reward.gold} 🪙 และ ${order.reward.xp} XP`, '✅');
            if (typeof fireConfetti === 'function') fireConfetti();"""

new_fulfill = """            state.gold += Math.floor(order.reward.gold * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 2 : 1));
            state.diamonds = (state.diamonds || 0) + (order.reward.diamond || 0);
            addXP(order.reward.xp);
            order.completed = true;
            
            let diamondStr = order.reward.diamond ? ` และ ${order.reward.diamond} 💎` : '';
            showAlert('ส่งของสำเร็จ!', `คุณได้รับ ${order.reward.gold} 🪙, ${order.reward.xp} XP${diamondStr}`, '✅');
            if (typeof fireConfetti === 'function') fireConfetti();"""

content = content.replace(old_fulfill, new_fulfill)

old_render = """<div class="text-xs font-bold text-amber-600 bg-amber-50 px-2 py-1 rounded-lg border border-amber-200">
                                รางวัล: ${o.reward.gold} 🪙 | ${o.reward.xp} XP
                            </div>"""

new_render = """<div class="text-xs font-bold text-amber-600 bg-amber-50 px-2 py-1 rounded-lg border border-amber-200">
                                รางวัล: ${o.reward.gold} 🪙 | ${o.reward.xp} XP ${o.reward.diamond ? `| ${o.reward.diamond} 💎` : ''}
                            </div>"""

content = content.replace(old_render, new_render)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add container
old_nav_end = "</nav>"
new_nav_end = "</nav>\n        <!-- Active Buffs -->\n        <div id=\"active-buffs-container\" class=\"flex flex-wrap gap-2 mb-4 empty:hidden\"></div>"
content = content.replace(old_nav_end, new_nav_end)

# Add to game loop
old_gameloop = """        function gameLoop() {
            const now = Date.now();
            const dt = now - lastTime;
            lastTime = now;"""

new_gameloop = """        function formatTimeLeft(ms) {
            if (ms <= 0) return '0s';
            let totalSeconds = Math.floor(ms / 1000);
            let m = Math.floor(totalSeconds / 60);
            let s = totalSeconds % 60;
            return m > 0 ? `${m}m ${s}s` : `${s}s`;
        }

        function gameLoop() {
            const now = Date.now();
            const dt = now - lastTime;
            lastTime = now;
            
            // Update Buffs UI
            const buffContainer = document.getElementById('active-buffs-container');
            if (buffContainer && state.activeBuffs) {
                let buffsHtml = '';
                if (state.activeBuffs.goldMultEnd && now < state.activeBuffs.goldMultEnd) {
                    buffsHtml += `<div class="bg-amber-100 border border-amber-300 text-amber-800 text-xs font-bold px-3 py-1.5 rounded-lg flex items-center gap-1 shadow-sm"><span class="animate-pulse">💰 เงิน x2 :</span> <span>${formatTimeLeft(state.activeBuffs.goldMultEnd - now)}</span></div>`;
                }
                if (state.activeBuffs.cropSpeedEnd && now < state.activeBuffs.cropSpeedEnd) {
                    buffsHtml += `<div class="bg-green-100 border border-green-300 text-green-800 text-xs font-bold px-3 py-1.5 rounded-lg flex items-center gap-1 shadow-sm"><span class="animate-pulse">🌱 พืชโตไว x2 :</span> <span>${formatTimeLeft(state.activeBuffs.cropSpeedEnd - now)}</span></div>`;
                }
                if (state.activeBuffs.animalSpeedEnd && now < state.activeBuffs.animalSpeedEnd) {
                    buffsHtml += `<div class="bg-orange-100 border border-orange-300 text-orange-800 text-xs font-bold px-3 py-1.5 rounded-lg flex items-center gap-1 shadow-sm"><span class="animate-pulse">🐾 สัตว์ผลิตไว x2 :</span> <span>${formatTimeLeft(state.activeBuffs.animalSpeedEnd - now)}</span></div>`;
                }
                if (state.activeBuffs.doubleDropEnd && now < state.activeBuffs.doubleDropEnd) {
                    buffsHtml += `<div class="bg-blue-100 border border-blue-300 text-blue-800 text-xs font-bold px-3 py-1.5 rounded-lg flex items-center gap-1 shadow-sm"><span class="animate-pulse">🍀 โอกาสเบิ้ล 100% :</span> <span>${formatTimeLeft(state.activeBuffs.doubleDropEnd - now)}</span></div>`;
                }
                if (buffContainer.innerHTML !== buffsHtml) {
                    buffContainer.innerHTML = buffsHtml;
                }
            }"""

content = content.replace(old_gameloop, new_gameloop)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

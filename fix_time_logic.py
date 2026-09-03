import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_loop_start = """        function gameLoop() {
            const now = Date.now();
            // Season logic (10 minutes = 600,000 ms)
            if (!state.seasonStartTime) state.seasonStartTime = now;
            const seasonIndex = Math.floor((now - state.seasonStartTime) / 600000) % 4;"""

new_loop_start = """        function gameLoop() {
            const now = Date.now();
            
            if (!state.seasonStartTime) state.seasonStartTime = now;
            
            // Time & Day/Night Cycle (2 minutes = 1 in-game day = 120,000 ms)
            const timeOfDay = ((now - state.seasonStartTime) % 120000) / 120000;
            const timeLayer = document.getElementById('time-layer');
            const uiTime = document.getElementById('ui-time');
            
            let timeStr = "";
            let timeColor = "text-amber-800 bg-amber-100/80";
            
            if (timeOfDay < 0.5) { // 06:00 - 18:00
                if(timeLayer) timeLayer.style.backgroundColor = "transparent";
                const hours = Math.floor(6 + (timeOfDay / 0.5) * 12);
                const minutes = Math.floor((((timeOfDay / 0.5) * 12) % 1) * 60);
                timeStr = `☀️ ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
                timeColor = "text-amber-800 bg-amber-100/80";
            } else if (timeOfDay < 0.75) { // 18:00 - 24:00
                const eveningProg = (timeOfDay - 0.5) / 0.25;
                if(timeLayer) timeLayer.style.backgroundColor = `rgba(15, 10, 40, ${eveningProg * 0.4})`;
                const hours = Math.floor(18 + eveningProg * 6);
                const minutes = Math.floor(((eveningProg * 6) % 1) * 60);
                timeStr = `🌇 ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
                timeColor = "text-orange-800 bg-orange-100/80";
            } else { // 00:00 - 06:00
                const nightProg = (timeOfDay - 0.75) / 0.25;
                const alpha = 0.4 - (nightProg * 0.4);
                if(timeLayer) timeLayer.style.backgroundColor = `rgba(15, 10, 40, ${alpha})`;
                const hours = Math.floor(0 + nightProg * 6);
                const minutes = Math.floor(((nightProg * 6) % 1) * 60);
                timeStr = `🌙 ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
                timeColor = "text-indigo-800 bg-indigo-100/80";
            }
            
            if (uiTime) {
                if (state.upgrades && state.upgrades.weather_radar) {
                    uiTime.classList.remove('hidden');
                    // Add time remaining for season
                    const msLeft = 600000 - ((now - state.seasonStartTime) % 600000);
                    const minsLeft = Math.floor(msLeft / 60000);
                    const secsLeft = Math.floor((msLeft % 60000) / 1000);
                    uiTime.innerText = `${timeStr} (ฤดูเปลี่ยนใน ${minsLeft}:${secsLeft.toString().padStart(2, '0')})`;
                    uiTime.className = `text-sm font-semibold px-3 py-0.5 rounded-full shadow-sm border border-white transition-all ${timeColor}`;
                } else {
                    uiTime.classList.add('hidden');
                }
            }

            // Season logic (10 minutes = 600,000 ms)
            const seasonIndex = Math.floor((now - state.seasonStartTime) / 600000) % 4;"""

content = content.replace(old_loop_start, new_loop_start)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fallback_old = "if (!state.inventory.barnResetCoupons === undefined) state.inventory.barnResetCoupons = 0;"
fallback_new = """if (state.inventory.barnResetCoupons === undefined) state.inventory.barnResetCoupons = 0;
                    if (!state.gameTime) state.gameTime = { year: 1, seasonIndex: 0, day: 1, minute: 360 };"""
content = content.replace(fallback_old, fallback_new)
content = content.replace("if (!state.inventory.barnResetCoupons === undefined) state.inventory.barnResetCoupons = 0;", "if (state.inventory.barnResetCoupons === undefined) state.inventory.barnResetCoupons = 0;")

gameloop_pat = r"// Season logic \(10 minutes = 600,000 ms\)\n\s*if \(\!state\.seasonStartTime\) state\.seasonStartTime = now;\n\s*const seasonIndex = Math\.floor\(\(now - state\.seasonStartTime\) / 600000\) % 4;\n\s*const currentSeason = SEASONS\[seasonIndex\];"
gameloop_new = """// Stardew Valley style calendar system
            if (!state.gameTime) state.gameTime = { year: 1, seasonIndex: 0, day: 1, minute: 360 };
            
            // Advance time (1 real second = 10 in-game minutes)
            state.gameTime.minute += 10;
            if (state.gameTime.minute >= 1440) {
                state.gameTime.minute -= 1440;
                state.gameTime.day += 1;
                // Generate new quests every day
                if (typeof resetQuests === 'function') resetQuests();
                
                if (state.gameTime.day > 28) {
                    state.gameTime.day = 1;
                    state.gameTime.seasonIndex = (state.gameTime.seasonIndex + 1) % 4;
                    if (state.gameTime.seasonIndex === 0) {
                        state.gameTime.year += 1;
                    }
                }
            }
            
            const currentSeason = SEASONS[state.gameTime.seasonIndex];
            
            // Format time for UI
            const hours = Math.floor(state.gameTime.minute / 60);
            const mins = state.gameTime.minute % 60;
            const ampm = hours >= 12 ? 'PM' : 'AM';
            const displayHours = hours % 12 === 0 ? 12 : hours % 12;
            const timeStr = `${displayHours}:${mins.toString().padStart(2, '0')} ${ampm}`;
            const uiCalendar = document.getElementById('ui-calendar');
            if (uiCalendar) {
                uiCalendar.innerText = `ปี ${state.gameTime.year} ฤดู${currentSeason === 'spring' ? 'ใบไม้ผลิ' : currentSeason === 'summer' ? 'ร้อน' : currentSeason === 'autumn' ? 'ใบไม้ร่วง' : 'หนาว'} วันที่ ${state.gameTime.day} | ${timeStr}`;
            }"""
content = re.sub(gameloop_pat, gameloop_new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

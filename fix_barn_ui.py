import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_render_inv = """        function renderInventory() {
            const seedEntries = Object.entries(state.inventory.seeds).filter(([_, qty]) => qty > 0);"""

new_render_inv = """        function renderInventory() {
            // Update Barn UI
            const uiBarnLvl = document.getElementById('ui-barn-level');
            const uiBarnCur = document.getElementById('ui-barn-cur');
            const uiBarnMax = document.getElementById('ui-barn-max');
            const uiBarnFill = document.getElementById('ui-barn-fill');
            
            if (uiBarnLvl) {
                const cur = getCurrentItemsCount();
                const mx = getBarnCapacity();
                const lvl = state.inventory.barnLevel || 1;
                uiBarnLvl.innerText = `Lv.${lvl}`;
                uiBarnCur.innerText = cur;
                uiBarnMax.innerText = mx >= 999999 ? 'MAX' : mx;
                
                let percent = (cur / mx) * 100;
                if (percent > 100) percent = 100;
                uiBarnFill.style.width = `${percent}%`;
                
                if (percent >= 90) {
                    uiBarnFill.className = "h-full bg-red-500 transition-all duration-300";
                    uiBarnCur.className = "text-red-600 font-black animate-pulse";
                } else if (percent >= 70) {
                    uiBarnFill.className = "h-full bg-orange-400 transition-all duration-300";
                    uiBarnCur.className = "text-orange-600 font-bold";
                } else {
                    uiBarnFill.className = "h-full bg-green-500 transition-all duration-300";
                    uiBarnCur.className = "";
                }
            }

            const seedEntries = Object.entries(state.inventory.seeds).filter(([_, qty]) => qty > 0);"""

content = content.replace(old_render_inv, new_render_inv)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

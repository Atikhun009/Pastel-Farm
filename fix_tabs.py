import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_tabs = "const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements', 'redeem'];"
new_tabs = "const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements', 'redeem', 'diamond'];"
content = content.replace(old_tabs, new_tabs)

old_btn = """                if(btn) {
                    btn.classList.remove('bg-white', 'text-green-900', 'shadow-sm');
                    btn.classList.add('hover:bg-white/70', 'text-green-700');
                }"""

new_btn = """                if(btn) {
                    btn.classList.remove('bg-white', 'text-green-900', 'shadow-sm', 'text-blue-900');
                    if (t === 'diamond') {
                        btn.classList.add('hover:bg-white/70', 'text-blue-700');
                    } else {
                        btn.classList.add('hover:bg-white/70', 'text-green-700');
                    }
                }"""
content = content.replace(old_btn, new_btn)

old_active_btn = """            const activeBtn = document.getElementById(`tab-${tabId}`);
            if(activeBtn) {
                activeBtn.classList.add('bg-white', 'text-green-900', 'shadow-sm');
                activeBtn.classList.remove('hover:bg-white/70', 'text-green-700');
            }"""

new_active_btn = """            const activeBtn = document.getElementById(`tab-${tabId}`);
            if(activeBtn) {
                if (tabId === 'diamond') {
                    activeBtn.classList.add('bg-white', 'text-blue-900', 'shadow-sm');
                    activeBtn.classList.remove('hover:bg-white/70', 'text-blue-700');
                } else {
                    activeBtn.classList.add('bg-white', 'text-green-900', 'shadow-sm');
                    activeBtn.classList.remove('hover:bg-white/70', 'text-green-700');
                }
            }"""
content = content.replace(old_active_btn, new_active_btn)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

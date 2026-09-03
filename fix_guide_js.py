import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_tabs = "const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements', 'redeem', 'diamond', 'rebirth'];"
new_tabs = "const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements', 'redeem', 'diamond', 'rebirth', 'guide'];"
content = content.replace(old_tabs, new_tabs)

old_btn = """                    } else if (t === 'rebirth') {
                        btn.classList.add('hover:bg-white/70', 'text-purple-700');
                    } else {"""
new_btn = """                    } else if (t === 'rebirth') {
                        btn.classList.add('hover:bg-white/70', 'text-purple-700');
                    } else if (t === 'guide') {
                        btn.classList.add('hover:bg-white/70', 'text-orange-700');
                    } else {"""
content = content.replace(old_btn, new_btn)

old_active = """                } else if (tabId === 'rebirth') {
                    activeBtn.classList.add('bg-white', 'text-purple-900', 'shadow-sm');
                    activeBtn.classList.remove('hover:bg-white/70', 'text-purple-700');
                } else {"""
new_active = """                } else if (tabId === 'rebirth') {
                    activeBtn.classList.add('bg-white', 'text-purple-900', 'shadow-sm');
                    activeBtn.classList.remove('hover:bg-white/70', 'text-purple-700');
                } else if (tabId === 'guide') {
                    activeBtn.classList.add('bg-white', 'text-orange-900', 'shadow-sm');
                    activeBtn.classList.remove('hover:bg-white/70', 'text-orange-700');
                } else {"""
content = content.replace(old_active, new_active)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


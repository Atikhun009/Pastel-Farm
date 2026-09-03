import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add switchTab('farm') in initGame
old_init = "function initGame() {"
new_init = "function initGame() {\n            switchTab('farm');"
content = content.replace(old_init, new_init)

# Fix switchTab logic
old_switch = """        function switchTab(tabId) {
            const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements'];
            tabs.forEach(t => {
                const view = document.getElementById(`view-${t}`);
                if(view) view.classList.add('hidden');
                const btn = document.getElementById(`tab-${t}`);
                if(btn) {
                    btn.classList.replace('bg-white', 'hover:bg-white/70');
                    btn.classList.replace('text-green-900', 'text-green-700');
                }
            });
            const activeView = document.getElementById(`view-${tabId}`);
            if(activeView) activeView.classList.remove('hidden');
            const activeBtn = document.getElementById(`tab-${tabId}`);
            if(activeBtn) {
                activeBtn.classList.replace('hover:bg-white/70', 'bg-white');
                activeBtn.classList.replace('text-green-700', 'text-green-900');
            }
        }"""
new_switch = """        function switchTab(tabId) {
            const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements'];
            tabs.forEach(t => {
                const view = document.getElementById(`view-${t}`);
                if(view) view.classList.add('hidden');
                const btn = document.getElementById(`tab-${t}`);
                if(btn) {
                    btn.classList.remove('bg-white', 'text-green-900', 'shadow-sm');
                    btn.classList.add('hover:bg-white/70', 'text-green-700');
                }
            });
            const activeView = document.getElementById(`view-${tabId}`);
            if(activeView) activeView.classList.remove('hidden');
            const activeBtn = document.getElementById(`tab-${tabId}`);
            if(activeBtn) {
                activeBtn.classList.remove('hover:bg-white/70', 'text-green-700');
                activeBtn.classList.add('bg-white', 'text-green-900', 'shadow-sm');
            }
            
            const tabsContainer = document.getElementById('view-tabs-container');
            if (tabsContainer) {
                if (tabId === 'farm') {
                    tabsContainer.classList.add('hidden');
                } else {
                    tabsContainer.classList.remove('hidden');
                }
            }
        }"""
content = content.replace(old_switch, new_switch)

# ensure view-tabs-container has an ID
content = content.replace('<!-- Right Column: Interactive Tabs -->\n            <div class="w-full">', '<!-- Right Column: Interactive Tabs -->\n            <div id="view-tabs-container" class="w-full">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


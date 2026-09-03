import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

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

content = re.sub(r'function switchTab\(tabId\) \{[\s\S]*?(?=\n\s*function showAlert)', new_switch, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

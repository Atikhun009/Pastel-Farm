import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. We will extract the Tabs Menu block.
# Let's find the exact block.
tabs_menu_start = content.find('<!-- Tabs Menu -->')
tabs_menu_end = content.find('<!-- Achievements Content -->')

if tabs_menu_start != -1 and tabs_menu_end != -1:
    tabs_menu_html = content[tabs_menu_start:tabs_menu_end]
    
    # Remove from original place
    content = content[:tabs_menu_start] + content[tabs_menu_end:]
    
    # We need to add "tab-farm" to tabs_menu_html
    farm_tab = """
                        <button id="tab-farm" onclick="switchTab('farm')" class="px-4 py-2.5 rounded-xl text-sm font-bold bg-white shadow-sm text-green-900 transition flex-1">
                            🚜 ฟาร์ม
                        </button>"""
    # Just insert it after <div class="flex gap-2 ...">
    div_start = tabs_menu_html.find('hide-scroll">') + len('hide-scroll">')
    tabs_menu_html = tabs_menu_html[:div_start] + farm_tab + tabs_menu_html[div_start:]
    
    # Make other tabs not active by default (replace bg-white with hover:bg-white/70 etc.)
    tabs_menu_html = tabs_menu_html.replace('bg-white shadow-sm text-green-900 transition', 'text-green-700 hover:bg-white/70 transition')
    # Re-activate farm tab
    tabs_menu_html = tabs_menu_html.replace(
        '<button id="tab-farm" onclick="switchTab(\'farm\')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">',
        '<button id="tab-farm" onclick="switchTab(\'farm\')" class="px-4 py-2.5 rounded-xl text-sm font-bold bg-white shadow-sm text-green-900 transition flex-1">'
    )
    
    # Insert Tabs Menu above Main Game Area Grid
    grid_start = content.find('<!-- Main Game Area Grid -->')
    
    tabs_wrapper = f"""
        <!-- Top Navigation Tabs -->
        <nav class="glass-panel p-2 md:p-3 rounded-2xl relative z-10 w-full mb-6">
            <div class="flex gap-2 overflow-x-auto whitespace-nowrap hide-scroll">
                {tabs_menu_html.replace('<!-- Tabs Menu -->', '').replace('<div class="flex gap-2 mb-5 bg-white/40 p-1.5 rounded-2xl shadow-inner overflow-x-auto whitespace-nowrap hide-scroll">', '').replace('</div>', '').strip()}
            </div>
        </nav>
        
        <!-- Main Game Area Grid -->"""
        
    content = content[:grid_start] + tabs_wrapper + content[grid_start + len('<!-- Main Game Area Grid -->'):]
    
# 2. Modify grid layout and view-farm
content = content.replace('<div class="grid grid-cols-1 lg:grid-cols-12 gap-6 relative z-10">', '<div class="relative z-10">')
content = content.replace('<div class="lg:col-span-8 space-y-6">', '<div id="view-farm" class="space-y-6">')

# 3. Clean up right column
content = content.replace('<div class="lg:col-span-4 h-full">', '<div class="w-full">')
# change section fixed height to just min-h
content = content.replace('<section class="glass-panel p-5 md:p-6 rounded-[2rem] flex flex-col h-[700px]">', '<section class="glass-panel p-5 md:p-6 rounded-[2rem] flex flex-col min-h-[500px]">')


# 4. Modify switchTab function to include 'farm'
old_switchTab = "const tabs = ['market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements'];"
new_switchTab = "const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements'];"
content = content.replace(old_switchTab, new_switchTab)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


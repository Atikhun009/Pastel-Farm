import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add state variable
old_state = r"autoHarvesterUnlocked: false,\s*lastAutoHarvest: 0"
new_state = "autoHarvesterUnlocked: false,\n            autoHarvesterActive: true,\n            lastAutoHarvest: 0"
content = re.sub(old_state, new_state, content)

# 2. Add Auto Harvester toggle logic
toggle_script = """        function toggleAutoHarvester() {
            state.autoHarvesterActive = !state.autoHarvesterActive;
            updateUI();
        }
"""
# Insert before updateUI function
update_ui_idx = content.find("function updateUI()")
content = content[:update_ui_idx] + toggle_script + "\n" + content[update_ui_idx:]

# 3. Update game loop to respect autoHarvesterActive
old_game_loop = r"if \(\(state\.autoHarvesterUnlocked \|\| \(state\.upgrades && state\.upgrades\.auto_harvester\)\) && \(\!state\.lastAutoHarvest \|\| now - state\.lastAutoHarvest > 2000\)\) \{"
new_game_loop = r"if (state.autoHarvesterActive !== false && (state.autoHarvesterUnlocked || (state.upgrades && state.upgrades.auto_harvester)) && (!state.lastAutoHarvest || now - state.lastAutoHarvest > 2000)) {"
content = re.sub(old_game_loop, new_game_loop, content)

# 4. Modify updateUI to show/hide and update the toggle button
# Let's find updateUI() and insert the logic at the top of it.
update_ui_header = """function updateUI() {
            // Auto Harvester Button
            const toggleBtn = document.getElementById('btn-toggle-auto');
            if (toggleBtn) {
                if (state.autoHarvesterUnlocked || (state.upgrades && state.upgrades.auto_harvester)) {
                    toggleBtn.classList.remove('hidden');
                    const isActive = state.autoHarvesterActive !== false;
                    document.getElementById('ui-auto-status').innerText = isActive ? 'เปิด' : 'ปิด';
                    document.getElementById('ui-auto-status').className = isActive ? 'text-white' : 'text-red-100';
                    toggleBtn.className = isActive 
                        ? 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600'
                        : 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-red-400 text-white hover:bg-red-500';
                } else {
                    toggleBtn.classList.add('hidden');
                }
            }"""
content = content.replace("function updateUI() {", update_ui_header)

# 5. Insert HTML for the button
old_html_plots = r"<h2 class=\"text-xl font-bold text-green-900 flex items-center gap-2\">\s*<span class=\"text-2xl\">🌱</span> แปลงเพาะปลูก\s*</h2>"
new_html_plots = """<div class="flex items-center gap-3">
                            <h2 class="text-xl font-bold text-green-900 flex items-center gap-2">
                                <span class="text-2xl">🌱</span> แปลงเพาะปลูก
                            </h2>
                            <button id="btn-toggle-auto" onclick="toggleAutoHarvester()" class="hidden text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600">
                                🤖 ออโต้: <span id="ui-auto-status" class="text-white">เปิด</span>
                            </button>
                        </div>"""
content = re.sub(old_html_plots, new_html_plots, content)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


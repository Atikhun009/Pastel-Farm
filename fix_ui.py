import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_ui = """            const toggleBtn = document.getElementById('btn-toggle-auto');
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

new_ui = """            const toggleBtnCrop = document.getElementById('btn-toggle-auto-crop');
            if (toggleBtnCrop) {
                if (state.upgrades && state.upgrades.auto_harvester_crop) {
                    toggleBtnCrop.classList.remove('hidden');
                    const isActive = state.autoHarvesterCropActive !== false;
                    document.getElementById('ui-auto-crop-status').innerText = isActive ? 'เปิด' : 'ปิด';
                    document.getElementById('ui-auto-crop-status').className = isActive ? 'text-white' : 'text-red-100';
                    toggleBtnCrop.className = isActive 
                        ? 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600'
                        : 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-red-400 text-white hover:bg-red-500';
                } else {
                    toggleBtnCrop.classList.add('hidden');
                }
            }
            
            const toggleBtnAnimal = document.getElementById('btn-toggle-auto-animal');
            if (toggleBtnAnimal) {
                if (state.upgrades && state.upgrades.auto_harvester_animal) {
                    toggleBtnAnimal.classList.remove('hidden');
                    const isActive = state.autoHarvesterAnimalActive !== false;
                    document.getElementById('ui-auto-animal-status').innerText = isActive ? 'เปิด' : 'ปิด';
                    document.getElementById('ui-auto-animal-status').className = isActive ? 'text-white' : 'text-red-100';
                    toggleBtnAnimal.className = isActive 
                        ? 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-amber-500 text-white hover:bg-amber-600'
                        : 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-red-400 text-white hover:bg-red-500';
                } else {
                    toggleBtnAnimal.classList.add('hidden');
                }
            }"""

content = content.replace(old_ui, new_ui)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_toggle = """function toggleAutoHarvester() {
            state.autoHarvesterActive = !state.autoHarvesterActive;
            updateUI();
        }"""
new_toggle = """function toggleAutoHarvesterCrop() {
            state.autoHarvesterCropActive = state.autoHarvesterCropActive === false ? true : false;
            updateUI();
        }
        function toggleAutoHarvesterAnimal() {
            state.autoHarvesterAnimalActive = state.autoHarvesterAnimalActive === false ? true : false;
            updateUI();
        }"""
        
content = content.replace(old_toggle, new_toggle)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

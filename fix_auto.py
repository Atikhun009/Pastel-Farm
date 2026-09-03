import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Auto crop
crop_pat = r"if \(state\.autoHarvesterCropActive !== false && \(state\.upgrades && state\.upgrades\.auto_harvester_crop\) && \(\!state\.lastAutoHarvestCrop \|\| now \- state\.lastAutoHarvestCrop > 2000\)\) \{"
content = re.sub(crop_pat, "if (state.autoHarvesterCropActive !== false && state.upgrades && state.upgrades.auto_harvester_crop) {", content)

# Auto animal
animal_pat = r"if \(state\.autoHarvesterAnimalActive !== false && \(state\.upgrades && state\.upgrades\.auto_harvester_animal\) && \(\!state\.lastAutoHarvestAnimal \|\| now \- state\.lastAutoHarvestAnimal > 2000\)\) \{"
content = re.sub(animal_pat, "if (state.autoHarvesterAnimalActive !== false && state.upgrades && state.upgrades.auto_harvester_animal) {", content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

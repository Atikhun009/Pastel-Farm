import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to get elFertilize in the state.plots.forEach(plot => { block
old_block = """            state.plots.forEach(plot => {
                const elLocked = document.getElementById(`plot-${plot.id}-locked`);
                const elEmpty = document.getElementById(`plot-${plot.id}-empty`);
                const elGrowing = document.getElementById(`plot-${plot.id}-growing`);
                const elHarvest = document.getElementById(`plot-${plot.id}-harvest`);"""

new_block = """            state.plots.forEach(plot => {
                const elLocked = document.getElementById(`plot-${plot.id}-locked`);
                const elEmpty = document.getElementById(`plot-${plot.id}-empty`);
                const elGrowing = document.getElementById(`plot-${plot.id}-growing`);
                const elHarvest = document.getElementById(`plot-${plot.id}-harvest`);
                const elFertilize = document.getElementById(`plot-${plot.id}-fertilize`);"""

content = content.replace(old_block, new_block)

old_progress = """                    if (progress >= 100) {
                        elGrowing.classList.add('hidden');
                        elHarvest.classList.remove('hidden');
                        document.getElementById(`plot-${plot.id}-harvest-emoji`).innerText = PRODUCTS[seed.produces].emoji;
                    } else {
                        elGrowing.classList.remove('hidden');
                        elHarvest.classList.add('hidden');"""
                        
new_progress = """                    if (progress >= 100) {
                        elGrowing.classList.add('hidden');
                        elHarvest.classList.remove('hidden');
                        if (elFertilize) elFertilize.classList.add('hidden');
                        document.getElementById(`plot-${plot.id}-harvest-emoji`).innerText = PRODUCTS[seed.produces].emoji;
                    } else {
                        elGrowing.classList.remove('hidden');
                        elHarvest.classList.add('hidden');
                        if (elFertilize) {
                            if (state.inventory.fertilizer > 0) {
                                elFertilize.classList.remove('hidden');
                                document.getElementById(`plot-${plot.id}-fert-count`).innerText = state.inventory.fertilizer;
                            } else {
                                elFertilize.classList.add('hidden');
                            }
                        }"""

content = content.replace(old_progress, new_progress)

# and when plot is empty/locked
old_empty = """                } else {
                    elEmpty.classList.remove('hidden');
                    elGrowing.classList.add('hidden');
                    elHarvest.classList.add('hidden');
                }"""
new_empty = """                } else {
                    elEmpty.classList.remove('hidden');
                    elGrowing.classList.add('hidden');
                    elHarvest.classList.add('hidden');
                    if (elFertilize) elFertilize.classList.add('hidden');
                }"""
content = content.replace(old_empty, new_empty)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


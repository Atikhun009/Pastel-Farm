import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix hide on harvest
old_harvest = """                    if (progress >= 100) {
                        elGrowing.classList.add('hidden');
                        elHarvest.classList.remove('hidden');
                        if (elFertilize) elFertilize.classList.add('hidden');
                        document.getElementById(`plot-${plot.id}-harvest-emoji`).innerText = PRODUCTS[seed.produces].emoji;"""

new_harvest = """                    if (progress >= 100) {
                        elGrowing.classList.add('hidden');
                        elHarvest.classList.remove('hidden');
                        if (elFertilize) elFertilize.classList.add('hidden');
                        const wOverlay = document.getElementById(`plot-${plot.id}-weather`);
                        if (wOverlay) wOverlay.classList.add('hidden');
                        document.getElementById(`plot-${plot.id}-harvest-emoji`).innerText = PRODUCTS[seed.produces].emoji;"""

if old_harvest in content:
    content = content.replace(old_harvest, new_harvest)
    print("harvest hidden updated")

old_empty = """                } else {
                    elEmpty.classList.remove('hidden');
                    elGrowing.classList.add('hidden');
                    elHarvest.classList.add('hidden');
                    if (elFertilize) elFertilize.classList.add('hidden');
                }"""

new_empty = """                } else {
                    elEmpty.classList.remove('hidden');
                    elGrowing.classList.add('hidden');
                    elHarvest.classList.add('hidden');
                    if (elFertilize) elFertilize.classList.add('hidden');
                    const wOverlay = document.getElementById(`plot-${plot.id}-weather`);
                    if (wOverlay) wOverlay.classList.add('hidden');
                }"""

if old_empty in content:
    content = content.replace(old_empty, new_empty)
    print("empty hidden updated")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

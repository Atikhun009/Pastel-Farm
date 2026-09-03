import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix auto harvester animal premium_feed
old_loop = """            // Auto-Harvester (Animal)
            if (state.autoHarvesterAnimalActive !== false && state.upgrades && state.upgrades.auto_harvester_animal) {
                state.lastAutoHarvestAnimal = now;
                state.pens.forEach(pen => {
                    if (pen.unlocked && pen.animalId && pen.lastCollected) {
                        const animal = ANIMALS[pen.animalId];
                        const elapsedSec = (now - pen.lastCollected) / 1000;
                        if (elapsedSec >= animal.cooldown) {"""

new_loop = """            // Auto-Harvester (Animal)
            if (state.autoHarvesterAnimalActive !== false && state.upgrades && state.upgrades.auto_harvester_animal) {
                state.lastAutoHarvestAnimal = now;
                state.pens.forEach(pen => {
                    if (pen.unlocked && pen.animalId && pen.lastCollected) {
                        const animal = ANIMALS[pen.animalId];
                        let elapsedSec = (now - pen.lastCollected) / 1000;
                        if (state.upgrades && state.upgrades.premium_feed) {
                            elapsedSec *= (1 + (state.upgrades.premium_feed * 0.005));
                        }
                        if (elapsedSec >= animal.cooldown) {"""

content = content.replace(old_loop, new_loop)

# Fix calendar text overflow
old_calendar = """<div id="ui-calendar" class="px-4 py-2.5 rounded-xl text-sm font-bold bg-white/80 shadow-sm border border-blue-200 text-blue-800 flex-1 flex items-center justify-center whitespace-nowrap min-w-[200px]">"""
new_calendar = """<div id="ui-calendar" class="px-3 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-white/80 shadow-sm border border-blue-200 text-blue-800 flex-1 flex items-center justify-center min-w-0 text-center break-words leading-tight">"""

content = content.replace(old_calendar, new_calendar)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

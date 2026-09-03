import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update UI animal progress
old_progress = """                    if (state.upgrades && state.upgrades.premium_feed) {
                        elapsedSec *= (1 + (state.upgrades.premium_feed * 0.005));
                    }
                    const progress = Math.min((elapsedSec / animal.cooldown) * 100, 100);"""

new_progress = """                    if (state.upgrades && state.upgrades.premium_feed) {
                        elapsedSec *= (1 + (state.upgrades.premium_feed * 0.005));
                    }
                    if (state.activeBuffs && state.activeBuffs.animalSpeedEnd && now < state.activeBuffs.animalSpeedEnd) {
                        elapsedSec *= 2;
                    }
                    const progress = Math.min((elapsedSec / animal.cooldown) * 100, 100);"""

content = content.replace(old_progress, new_progress)

# Update Auto-Harvester animal progress
old_auto_animal = """                        let elapsedSec = (now - pen.lastCollected) / 1000;
                        if (state.upgrades && state.upgrades.premium_feed) {
                            elapsedSec *= (1 + (state.upgrades.premium_feed * 0.005));
                        }
                        if (elapsedSec >= animal.cooldown) {"""

new_auto_animal = """                        let elapsedSec = (now - pen.lastCollected) / 1000;
                        if (state.upgrades && state.upgrades.premium_feed) {
                            elapsedSec *= (1 + (state.upgrades.premium_feed * 0.005));
                        }
                        if (state.activeBuffs && state.activeBuffs.animalSpeedEnd && now < state.activeBuffs.animalSpeedEnd) {
                            elapsedSec *= 2;
                        }
                        if (elapsedSec >= animal.cooldown) {"""

content = content.replace(old_auto_animal, new_auto_animal)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

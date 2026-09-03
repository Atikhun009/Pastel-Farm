import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_auto = """            // Auto-Harvester
            if (state.autoHarvesterActive !== false && (state.autoHarvesterUnlocked || (state.upgrades && state.upgrades.auto_harvester)) && (!state.lastAutoHarvest || now - state.lastAutoHarvest > 2000)) {
                state.lastAutoHarvest = now;
                state.plots.forEach(plot => {
                    if (plot.unlocked && plot.seedId && plot.plantedAt) {
                        const seed = SEEDS[plot.seedId];
                        let elapsedSec = (now - plot.plantedAt) / 1000;
                        elapsedSec *= plantSpeedMult;
                        if (elapsedSec >= seed.growTime) {
                            harvest(plot.id);
                        }
                    }
                });
                state.pens.forEach(pen => {
                    if (pen.unlocked && pen.animalId && pen.lastCollected) {
                        const animal = ANIMALS[pen.animalId];
                        const elapsedSec = (now - pen.lastCollected) / 1000;
                        if (elapsedSec >= animal.cooldown) {
                            collectAnimal(pen.id);
                        }
                    }
                });
            }"""

new_auto = """            // Auto-Harvester (Crop)
            if (state.autoHarvesterCropActive !== false && (state.upgrades && state.upgrades.auto_harvester_crop) && (!state.lastAutoHarvestCrop || now - state.lastAutoHarvestCrop > 2000)) {
                state.lastAutoHarvestCrop = now;
                state.plots.forEach(plot => {
                    if (plot.unlocked && plot.seedId && plot.plantedAt) {
                        const seed = SEEDS[plot.seedId];
                        let elapsedSec = (now - plot.plantedAt) / 1000;
                        elapsedSec *= plantSpeedMult;
                        if (elapsedSec >= seed.growTime) {
                            if (checkBarnCapacity(1)) {
                                harvest(plot.id, true);
                            }
                        }
                    }
                });
            }

            // Auto-Harvester (Animal)
            if (state.autoHarvesterAnimalActive !== false && (state.upgrades && state.upgrades.auto_harvester_animal) && (!state.lastAutoHarvestAnimal || now - state.lastAutoHarvestAnimal > 2000)) {
                state.lastAutoHarvestAnimal = now;
                state.pens.forEach(pen => {
                    if (pen.unlocked && pen.animalId && pen.lastCollected) {
                        const animal = ANIMALS[pen.animalId];
                        const elapsedSec = (now - pen.lastCollected) / 1000;
                        if (elapsedSec >= animal.cooldown) {
                            if (checkBarnCapacity(1)) {
                                collectAnimal(pen.id, true);
                            }
                        }
                    }
                });
            }"""

content = content.replace(old_auto, new_auto)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

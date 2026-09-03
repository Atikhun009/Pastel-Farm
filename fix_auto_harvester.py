import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update UPGRADES
old_upgrade = "auto_harvester: { id: 'auto_harvester', name: 'เครื่องเก็บเกี่ยวออโต้', emoji: '🚜', desc: 'ปลดล็อกปุ่มเก็บเกี่ยวพืชทั้งหมดพร้อมกัน', buyPrice: 2000, maxLevel: 1, priceMult: 1, type: 'feature' },"
new_upgrade = """auto_harvester_crop: { id: 'auto_harvester_crop', name: 'เครื่องเกี่ยวข้าวออโต้', emoji: '🚜', desc: 'เก็บเกี่ยวพืชอัตโนมัติเมื่อโตเต็มที่', buyPrice: 6000, maxLevel: 1, priceMult: 1, type: 'feature' },
            auto_harvester_animal: { id: 'auto_harvester_animal', name: 'เครื่องรีดนมออโต้', emoji: '🐄', desc: 'เก็บผลผลิตสัตว์อัตโนมัติ', buyPrice: 6000, maxLevel: 1, priceMult: 1, type: 'feature' },"""

content = content.replace(old_upgrade, new_upgrade)

# 2. Update toggle button UI
old_btn = """                            <button id="btn-toggle-auto" onclick="toggleAutoHarvester()" class="hidden text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600">
                                🤖 เก็บเกี่ยว: <span id="ui-auto-status" class="text-white">เปิด</span>
                            </button>"""
new_btn = """                            <button id="btn-toggle-auto-crop" onclick="toggleAutoHarvesterCrop()" class="hidden text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600">
                                🚜 พืชออโต้: <span id="ui-auto-crop-status" class="text-white">เปิด</span>
                            </button>
                            <button id="btn-toggle-auto-animal" onclick="toggleAutoHarvesterAnimal()" class="hidden text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-amber-500 text-white hover:bg-amber-600">
                                🐄 สัตว์ออโต้: <span id="ui-auto-animal-status" class="text-white">เปิด</span>
                            </button>"""
content = content.replace(old_btn, new_btn)

# 3. Update gameLoop
old_auto_harvest = """            if (state.autoHarvesterActive !== false && (state.autoHarvesterUnlocked || (state.upgrades && state.upgrades.auto_harvester)) && (!state.lastAutoHarvest || now - state.lastAutoHarvest > 2000)) {
                let harvested = false;
                
                // Crop
                state.plots.forEach(p => {
                    if (p.seedId && p.plantedAt) {
                        const seed = SEEDS[p.seedId];
                        let plantSpeedMult = 1;
                        if (state.weather === 'rainy') plantSpeedMult = 2;
                        if (state.weather === 'snowy') plantSpeedMult = 0.5;
                        if (state.upgrades && state.upgrades.greenhouse) {
                            plantSpeedMult *= (1 + (state.upgrades.greenhouse * 0.1));
                        } else if (state.greenhouseUnlocked) {
                            plantSpeedMult *= 1.5;
                        }
                        if (state.achievements && state.achievements.claimed && state.achievements.claimed.includes('a3')) plantSpeedMult *= 1.1;

                        const growTime = seed.growTime / plantSpeedMult;
                        if (now - p.plantedAt >= growTime) {
                            harvestCrop(p.id, true);
                            harvested = true;
                        }
                    }
                });
                
                // Animals
                state.pens.forEach(p => {
                    if (p.animalId && p.lastCollected) {
                        const animal = ANIMALS[p.animalId];
                        let animSpeedMult = 1;
                        if (state.weather === 'sunny') animSpeedMult = 1.2;
                        if (state.weather === 'snowy') animSpeedMult = 0.8;
                        if (state.upgrades && state.upgrades.premium_feed) animSpeedMult *= (1 + (state.upgrades.premium_feed * 0.1));
                        if (state.achievements && state.achievements.claimed && state.achievements.claimed.includes('a4')) animSpeedMult *= 1.1;
                        
                        const timeNeeded = animal.produceTime / animSpeedMult;
                        if (now - p.lastCollected >= timeNeeded) {
                            collectAnimal(p.id, true);
                            harvested = true;
                        }
                    }
                });

                if (harvested) {
                    state.lastAutoHarvest = now;
                    updateUI();
                }
            }"""

new_auto_harvest = """            // Auto Harvest Crop
            if (state.autoHarvesterCropActive !== false && state.upgrades && state.upgrades.auto_harvester_crop && (!state.lastAutoHarvestCrop || now - state.lastAutoHarvestCrop > 2000)) {
                let harvested = false;
                state.plots.forEach(p => {
                    if (p.seedId && p.plantedAt) {
                        const seed = SEEDS[p.seedId];
                        let plantSpeedMult = 1;
                        if (state.weather === 'rainy') plantSpeedMult = 2;
                        if (state.weather === 'snowy') plantSpeedMult = 0.5;
                        if (state.upgrades && state.upgrades.greenhouse) plantSpeedMult *= (1 + (state.upgrades.greenhouse * 0.1));
                        else if (state.greenhouseUnlocked) plantSpeedMult *= 1.5;
                        if (state.achievements && state.achievements.claimed && state.achievements.claimed.includes('a3')) plantSpeedMult *= 1.1;

                        const growTime = seed.growTime / plantSpeedMult;
                        if (now - p.plantedAt >= growTime) {
                            harvestCrop(p.id, true);
                            harvested = true;
                        }
                    }
                });
                if (harvested) {
                    state.lastAutoHarvestCrop = now;
                    updateUI();
                }
            }

            // Auto Harvest Animal
            if (state.autoHarvesterAnimalActive !== false && state.upgrades && state.upgrades.auto_harvester_animal && (!state.lastAutoHarvestAnimal || now - state.lastAutoHarvestAnimal > 2000)) {
                let harvested = false;
                state.pens.forEach(p => {
                    if (p.animalId && p.lastCollected) {
                        const animal = ANIMALS[p.animalId];
                        let animSpeedMult = 1;
                        if (state.weather === 'sunny') animSpeedMult = 1.2;
                        if (state.weather === 'snowy') animSpeedMult = 0.8;
                        if (state.upgrades && state.upgrades.premium_feed) animSpeedMult *= (1 + (state.upgrades.premium_feed * 0.1));
                        if (state.achievements && state.achievements.claimed && state.achievements.claimed.includes('a4')) animSpeedMult *= 1.1;
                        
                        const timeNeeded = animal.produceTime / animSpeedMult;
                        if (now - p.lastCollected >= timeNeeded) {
                            collectAnimal(p.id, true);
                            harvested = true;
                        }
                    }
                });
                if (harvested) {
                    state.lastAutoHarvestAnimal = now;
                    updateUI();
                }
            }"""

content = content.replace(old_auto_harvest, new_auto_harvest)

# 4. Remove auto_harvester migration and fix old state
old_migration = """                    if (state.greenhouseUnlocked && state.upgrades.greenhouse === undefined) state.upgrades.greenhouse = 1;
                    if (state.autoHarvesterUnlocked && state.upgrades.auto_harvester === undefined) state.upgrades.auto_harvester = 1;"""
new_migration = """                    if (state.greenhouseUnlocked && state.upgrades.greenhouse === undefined) state.upgrades.greenhouse = 1;
                    if (state.autoHarvesterUnlocked && state.upgrades.auto_harvester !== undefined) {
                        state.upgrades.auto_harvester_crop = 1;
                        state.upgrades.auto_harvester_animal = 1;
                        delete state.upgrades.auto_harvester;
                    }"""
content = content.replace(old_migration, new_migration)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

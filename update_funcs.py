import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

funcs = """        let isPlantAllMode = false;

        function openPlantAllModal() {
            isPlantAllMode = true;
            currentActivePlotId = null;
            const modal = document.getElementById('modal-seed');
            const grid = document.getElementById('seed-selection-grid');
            
            grid.innerHTML = Object.values(SEEDS).map(seed => {
                const hasQty = state.inventory.seeds[seed.id] || 0;
                const isLocked = state.level < seed.unlockLevel;
                if (isLocked) {
                    return `
                        <div class="flex flex-col items-center p-3 bg-gray-50 border-2 border-gray-100 rounded-[1.5rem] opacity-50 grayscale cursor-not-allowed">
                            <span class="text-3xl mb-1">${seed.emoji}</span>
                            <span class="text-xs font-bold text-gray-600">${seed.name}</span>
                            <span class="text-[10px] text-red-500 mt-1">Lv.${seed.unlockLevel}</span>
                        </div>
                    `;
                }
                
                if (hasQty > 0) {
                    return `
                        <button onclick="plantSeed('${seed.id}')" class="glass p-3 rounded-xl flex flex-col items-center hover:bg-white/50 transition border border-transparent hover:border-white">
                            <span class="text-3xl mb-1 drop-shadow-sm">${seed.emoji}</span>
                            <span class="text-xs font-bold text-green-900">${seed.name}</span>
                            <span class="text-[10px] text-gray-500 font-semibold bg-white/60 px-2 rounded mt-1">มี ${hasQty}</span>
                        </button>
                    `;
                } else {
                    return `
                        <div class="flex flex-col items-center p-3 bg-gray-50 border-2 border-gray-100 rounded-[1.5rem] opacity-50 grayscale cursor-not-allowed">
                            <span class="text-3xl mb-1">${seed.emoji}</span>
                            <span class="text-xs font-bold text-gray-600">${seed.name}</span>
                            <span class="text-[10px] text-gray-400 mt-1">หมด</span>
                        </div>
                    `;
                }
            }).join('');
            
            modal.classList.remove('hidden-scale');
            modal.classList.add('visible-scale');
        }

        function sellAllAnimals() {
            if (!confirm('คุณแน่ใจหรือไม่ว่าต้องการขายสัตว์เลี้ยงทั้งหมดในคอก?')) return;
            let count = 0;
            let totalGold = 0;
            state.pens.forEach(pen => {
                if (pen.unlocked && pen.animalId) {
                    const animal = ANIMALS[pen.animalId];
                    const sellPrice = Math.floor(animal.buyPrice * 0.5);
                    const actualGold = Math.floor(sellPrice * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 2 : 1));
                    totalGold += actualGold;
                    pen.animalId = null;
                    pen.lastCollected = null;
                    pen.happiness = 0;
                    count++;
                }
            });
            if (count > 0) {
                state.gold += totalGold;
                showToast('ขายสัตว์ทั้งหมด', `ขายสัตว์ ${count} ตัว ได้เงิน ${totalGold} 🪙`, '👋');
                updateUI();
            } else {
                showToast('ไม่มีสัตว์', 'ไม่มีสัตว์ในคอกให้ขาย', '❌');
            }
        }

        function openSeedModal(plotId) {"""

content = content.replace("        function openSeedModal(plotId) {", funcs)

# Now modify plantSeed to support plantAll
old_plant_seed = """        function plantSeed(seedId) {
            if (currentActivePlotId === null) return;
            const plot = state.plots[currentActivePlotId];
            if (!plot || !plot.unlocked || plot.seedId) return;
            
            if (state.inventory.seeds[seedId] && state.inventory.seeds[seedId] > 0) {
                state.inventory.seeds[seedId]--;
                plot.seedId = seedId;
                plot.plantedAt = Date.now();
                plot.watered = (state.upgrades && state.upgrades.sprinkler && Math.random() < Math.min(0.5, state.upgrades.sprinkler * 0.005));
                if (plot.watered) {
                    plot.plantedAt -= SEEDS[seedId].growTime * 1000;
                }
                
                closeSeedModal();
                updateUI();
            }
        }"""

new_plant_seed = """        function plantSeed(seedId) {
            if (isPlantAllMode) {
                let plantedCount = 0;
                state.plots.forEach(plot => {
                    if (plot.unlocked && plot.seedId === null && (state.inventory.seeds[seedId] || 0) > 0) {
                        state.inventory.seeds[seedId]--;
                        plot.seedId = seedId;
                        plot.plantedAt = Date.now();
                        plot.watered = (state.upgrades && state.upgrades.sprinkler && Math.random() < Math.min(0.5, state.upgrades.sprinkler * 0.005));
                        if (plot.watered) {
                            plot.plantedAt -= SEEDS[seedId].growTime * 1000;
                        }
                        plantedCount++;
                    }
                });
                closeSeedModal();
                updateUI();
                if (plantedCount > 0) {
                    showToast('ปลูกผักสำเร็จ', `ปลูก ${SEEDS[seedId].name} จำนวน ${plantedCount} ต้น`, '🌱');
                } else {
                    showToast('ไม่สามารถปลูกได้', 'ไม่มีแปลงว่างหรือเมล็ดพันธุ์ไม่พอ', '❌');
                }
                return;
            }

            if (currentActivePlotId === null) return;
            const plot = state.plots[currentActivePlotId];
            if (!plot || !plot.unlocked || plot.seedId) return;
            
            if (state.inventory.seeds[seedId] && state.inventory.seeds[seedId] > 0) {
                state.inventory.seeds[seedId]--;
                plot.seedId = seedId;
                plot.plantedAt = Date.now();
                plot.watered = (state.upgrades && state.upgrades.sprinkler && Math.random() < Math.min(0.5, state.upgrades.sprinkler * 0.005));
                if (plot.watered) {
                    plot.plantedAt -= SEEDS[seedId].growTime * 1000;
                }
                
                closeSeedModal();
                updateUI();
            }
        }"""

content = content.replace(old_plant_seed, new_plant_seed)
print("Funcs updated")

# Ensure isPlantAllMode resets on close
old_close_modal = """        function closeSeedModal() {
            const modal = document.getElementById('modal-seed');
            modal.classList.remove('visible-scale');
            modal.classList.add('hidden-scale');
            currentActivePlotId = null;
        }"""

new_close_modal = """        function closeSeedModal() {
            const modal = document.getElementById('modal-seed');
            modal.classList.remove('visible-scale');
            modal.classList.add('hidden-scale');
            currentActivePlotId = null;
            isPlantAllMode = false;
        }"""

content = content.replace(old_close_modal, new_close_modal)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


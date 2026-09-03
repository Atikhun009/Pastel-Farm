import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: plantSeed replacement
pattern = r"function plantSeed\(seedId\) \{[\s\S]*?function fertilize\(plotId, event\) \{"
new_plant = """function plantSeed(seedId) {
            if (isPlantAllMode) {
                let plantedCount = 0;
                state.plots.forEach(plot => {
                    if (plot.unlocked && plot.seedId === null && (state.inventory.seeds[seedId] || 0) > 0) {
                        state.inventory.seeds[seedId]--;
                        plot.seedId = seedId;
                        
                        let plantedTime = Date.now();
                        if (state.upgrades && state.upgrades.sprinkler) {
                            const chance = state.upgrades.sprinkler * 0.005;
                            if (Math.random() < chance) {
                                plantedTime -= SEEDS[seedId].growTime * 1000 * 2;
                            }
                        }
                        plot.plantedAt = plantedTime;
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
            if (state.inventory.seeds[seedId] > 0) {
                state.inventory.seeds[seedId]--;
                const plot = state.plots.find(p => p.id === currentActivePlotId);
                plot.seedId = seedId;
                
                let plantedTime = Date.now();
                if (state.upgrades && state.upgrades.sprinkler) {
                    const chance = state.upgrades.sprinkler * 0.005;
                    if (Math.random() < chance) {
                        plantedTime -= SEEDS[seedId].growTime * 1000 * 2;
                        showToast('สปริงเกอร์ทำงาน!', 'เมล็ดพันธุ์โตเต็มที่ทันที!', '💦');
                    }
                }
                
                plot.plantedAt = plantedTime;
                updateUI();
                closeSeedModal();
            }
        }

        function fertilize(plotId, event) {"""

content, count = re.subn(pattern, new_plant, content)
print(f"plantSeed replaced {count} times")

# Fix 2: sellAllAnimals - remove window.confirm
sell_all_pattern = r"function sellAllAnimals\(\) \{[\s\S]*?if \(\!confirm\('คุณแน่ใจหรือไม่ว่าต้องการขายสัตว์เลี้ยงทั้งหมดในคอก\?'\)\) return;"
new_sell_all = """function sellAllAnimals() {"""

content, count2 = re.subn(sell_all_pattern, new_sell_all, content)
print(f"sellAllAnimals replaced {count2} times")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

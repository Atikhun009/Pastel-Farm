import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update plantSpeedMult
plant_speed_old = """            let plantSpeedMult = 1;
            if (state.weather === 'rainy') plantSpeedMult = 2;
            if (state.weather === 'snowy') plantSpeedMult = 0.5;"""
plant_speed_new = """            let plantSpeedMult = 1;
            if (state.weather === 'rainy') plantSpeedMult = 2;
            if (state.weather === 'snowy') plantSpeedMult = 0.5;
            if (state.activeBuffs && state.activeBuffs.cropSpeedEnd && Date.now() < state.activeBuffs.cropSpeedEnd) {
                plantSpeedMult *= 2;
            }"""
content = content.replace(plant_speed_old, plant_speed_new)

# 2. Update gold adding places
# 2065: NPC orders
# state.gold += order.goldReward;
order_gold_old = "state.gold += order.goldReward;"
order_gold_new = "state.gold += Math.floor(order.goldReward * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 1.5 : 1));"
content = content.replace(order_gold_old, order_gold_new)

# 2194: sellSeed
sell_seed_old = "state.gold += totalValue;"
sell_seed_new = "state.gold += Math.floor(totalValue * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 1.5 : 1));"
content = content.replace(sell_seed_old, sell_seed_new)

# 2229: sellAllInventory
# Wait, let's see how finalValue is defined
sell_all_old = "state.gold += finalValue;"
sell_all_new = "state.gold += Math.floor(finalValue * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 1.5 : 1));"
content = content.replace(sell_all_old, sell_all_new)

# 2907: executeSell
sell_exec_old = "state.gold += total;"
sell_exec_new = "state.gold += Math.floor(total * (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd ? 1.5 : 1));"
content = content.replace(sell_exec_old, sell_exec_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

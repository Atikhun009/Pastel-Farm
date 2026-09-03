import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_barn = """        const BARN_UPGRADES = [
            { level: 1, capacity: 1700, reqGold: 0, reqItems: {} },
            { level: 2, capacity: 4000, reqGold: 100000, reqItems: { wheat: 500, corn: 300, potato: 390 } },
            { level: 3, capacity: 10000, reqGold: 500000, reqItems: { tomato: 1000, onion: 1000, egg: 800 } },
            { level: 4, capacity: 25000, reqGold: 2000000, reqItems: { strawberry: 3000, milk: 1500, bread: 500, cabbage: 2000 } },
            { level: 5, capacity: 60000, reqGold: 8000000, reqItems: { watermelon: 6000, goat_milk: 3000, cake: 2500, pumpkin: 6000 } },
            { level: 6, capacity: 150000, reqGold: 25000000, reqItems: { rose: 15000, apple: 10000, pizza: 7000, honey: 10000 } },
            { level: 7, capacity: 350000, reqGold: 80000000, reqItems: { peach: 35000, truffle: 20000, goat_cheese: 25000, omelet: 25000 } },
            { level: 8, capacity: 800000, reqGold: 250000000, reqItems: { tulip: 80000, coconut: 60000, peacock_feather: 25000, honey_toast: 80000 } },
            { level: 9, capacity: 2000000, reqGold: 800000000, reqItems: { mango: 200000, buffalo_milk: 100000, llama_wool: 60000, pineapple_fried_rice: 200000 } },
            { level: 10, capacity: 9999999, reqGold: 2500000000, reqItems: { truffle: 300000, owl_feather: 200000, alpaca_wool: 300000, melon_pan: 300000, squid_ink: 300000 } }
        ];"""

new_barn = """        const BARN_UPGRADES = [
            { level: 1, capacity: 1700, reqGold: 0, reqItems: {} },
            { level: 2, capacity: 4000, reqGold: 100000, reqItems: { wheat: 50, corn: 30, potato: 39 } },
            { level: 3, capacity: 10000, reqGold: 500000, reqItems: { tomato: 100, onion: 100, egg: 80 } },
            { level: 4, capacity: 25000, reqGold: 2000000, reqItems: { strawberry: 300, milk: 150, bread: 50, cabbage: 200 } },
            { level: 5, capacity: 60000, reqGold: 8000000, reqItems: { watermelon: 600, goat_milk: 300, cake: 250, pumpkin: 600 } },
            { level: 6, capacity: 150000, reqGold: 25000000, reqItems: { rose: 1500, apple: 1000, pizza: 700, honey: 1000 } },
            { level: 7, capacity: 350000, reqGold: 80000000, reqItems: { peach: 3500, truffle: 2000, goat_cheese: 2500, omelet: 2500 } },
            { level: 8, capacity: 800000, reqGold: 250000000, reqItems: { tulip: 8000, coconut: 6000, peacock_feather: 2500, honey_toast: 8000 } },
            { level: 9, capacity: 2000000, reqGold: 800000000, reqItems: { mango: 20000, buffalo_milk: 10000, llama_wool: 6000, pineapple_fried_rice: 20000 } },
            { level: 10, capacity: 9999999, reqGold: 2500000000, reqItems: { truffle: 30000, owl_feather: 20000, alpaca_wool: 30000, melon_pan: 30000, squid_ink: 30000 } }
        ];"""

if old_barn in content:
    content = content.replace(old_barn, new_barn)
    print("Barn upgrades updated successfully.")
else:
    print("Barn upgrades pattern not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

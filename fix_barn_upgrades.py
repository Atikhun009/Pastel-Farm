import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_barn = """                const BARN_UPGRADES = [
            { level: 1, capacity: 100, reqGold: 0, reqItems: {} },
            { level: 2, capacity: 250, reqGold: 100000, reqItems: { wheat: 500, corn: 300, potato: 500 } },
            { level: 3, capacity: 600, reqGold: 500000, reqItems: { tomato: 1000, onion: 1000, egg: 300 } },
            { level: 4, capacity: 1500, reqGold: 2000000, reqItems: { strawberry: 2000, milk: 800, bread: 300, cabbage: 1000 } },
            { level: 5, capacity: 4000, reqGold: 8000000, reqItems: { watermelon: 3000, goat_milk: 1000, cake: 300, pumpkin: 1500 } },
            { level: 6, capacity: 10000, reqGold: 25000000, reqItems: { rose: 3000, apple: 2000, pizza: 500, honey: 1000 } },
            { level: 7, capacity: 25000, reqGold: 80000000, reqItems: { peach: 4000, truffle: 1000, goat_cheese: 800, omelet: 1000 } },
            { level: 8, capacity: 60000, reqGold: 250000000, reqItems: { tulip: 5000, coconut: 3000, peacock_feather: 800, honey_toast: 1000 } },
            { level: 9, capacity: 150000, reqGold: 800000000, reqItems: { mango: 8000, buffalo_milk: 3000, llama_wool: 1000, pineapple_fried_rice: 1500 } },
            { level: 10, capacity: 999999, reqGold: 2500000000, reqItems: { truffle: 3000, owl_feather: 2000, alpaca_wool: 1500, melon_pan: 2000, squid_ink: 2000 } }
        ];"""

new_barn = """                const BARN_UPGRADES = [
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

content = content.replace(old_barn, new_barn)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

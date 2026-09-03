import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_req = """            { level: 8, capacity: 60000, reqGold: 250000000, reqItems: { tulip: 5000, coconut: 3000, golden_egg: 800, honey_toast: 1000 } },
            { level: 9, capacity: 150000, reqGold: 800000000, reqItems: { mango: 8000, turkey_egg: 3000, llama_wool: 1000, pineapple_fried_rice: 1500 } },
            { level: 10, capacity: 999999, reqGold: 2500000000, reqItems: { truffle: 3000, golden_egg: 2000, alpaca_wool: 1500, melon_pan: 2000, cake: 2000 } }"""

new_req = """            { level: 8, capacity: 60000, reqGold: 250000000, reqItems: { tulip: 5000, coconut: 3000, peacock_feather: 800, honey_toast: 1000 } },
            { level: 9, capacity: 150000, reqGold: 800000000, reqItems: { mango: 8000, buffalo_milk: 3000, llama_wool: 1000, pineapple_fried_rice: 1500 } },
            { level: 10, capacity: 999999, reqGold: 2500000000, reqItems: { truffle: 3000, owl_feather: 2000, alpaca_wool: 1500, melon_pan: 2000, squid_ink: 2000 } }"""

content = content.replace(old_req, new_req)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

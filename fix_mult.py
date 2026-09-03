import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

patterns = [
    (r'state\.upgrades\.speedy_boots \* 0\.\d+', r'state.upgrades.speedy_boots * 0.005'),
    (r'state\.upgrades\.bulk_buyer \* 0\.\d+', r'state.upgrades.bulk_buyer * 0.005'),
    (r'state\.upgrades\.upgrade_discount \* 0\.\d+', r'state.upgrades.upgrade_discount * 0.005'),
    (r'state\.upgrades\.greenhouse \* 0\.\d+', r'state.upgrades.greenhouse * 0.005'),
    (r'state\.upgrades\.premium_feed \* 0\.\d+', r'state.upgrades.premium_feed * 0.005'),
    (r'state\.upgrades\.golden_hoe \* 0\.\d+', r'state.upgrades.golden_hoe * 0.005'),
    (r'state\.upgrades\.lucky_charm \* 0\.\d+', r'state.upgrades.lucky_charm * 0.005'),
    (r'state\.upgrades\.sprinkler \* 0\.\d+', r'state.upgrades.sprinkler * 0.005'),
    (r'state\.upgrades\.magic_beans \* 0\.\d+', r'state.upgrades.magic_beans * 0.005'),
    (r'state\.upgrades\.lucky_hand \* 0\.\d+', r'state.upgrades.lucky_hand * 0.005'),
    (r'state\.upgrades\.animal_breeder \* 0\.\d+', r'state.upgrades.animal_breeder * 0.005'),
    (r'state\.upgrades\.master_chef \* 0\.\d+', r'state.upgrades.master_chef * 0.005'),
    (r'state\.upgrades\.sales_license \* 0\.\d+', r'state.upgrades.sales_license * 0.005'),
]

for pat, repl in patterns:
    content = re.sub(pat, repl, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

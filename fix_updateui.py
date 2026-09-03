import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_gold = """            document.getElementById('ui-gold').innerText = state.gold;"""

new_gold = """            document.getElementById('ui-gold').innerText = state.gold;
            const uiDiamond = document.getElementById('ui-diamond');
            if (uiDiamond) uiDiamond.innerText = state.diamonds || 0;
            const diamondGoldReward = document.getElementById('diamond-gold-reward');
            if (diamondGoldReward) diamondGoldReward.innerText = state.level * 1000;"""

content = content.replace(old_gold, new_gold)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

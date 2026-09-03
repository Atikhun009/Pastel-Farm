import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the seed button disabled logic
bad_disabled = r"\$\{isLocked \|\| state\.gold < \(state\.upgrades\.storage_box \? Math\.floor\(seed\.buyPrice \* \(1 - \(state\.upgrades\.storage_box \* 0\.05\)\)\) : seed\.buyPrice\) \* quickBuyAmount \? 'disabled' : ''\}"
good_disabled = r"${isLocked || state.gold < finalPrice * quickBuyAmount ? 'disabled' : ''}"
content = re.sub(bad_disabled, good_disabled, content)

# Fix the seed button price text
bad_price_text = r"\$\{\(state\.upgrades\.storage_box \? Math\.floor\(seed\.buyPrice \* \(1 - \(state\.upgrades\.storage_box \* 0\.05\)\)\) : seed\.buyPrice\) \* quickBuyAmount\} 🪙"
good_price_text = r"<span class=\"${trendColor} mr-1 text-[10px]\">${trendIcon}</span> ${finalPrice * quickBuyAmount} 🪙"
content = re.sub(bad_price_text, good_price_text, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

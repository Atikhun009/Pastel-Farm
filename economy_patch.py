import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update plot and pen prices calculation
# Use exponential scaling
plot_price_old = r"let plotPrice = \(unlockedPlots - 2\) \* PLOT_BASE_PRICE;"
plot_price_new = r"let plotPrice = Math.floor(PLOT_BASE_PRICE * Math.pow(1.5, unlockedPlots - 3));"
content = re.sub(plot_price_old, plot_price_new, content)

buy_plot_old = r"let price = \(unlockedCount - 2\) \* PLOT_BASE_PRICE;"
buy_plot_new = r"let price = Math.floor(PLOT_BASE_PRICE * Math.pow(1.5, unlockedCount - 3));"
content = re.sub(buy_plot_old, buy_plot_new, content)

pen_price_old = r"let penPrice = \(unlockedPens - 1\) \* PEN_BASE_PRICE;"
pen_price_new = r"let penPrice = Math.floor(PEN_BASE_PRICE * Math.pow(1.5, unlockedPens - 2));"
content = re.sub(pen_price_old, pen_price_new, content)

buy_pen_old = r"let price = \(unlockedCount - 1\) \* PEN_BASE_PRICE;"
buy_pen_new = r"let price = Math.floor(PEN_BASE_PRICE * Math.pow(1.5, unlockedCount - 2));"
content = re.sub(buy_pen_old, buy_pen_new, content)

# 2. Adjust PRODUCTS base prices to be less profitable
products_block_pattern = r"(const PRODUCTS = \{)([\s\S]*?)(\n\s*\};)"
def repl_products(m):
    block = m.group(2)
    # Match each basePrice value
    def repl_price(pm):
        name = pm.group(1)
        val = int(pm.group(2))
        
        # New base price logic: cut by ~30-50%
        # For base crops, make sure it's not lower than seed
        seed_prices = {
            'carrot': 10, 'tomato': 20, 'wheat': 15, 'corn': 35, 'watermelon': 50, 'strawberry': 80,
            'potato': 15, 'onion': 20, 'cabbage': 25, 'pumpkin': 40, 'eggplant': 35, 'chili': 50,
            'blueberry': 60, 'grape': 80, 'melon': 100, 'pineapple': 120
        }
        
        new_val = val
        if name in seed_prices:
            new_val = int(seed_prices[name] * 1.3) # 30% profit
        else:
            new_val = int(val * 0.6) # 40% cut for animal products and cooked foods
            
        return f"{name}: {new_val}"
    
    new_block = re.sub(r"basePrice:\s*(\d+)", lambda pm: "basePrice: " + str(
        int(int(pm.group(1)) * 0.5) if int(pm.group(1)) > 10 else int(pm.group(1))
    ), block)
    
    # Actually let's use a more custom replacement string approach.
    return m.group(1) + new_block + m.group(3)

# Instead of complex regex for products, I'll just string replace the known ones.

import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update randomizeMarket to include multipliers for shop items
old_randomize = r"function randomizeMarket\(\) \{[\s\S]*?updateUI\(\); // Refresh views\s*\}"
new_randomize = """function randomizeMarket() {
            Object.keys(PRODUCTS).forEach(key => {
                state.marketMultipliers[key] = parseFloat((Math.random() * (1.4 - 0.8) + 0.8).toFixed(2));
            });
            Object.keys(SEEDS).forEach(key => {
                state.marketMultipliers['seed_'+key] = parseFloat((Math.random() * (1.5 - 0.7) + 0.7).toFixed(2));
            });
            Object.keys(ANIMALS).forEach(key => {
                state.marketMultipliers['animal_'+key] = parseFloat((Math.random() * (1.5 - 0.7) + 0.7).toFixed(2));
            });
            Object.keys(RECIPES).forEach(key => {
                state.marketMultipliers['recipe_'+key] = parseFloat((Math.random() * (1.5 - 0.7) + 0.7).toFixed(2));
            });
            state.lastMarketUpdate = Date.now();
            updateUI(); // Refresh views
        }"""
content = re.sub(old_randomize, new_randomize, content)

# 2. Update renderMarket to apply multipliers
# Replace SEED price parsing
old_seed_render = r"const isLocked = state\.level < seed\.unlockLevel;"
new_seed_render = """const isLocked = state.level < seed.unlockLevel;
                const mult = state.marketMultipliers['seed_'+seed.id] || 1.0;
                const dynamicPrice = Math.floor(seed.buyPrice * mult);
                let trendIcon = '➖'; let trendColor = 'text-gray-500';
                if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-red-500'; } // red for expensive to buy
                else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-green-600'; } // green for cheap to buy
                const finalPrice = state.upgrades.storage_box ? Math.floor(dynamicPrice * (1 - (state.upgrades.storage_box * 0.05))) : dynamicPrice;
"""
content = content.replace(old_seed_render, new_seed_render)

old_seed_btn = r"(<button onclick=\"buyItem\('seed', '\$\{seed\.id\}', )\$\{seed\.buyPrice\}(\)\".*?\$\{isLocked \|\| state\.gold < )(\(state\.upgrades\.storage_box \? Math\.floor\(seed\.buyPrice \* \(1 - \(state\.upgrades\.storage_box \* 0\.05\)\)\) : seed\.buyPrice\))"
new_seed_btn = r"\1${dynamicPrice}\2finalPrice"
content = re.sub(old_seed_btn, new_seed_btn, content)

old_seed_btn_disabled = r"(disabled' : 'text-green-700 bg-white/80 hover:bg-green-50'\}\" \$\{isLocked \|\| state\.gold < )(\(state\.upgrades\.storage_box \? Math\.floor\(seed\.buyPrice \* \(1 - \(state\.upgrades\.storage_box \* 0\.05\)\)\) : seed\.buyPrice\))"
new_seed_btn_disabled = r"\1finalPrice"
content = re.sub(old_seed_btn_disabled, new_seed_btn_disabled, content)

old_seed_btn_price = r"(\s+)\$\{\(state\.upgrades\.storage_box \? Math\.floor\(seed\.buyPrice \* \(1 - \(state\.upgrades\.storage_box \* 0\.05\)\)\) : seed\.buyPrice\)\} \* quickBuyAmount\} 🪙"
new_seed_btn_price = r"\1<span class=\"${trendColor} mr-1 text-[10px]\">${trendIcon}</span> ${finalPrice * quickBuyAmount} 🪙"
content = re.sub(old_seed_btn_price, new_seed_btn_price, content)

# Replace ANIMAL price parsing
old_animal_render = r"const isLocked = state\.level < animal\.unlockLevel;"
new_animal_render = """const isLocked = state.level < animal.unlockLevel;
                const mult = state.marketMultipliers['animal_'+animal.id] || 1.0;
                const dynamicPrice = Math.floor(animal.buyPrice * mult);
                let trendIcon = '➖'; let trendColor = 'text-gray-500';
                if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-red-500'; } 
                else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-green-600'; }
"""
content = content.replace(old_animal_render, new_animal_render)

old_animal_btn = r"(<button onclick=\"buyItem\('animal', '\$\{animal\.id\}', )\$\{animal\.buyPrice\}(\)\".*?>\s+)\$\{animal\.buyPrice\} 🪙"
new_animal_btn = r"\1${dynamicPrice}\2<span class=\"${trendColor} mr-1 text-[10px]\">${trendIcon}</span> ${dynamicPrice} 🪙"
content = re.sub(old_animal_btn, new_animal_btn, content)

# Replace RECIPE price parsing
old_recipe_render = r"const isLocked = state\.level < recipe\.unlockLevel;"
new_recipe_render = """const isLocked = state.level < recipe.unlockLevel;
                    const mult = state.marketMultipliers['recipe_'+recipe.id] || 1.0;
                    const dynamicPrice = Math.floor(recipe.shopPrice * mult);
                    let trendIcon = '➖'; let trendColor = 'text-gray-500';
                    if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-red-500'; } 
                    else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-green-600'; }
"""
content = content.replace(old_recipe_render, new_recipe_render)

old_recipe_btn = r"(<button onclick=\"buyItem\('recipe', '\$\{recipe\.id\}', )\$\{recipe\.shopPrice\}(\)\".*?>\s+)\$\{recipe\.shopPrice\} 🪙"
new_recipe_btn = r"\1${dynamicPrice}\2<span class=\"${trendColor} mr-1 text-[10px]\">${trendIcon}</span> ${dynamicPrice} 🪙"
content = re.sub(old_recipe_btn, new_recipe_btn, content)

# Also RECIPES should filter by season!
old_recipe_loop = r"Object\.values\(RECIPES\)\.forEach\(recipe => \{"
new_recipe_loop = r"Object.values(RECIPES).filter(recipe => !recipe.season || recipe.season === state.season).forEach(recipe => {"
content = re.sub(old_recipe_loop, new_recipe_loop, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


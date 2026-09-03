import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix seed parsing
seed_target = r"const isLocked = state\.level < seed\.unlockLevel;\s+return `"
seed_replacement = """const isLocked = state.level < seed.unlockLevel;
                const mult = state.marketMultipliers['seed_'+seed.id] || 1.0;
                const dynamicPrice = Math.floor(seed.buyPrice * mult);
                let trendIcon = '➖'; let trendColor = 'text-gray-500';
                if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-red-500'; } 
                else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-green-600'; }
                const finalPrice = state.upgrades.storage_box ? Math.floor(dynamicPrice * (1 - (state.upgrades.storage_box * 0.05))) : dynamicPrice;
                return `"""
content = re.sub(seed_target, seed_replacement, content)

# Fix animal parsing
animal_target = r"const isLocked = state\.level < animal\.unlockLevel;\s+return `"
animal_replacement = """const isLocked = state.level < animal.unlockLevel;
                const mult = state.marketMultipliers['animal_'+animal.id] || 1.0;
                const dynamicPrice = Math.floor(animal.buyPrice * mult);
                let trendIcon = '➖'; let trendColor = 'text-gray-500';
                if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-red-500'; } 
                else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-green-600'; }
                return `"""
content = re.sub(animal_target, animal_replacement, content)

# Fix recipe parsing
recipe_target = r"const isLocked = state\.level < recipe\.unlockLevel;\s+recipesHtml \+= `"
recipe_replacement = """const isLocked = state.level < recipe.unlockLevel;
                    const mult = state.marketMultipliers['recipe_'+recipe.id] || 1.0;
                    const dynamicPrice = Math.floor(recipe.shopPrice * mult);
                    let trendIcon = '➖'; let trendColor = 'text-gray-500';
                    if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-red-500'; } 
                    else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-green-600'; }
                    recipesHtml += `"""
content = re.sub(recipe_target, recipe_replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


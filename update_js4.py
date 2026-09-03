import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"function cookRecipe\(recipeId\) \{[\s\S]*?if \(qty < 1\) return;"
new_cook_recipe = """function cookRecipe(recipeId) {
            const recipe = RECIPES[recipeId];
            if (!recipe) return;
            const qty = quickCookAmount;
            if (qty < 1) return;"""

content, count = re.subn(pattern, new_cook_recipe, content, count=1)
print(f"cookRecipe updated: {count} times")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

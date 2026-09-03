import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 4. Update cookRecipe function to use quickCookAmount
pattern = r"""        function cookRecipe\(recipeId\) \{
            const recipe = RECIPES\[recipeId\];
            if \(\!recipe\) return;
            const qtyInput = document\.getElementById\(`qty-\$\{recipeId\}`\);
            const qty = parseInt\(qtyInput \? qtyInput\.value : 1\) \|\| 1;
            if \(qty < 1\) return;"""

new_cook_recipe = """        function cookRecipe(recipeId) {
            const recipe = RECIPES[recipeId];
            if (!recipe) return;
            const qty = quickCookAmount;
            if (qty < 1) return;"""

content, count = re.subn(pattern, new_cook_recipe, content)
print(f"cookRecipe updated: {count} times")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

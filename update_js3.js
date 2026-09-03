const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf-8');

html = html.replace(/function cookRecipe\(recipeId\) {[\s\S]*?if \(qty < 1\) return;/, `function cookRecipe(recipeId) {
            const recipe = RECIPES[recipeId];
            if (!recipe) return;
            const qty = quickCookAmount;
            if (qty < 1) return;`);

fs.writeFileSync('index.html', html);

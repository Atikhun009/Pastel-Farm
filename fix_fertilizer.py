import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix buyItem to read qty from input if type is fertilizer
old_buyItem = """        function buyItem(type, id, price) {
            let qty = quickBuyAmount;
            if (type === 'animal' || type === 'recipe') {
                qty = 1;
            }"""
new_buyItem = """        function buyItem(type, id, price) {
            let qty = quickBuyAmount;
            if (type === 'animal' || type === 'recipe') {
                qty = 1;
            } else if (type === 'fertilizer') {
                const qtyInput = document.getElementById('buy-qty-fertilizer');
                qty = parseInt(qtyInput ? qtyInput.value : 1) || 1;
            }"""
content = content.replace(old_buyItem, new_buyItem)

# Also fix the use fertilizer logic, make sure there is a button to use it.
# Let's check how fertilize() is called.

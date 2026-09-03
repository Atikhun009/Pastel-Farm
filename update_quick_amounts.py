import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add x1000 to market quick buy
old_market_qb = """                                <button onclick="setQuickBuy(1)" id="qb-1" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-green-500 text-white shadow">x1</button>
                                <button onclick="setQuickBuy(10)" id="qb-10" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x10</button>
                                <button onclick="setQuickBuy(100)" id="qb-100" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x100</button>"""
new_market_qb = """                                <button onclick="setQuickBuy(1)" id="qb-1" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-green-500 text-white shadow">x1</button>
                                <button onclick="setQuickBuy(10)" id="qb-10" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x10</button>
                                <button onclick="setQuickBuy(100)" id="qb-100" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x100</button>
                                <button onclick="setQuickBuy(1000)" id="qb-1000" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x1000</button>"""

if old_market_qb in content:
    content = content.replace(old_market_qb, new_market_qb)
    print("Market QB updated")
else:
    print("Market QB NOT FOUND")

# 2. Add quick cook buttons in cooking tab
old_cooking_header = """                        <div class="bg-blue-50/80 rounded-xl p-3 mb-4 text-xs font-semibold text-blue-800 border border-blue-200">
                            👨‍🍳 นำผลผลิตมาทำอาหารเพื่อขายได้ราคาที่สูงกว่าและได้ XP เพิ่ม!
                        </div>
                        <div id="cooking-recipes" class="space-y-3"></div>"""
new_cooking_header = """                        <div class="bg-blue-50/80 rounded-xl p-3 mb-4 text-xs font-semibold text-blue-800 border border-blue-200">
                            👨‍🍳 นำผลผลิตมาทำอาหารเพื่อขายได้ราคาที่สูงกว่าและได้ XP เพิ่ม!
                        </div>
                        <div id="quick-cook-container" class="flex items-center justify-between bg-white/40 p-2 rounded-xl mb-4">
                            <span class="text-sm font-bold text-blue-900">ทำจำนวน:</span>
                            <div class="flex gap-1">
                                <button onclick="setQuickCook(1)" id="qc-1" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-blue-500 text-white shadow">x1</button>
                                <button onclick="setQuickCook(10)" id="qc-10" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x10</button>
                                <button onclick="setQuickCook(100)" id="qc-100" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x100</button>
                                <button onclick="setQuickCook(1000)" id="qc-1000" class="px-3 py-1 text-xs font-bold rounded-lg transition-all bg-gray-100 text-gray-500 hover:bg-gray-200">x1000</button>
                            </div>
                        </div>
                        <div id="cooking-recipes" class="space-y-3"></div>"""

if old_cooking_header in content:
    content = content.replace(old_cooking_header, new_cooking_header)
    print("Cooking header updated")
else:
    print("Cooking header NOT FOUND")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


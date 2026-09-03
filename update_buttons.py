import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Plant All Button
old_plant_header = """                        <div class="flex items-center gap-2 flex-wrap">
                            <h2 class="text-xl font-bold text-green-900 flex items-center gap-1 mr-2">
                                <span class="text-2xl">🌱</span> แปลงเพาะปลูก
                            </h2>
                            <button id="btn-toggle-auto-crop" onclick="toggleAutoHarvesterCrop()" class="hidden text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600">
                                🚜 พืชออโต้: <span id="ui-auto-crop-status" class="text-white">เปิด</span>
                            </button>"""

new_plant_header = """                        <div class="flex items-center gap-2 flex-wrap">
                            <h2 class="text-xl font-bold text-green-900 flex items-center gap-1 mr-2">
                                <span class="text-2xl">🌱</span> แปลงเพาะปลูก
                            </h2>
                            <button id="btn-plant-all" onclick="openPlantAllModal()" class="text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-blue-500 text-white hover:bg-blue-600">
                                🌱 ปลูกทั้งหมด
                            </button>
                            <button id="btn-toggle-auto-crop" onclick="toggleAutoHarvesterCrop()" class="hidden text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600">
                                🚜 พืชออโต้: <span id="ui-auto-crop-status" class="text-white">เปิด</span>
                            </button>"""

if old_plant_header in content:
    content = content.replace(old_plant_header, new_plant_header)
    print("Plant all button added")

# 2. Add Sell All Animals Button
old_animal_header = """                    <div class="flex justify-between items-center mb-5">
                        <h2 class="text-xl font-bold text-green-900 flex items-center gap-2">
                            <span class="text-2xl">🐄</span> ฟาร์มสัตว์
                        </h2>
                        <button id="btn-buy-pen" onclick="buyPen()" class="glass-btn px-4 py-2 rounded-xl text-sm font-bold text-green-800 shadow-sm flex items-center gap-2">
                            <span>+ เพิ่มคอก</span>
                            <span class="bg-green-100 text-green-900 px-2 py-0.5 rounded-md"><span id="ui-pen-price">200</span> 🪙</span>
                        </button>
                    </div>"""

new_animal_header = """                    <div class="flex justify-between items-center mb-5 flex-wrap gap-2">
                        <h2 class="text-xl font-bold text-green-900 flex items-center gap-2">
                            <span class="text-2xl">🐄</span> ฟาร์มสัตว์
                        </h2>
                        <div class="flex items-center gap-2">
                            <button id="btn-sell-all-animals" onclick="sellAllAnimals()" class="glass-btn px-3 py-1.5 rounded-xl text-xs font-bold text-red-700 bg-red-100 hover:bg-red-200 shadow-sm transition">
                                👋 ขายสัตว์ทั้งหมด
                            </button>
                            <button id="btn-buy-pen" onclick="buyPen()" class="glass-btn px-4 py-2 rounded-xl text-sm font-bold text-green-800 shadow-sm flex items-center gap-2">
                                <span>+ เพิ่มคอก</span>
                                <span class="bg-green-100 text-green-900 px-2 py-0.5 rounded-md"><span id="ui-pen-price">200</span> 🪙</span>
                            </button>
                        </div>
                    </div>"""

if old_animal_header in content:
    content = content.replace(old_animal_header, new_animal_header)
    print("Sell all animals button added")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

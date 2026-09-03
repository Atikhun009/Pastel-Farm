import re
import json

crops = [
    # Spring
    {"id": "tulip", "name": "ทิวลิป", "emoji": "🌷", "buyPrice": 180, "growTime": 120, "xp": 90, "basePrice": 300, "season": "spring"},
    {"id": "rose", "name": "กุหลาบ", "emoji": "🌹", "buyPrice": 200, "growTime": 150, "xp": 100, "basePrice": 350, "season": "spring"},
    {"id": "daisy", "name": "เดซี่", "emoji": "🌼", "buyPrice": 150, "growTime": 100, "xp": 75, "basePrice": 250, "season": "spring"},
    {"id": "cucumber", "name": "แตงกวา", "emoji": "🥒", "buyPrice": 70, "growTime": 65, "xp": 40, "basePrice": 120, "season": "spring"},
    # Summer
    {"id": "mango", "name": "มะม่วง", "emoji": "🥭", "buyPrice": 180, "growTime": 150, "xp": 90, "basePrice": 300, "season": "summer"},
    {"id": "coconut", "name": "มะพร้าว", "emoji": "🥥", "buyPrice": 250, "growTime": 200, "xp": 120, "basePrice": 400, "season": "summer"},
    {"id": "papaya", "name": "มะละกอ", "emoji": "🍈", "buyPrice": 130, "growTime": 110, "xp": 60, "basePrice": 220, "season": "summer"},
    {"id": "lime", "name": "มะนาว", "emoji": "🍋", "buyPrice": 90, "growTime": 80, "xp": 45, "basePrice": 150, "season": "summer"},
    # Autumn
    {"id": "sweet_potato", "name": "มันเทศ", "emoji": "🍠", "buyPrice": 120, "growTime": 95, "xp": 60, "basePrice": 200, "season": "autumn"},
    {"id": "mushroom", "name": "เห็ด", "emoji": "🍄", "buyPrice": 80, "growTime": 70, "xp": 45, "basePrice": 140, "season": "autumn"},
    {"id": "apple", "name": "แอปเปิ้ล", "emoji": "🍎", "buyPrice": 220, "growTime": 180, "xp": 110, "basePrice": 380, "season": "autumn"},
    {"id": "chestnut", "name": "เกาลัด", "emoji": "🌰", "buyPrice": 160, "growTime": 140, "xp": 85, "basePrice": 280, "season": "autumn"},
    # Winter
    {"id": "broccoli", "name": "บรอกโคลี", "emoji": "🥦", "buyPrice": 140, "growTime": 110, "xp": 70, "basePrice": 240, "season": "winter"},
    {"id": "pear", "name": "ลูกแพร์", "emoji": "🍐", "buyPrice": 190, "growTime": 160, "xp": 95, "basePrice": 320, "season": "winter"},
    {"id": "peach", "name": "ลูกพีช", "emoji": "🍑", "buyPrice": 240, "growTime": 190, "xp": 120, "basePrice": 420, "season": "winter"}
]

seeds_js = ""
products_js = ""
for c in crops:
    seeds_js += f"            {c['id']}: {{ id: '{c['id']}', name: '{c['name']}', emoji: '{c['emoji']}', buyPrice: {c['buyPrice']}, growTime: {c['growTime']}, xp: {c['xp']}, produces: '{c['id']}', unlockLevel: 2, season: '{c['season']}' }},\n"
    products_js += f"            {c['id']}: {{ id: '{c['id']}', name: '{c['name']}', emoji: '{c['emoji']}', basePrice: {c['basePrice']} }},\n"

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert seeds
content = content.replace("const SEEDS = {", "const SEEDS = {\n" + seeds_js)
# Insert products
content = content.replace("const PRODUCTS = {", "const PRODUCTS = {\n" + products_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


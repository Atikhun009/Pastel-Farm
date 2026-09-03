import re

seasons = {
    "spring": {
        "crops": ["tulip", "rose", "daisy", "cucumber"],
        "names": ["ทิวลิป", "กุหลาบ", "เดซี่", "แตงกวา"],
        "emojis": ["🌷", "🌹", "🌼", "🥒"]
    },
    "summer": {
        "crops": ["mango", "coconut", "papaya", "lime"],
        "names": ["มะม่วง", "มะพร้าว", "มะละกอ", "มะนาว"],
        "emojis": ["🥭", "🥥", "🍈", "🍋"]
    },
    "autumn": {
        "crops": ["sweet_potato", "mushroom", "apple", "chestnut"],
        "names": ["มันเทศ", "เห็ด", "แอปเปิ้ล", "เกาลัด"],
        "emojis": ["🍠", "🍄", "🍎", "🌰"]
    },
    "winter": {
        "crops": ["broccoli", "pear", "peach", "snowdrop"], # reuse snowdrop if needed, wait we have 3 crops + maybe carrot?
        "names": ["บรอกโคลี", "แพร์", "พีช", "สโนว์ดรอป"], # I didn't add snowdrop in the new list, but it exists as a product!
        "emojis": ["🥦", "🍐", "🍑", "🌼"]
    }
}

prefixes = [
    ("ชา{0}", "🍵", ["honey"]),
    ("เค้ก{0}", "🍰", ["wheat", "milk"]),
    ("คุกกี้{0}", "🍪", ["wheat", "egg"]),
    ("สลัด{0}", "🥗", ["tomato"]),
    ("น้ำ{0}", "🍹", ["honey"]),
    ("ซุป{0}", "🥣", ["milk"]),
    ("พาย{0}", "🥧", ["wheat"]),
    ("แยม{0}", "🍯", ["honey"]),
    ("ขนมปัง{0}", "🍞", ["wheat"]),
    ("ออมเล็ต{0}", "🍳", ["egg"]),
    ("มิลค์เชค{0}", "🥤", ["milk", "honey"]),
    ("ข้าวผัด{0}", "🍛", ["wheat", "egg"]), # wheat as rice replacement
    ("เจลลี่{0}", "🍮", ["honey"]),
    ("น้ำเชื่อม{0}", "🍯", ["honey"]),
    ("แพนเค้ก{0}", "🥞", ["wheat", "egg", "honey"]),
    ("พิซซ่า{0}", "🍕", ["wheat", "tomato"]),
    ("ทาร์ต{0}", "🥧", ["wheat", "egg"]),
    ("สมูทตี้{0}", "🥤", ["milk"]),
    ("ไอศกรีม{0}", "🍦", ["milk", "honey"]),
    ("ขนมเปี๊ยะ{0}", "🥮", ["wheat", "egg"])
]

recipes_js = ""
recipe_idx = 1

for season, data in seasons.items():
    count = 0
    for crop, name, emoji in zip(data["crops"], data["names"], data["emojis"]):
        for prefix_template, r_emoji, extra_ingredients in prefixes:
            if count >= 20:
                break
            
            r_id = f"{season}_recipe_{count+1}"
            r_name = prefix_template.format(name)
            
            reqs = f"{crop}: 1"
            for ing in extra_ingredients:
                reqs += f", {ing}: 1"
                
            base_shop_price = 300 + (count * 50)
            
            recipes_js += f"            {r_id}: {{ id: '{r_id}', name: '{r_name}', emoji: '{r_emoji}', req: {{ {reqs} }}, xp: 50, unlockLevel: 2, shopPrice: {base_shop_price}, season: '{season}' }},\n"
            count += 1

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("const RECIPES = {", "const RECIPES = {\n" + recipes_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


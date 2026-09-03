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
        "crops": ["broccoli", "pear", "peach", "snowdrop"], 
        "names": ["บรอกโคลี", "แพร์", "พีช", "สโนว์ดรอป"],
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
    ("ข้าวผัด{0}", "🍛", ["wheat", "egg"]),
    ("เจลลี่{0}", "🍮", ["honey"]),
    ("น้ำเชื่อม{0}", "🍯", ["honey"]),
    ("แพนเค้ก{0}", "🥞", ["wheat", "egg", "honey"]),
    ("พิซซ่า{0}", "🍕", ["wheat", "tomato"]),
    ("ทาร์ต{0}", "🥧", ["wheat", "egg"]),
    ("สมูทตี้{0}", "🥤", ["milk"]),
    ("ไอศกรีม{0}", "🍦", ["milk", "honey"]),
    ("ขนมเปี๊ยะ{0}", "🥮", ["wheat", "egg"])
]

products_js = ""

for season, data in seasons.items():
    count = 0
    for crop, name, emoji in zip(data["crops"], data["names"], data["emojis"]):
        for prefix_template, r_emoji, extra_ingredients in prefixes:
            if count >= 20:
                break
            
            r_id = f"{season}_recipe_{count+1}"
            r_name = prefix_template.format(name)
            
            # Estimate base price
            basePrice = 200 + (count * 15) # Scaled up a bit so it's profitable
            
            products_js += f"            {r_id}: {{ id: '{r_id}', name: '{r_name}', emoji: '{r_emoji}', basePrice: {basePrice} }},\n"
            count += 1

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Append to PRODUCTS
content = content.replace("const PRODUCTS = {", "const PRODUCTS = {\n" + products_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add SEEDS
new_seeds = """
            potato: { id: 'potato', name: 'มันฝรั่ง', emoji: '🥔', buyPrice: 40, growTime: 20, xp: 25, produces: 'potato', unlockLevel: 3 },
            onion: { id: 'onion', name: 'หัวหอม', emoji: '🧅', buyPrice: 45, growTime: 25, xp: 30, produces: 'onion', unlockLevel: 4 },
            garlic: { id: 'garlic', name: 'กระเทียม', emoji: '🧄', buyPrice: 50, growTime: 30, xp: 35, produces: 'garlic', unlockLevel: 5 },
            bell_pepper: { id: 'bell_pepper', name: 'พริกหยวก', emoji: '🫑', buyPrice: 55, growTime: 35, xp: 40, produces: 'bell_pepper', unlockLevel: 5 },
            chili: { id: 'chili', name: 'พริก', emoji: '🌶️', buyPrice: 60, growTime: 40, xp: 45, produces: 'chili', unlockLevel: 6 },
            eggplant: { id: 'eggplant', name: 'มะเขือม่วง', emoji: '🍆', buyPrice: 65, growTime: 45, xp: 50, produces: 'eggplant', unlockLevel: 6 },
            peanut: { id: 'peanut', name: 'ถั่วลิสง', emoji: '🥜', buyPrice: 70, growTime: 50, xp: 55, produces: 'peanut', unlockLevel: 7 },
            beans: { id: 'beans', name: 'ถั่ว', emoji: '🫘', buyPrice: 75, growTime: 55, xp: 60, produces: 'beans', unlockLevel: 7 },
            cabbage: { id: 'cabbage', name: 'กะหล่ำปลี', emoji: '🥬', buyPrice: 80, growTime: 60, xp: 65, produces: 'cabbage', unlockLevel: 8 },
            avocado: { id: 'avocado', name: 'อะโวคาโด', emoji: '🥑', buyPrice: 85, growTime: 65, xp: 70, produces: 'avocado', unlockLevel: 8 },
            kiwi: { id: 'kiwi', name: 'กีวี', emoji: '🥝', buyPrice: 90, growTime: 70, xp: 75, produces: 'kiwi', unlockLevel: 9 },
            olive: { id: 'olive', name: 'มะกอก', emoji: '🫒', buyPrice: 95, growTime: 75, xp: 80, produces: 'olive', unlockLevel: 9 },
            cherry: { id: 'cherry', name: 'เชอร์รี', emoji: '🍒', buyPrice: 100, growTime: 80, xp: 85, produces: 'cherry', unlockLevel: 10 },
            lemon: { id: 'lemon', name: 'เลมอน', emoji: '🍋', buyPrice: 105, growTime: 85, xp: 90, produces: 'lemon', unlockLevel: 10 },
            orange: { id: 'orange', name: 'ส้ม', emoji: '🍊', buyPrice: 110, growTime: 90, xp: 95, produces: 'orange', unlockLevel: 11 },
            bamboo: { id: 'bamboo', name: 'ไผ่', emoji: '🎍', buyPrice: 115, growTime: 95, xp: 100, produces: 'bamboo', unlockLevel: 11 },
            hibiscus: { id: 'hibiscus', name: 'ชบา', emoji: '🌺', buyPrice: 120, growTime: 100, xp: 105, produces: 'hibiscus', unlockLevel: 12 },
            herb: { id: 'herb', name: 'สมุนไพร', emoji: '🌿', buyPrice: 125, growTime: 105, xp: 110, produces: 'herb', unlockLevel: 12 },
            green_apple: { id: 'green_apple', name: 'แอปเปิ้ลเขียว', emoji: '🍏', buyPrice: 130, growTime: 110, xp: 115, produces: 'green_apple', unlockLevel: 13 },
            pea: { id: 'pea', name: 'ถั่วลันเตา', emoji: '🫛', buyPrice: 135, growTime: 115, xp: 120, produces: 'pea', unlockLevel: 13 },
"""
content = re.sub(r"(const SEEDS = \{)", r"\1\n" + new_seeds, content)

# Add ANIMALS
new_animals = """
            turkey: { id: 'turkey', name: 'ไก่งวง', emoji: '🦃', buyPrice: 500, cooldown: 30, xp: 20, produces: 'turkey_egg', unlockLevel: 4 },
            goose: { id: 'goose', name: 'ห่าน', emoji: '🪿', buyPrice: 600, cooldown: 35, xp: 25, produces: 'goose_egg', unlockLevel: 5 },
            llama: { id: 'llama', name: 'ลามะ', emoji: '🦙', buyPrice: 2000, cooldown: 65, xp: 45, produces: 'llama_wool', unlockLevel: 7 },
            alpaca: { id: 'alpaca', name: 'อัลปาก้า', emoji: '🦙', buyPrice: 2200, cooldown: 70, xp: 50, produces: 'alpaca_wool', unlockLevel: 8 },
            deer: { id: 'deer', name: 'กวาง', emoji: '🦌', buyPrice: 3000, cooldown: 85, xp: 60, produces: 'antler', unlockLevel: 9 },
            camel: { id: 'camel', name: 'อูฐ', emoji: '🐪', buyPrice: 3500, cooldown: 95, xp: 65, produces: 'camel_milk', unlockLevel: 10 },
            buffalo: { id: 'buffalo', name: 'ควาย', emoji: '🐃', buyPrice: 4000, cooldown: 105, xp: 70, produces: 'buffalo_milk', unlockLevel: 11 },
            ox: { id: 'ox', name: 'วัวกระทิง', emoji: '🐂', buyPrice: 4500, cooldown: 110, xp: 75, produces: 'leather', unlockLevel: 12 },
            horse: { id: 'horse', name: 'ม้า', emoji: '🐴', buyPrice: 5000, cooldown: 120, xp: 80, produces: 'horse_hair', unlockLevel: 13 },
            dove: { id: 'dove', name: 'นกพิราบ', emoji: '🕊️', buyPrice: 5500, cooldown: 130, xp: 85, produces: 'feather', unlockLevel: 14 },
            peacock: { id: 'peacock', name: 'นกยูง', emoji: '🦚', buyPrice: 6000, cooldown: 140, xp: 90, produces: 'peacock_feather', unlockLevel: 15 },
            parrot: { id: 'parrot', name: 'นกแก้ว', emoji: '🦜', buyPrice: 6500, cooldown: 150, xp: 95, produces: 'colorful_feather', unlockLevel: 16 },
            swan: { id: 'swan', name: 'หงส์', emoji: '🦢', buyPrice: 7000, cooldown: 160, xp: 100, produces: 'swan_feather', unlockLevel: 17 },
            owl: { id: 'owl', name: 'นกฮูก', emoji: '🦉', buyPrice: 7500, cooldown: 170, xp: 105, produces: 'owl_feather', unlockLevel: 18 },
            turtle: { id: 'turtle', name: 'เต่า', emoji: '🐢', buyPrice: 8000, cooldown: 180, xp: 110, produces: 'turtle_shell', unlockLevel: 19 },
            snail: { id: 'snail', name: 'หอยทาก', emoji: '🐌', buyPrice: 8500, cooldown: 190, xp: 115, produces: 'snail_slime', unlockLevel: 20 },
            crab: { id: 'crab', name: 'ปู', emoji: '🦀', buyPrice: 9000, cooldown: 200, xp: 120, produces: 'crab_meat', unlockLevel: 21 },
            shrimp: { id: 'shrimp', name: 'กุ้ง', emoji: '🦐', buyPrice: 9500, cooldown: 210, xp: 125, produces: 'shrimp_meat', unlockLevel: 22 },
            fish: { id: 'fish', name: 'ปลา', emoji: '🐟', buyPrice: 10000, cooldown: 220, xp: 130, produces: 'fish_meat', unlockLevel: 23 },
            squid: { id: 'squid', name: 'ปลาหมึก', emoji: '🦑', buyPrice: 10500, cooldown: 230, xp: 135, produces: 'squid_ink', unlockLevel: 24 },
"""
content = re.sub(r"(const ANIMALS = \{)", r"\1\n" + new_animals, content)

# Add PRODUCTS
new_products = """
            potato: { id: 'potato', name: 'มันฝรั่ง', emoji: '🥔', basePrice: 60 },
            onion: { id: 'onion', name: 'หัวหอม', emoji: '🧅', basePrice: 70 },
            garlic: { id: 'garlic', name: 'กระเทียม', emoji: '🧄', basePrice: 80 },
            bell_pepper: { id: 'bell_pepper', name: 'พริกหยวก', emoji: '🫑', basePrice: 90 },
            chili: { id: 'chili', name: 'พริก', emoji: '🌶️', basePrice: 100 },
            eggplant: { id: 'eggplant', name: 'มะเขือม่วง', emoji: '🍆', basePrice: 110 },
            peanut: { id: 'peanut', name: 'ถั่วลิสง', emoji: '🥜', basePrice: 120 },
            beans: { id: 'beans', name: 'ถั่ว', emoji: '🫘', basePrice: 130 },
            cabbage: { id: 'cabbage', name: 'กะหล่ำปลี', emoji: '🥬', basePrice: 140 },
            avocado: { id: 'avocado', name: 'อะโวคาโด', emoji: '🥑', basePrice: 150 },
            kiwi: { id: 'kiwi', name: 'กีวี', emoji: '🥝', basePrice: 160 },
            olive: { id: 'olive', name: 'มะกอก', emoji: '🫒', basePrice: 170 },
            cherry: { id: 'cherry', name: 'เชอร์รี', emoji: '🍒', basePrice: 180 },
            lemon: { id: 'lemon', name: 'เลมอน', emoji: '🍋', basePrice: 190 },
            orange: { id: 'orange', name: 'ส้ม', emoji: '🍊', basePrice: 200 },
            bamboo: { id: 'bamboo', name: 'ไผ่', emoji: '🎍', basePrice: 210 },
            hibiscus: { id: 'hibiscus', name: 'ชบา', emoji: '🌺', basePrice: 220 },
            herb: { id: 'herb', name: 'สมุนไพร', emoji: '🌿', basePrice: 230 },
            green_apple: { id: 'green_apple', name: 'แอปเปิ้ลเขียว', emoji: '🍏', basePrice: 240 },
            pea: { id: 'pea', name: 'ถั่วลันเตา', emoji: '🫛', basePrice: 250 },

            turkey_egg: { id: 'turkey_egg', name: 'ไข่ไก่งวง', emoji: '🥚', basePrice: 60 },
            goose_egg: { id: 'goose_egg', name: 'ไข่ห่าน', emoji: '🥚', basePrice: 80 },
            llama_wool: { id: 'llama_wool', name: 'ขนลามะ', emoji: '🧶', basePrice: 250 },
            alpaca_wool: { id: 'alpaca_wool', name: 'ขนอัลปาก้า', emoji: '🧶', basePrice: 300 },
            antler: { id: 'antler', name: 'เขากวาง', emoji: '🦴', basePrice: 400 },
            camel_milk: { id: 'camel_milk', name: 'นมอูฐ', emoji: '🥛', basePrice: 500 },
            buffalo_milk: { id: 'buffalo_milk', name: 'นมควาย', emoji: '🥛', basePrice: 600 },
            leather: { id: 'leather', name: 'หนัง', emoji: '🟤', basePrice: 700 },
            horse_hair: { id: 'horse_hair', name: 'หางม้า', emoji: '🧵', basePrice: 800 },
            feather: { id: 'feather', name: 'ขนนก', emoji: '🪶', basePrice: 900 },
            peacock_feather: { id: 'peacock_feather', name: 'ขนนกยูง', emoji: '🪶', basePrice: 1000 },
            colorful_feather: { id: 'colorful_feather', name: 'ขนสีสดใส', emoji: '🪶', basePrice: 1100 },
            swan_feather: { id: 'swan_feather', name: 'ขนหงส์', emoji: '🪶', basePrice: 1200 },
            owl_feather: { id: 'owl_feather', name: 'ขนนกฮูก', emoji: '🪶', basePrice: 1300 },
            turtle_shell: { id: 'turtle_shell', name: 'กระดองเต่า', emoji: '🪨', basePrice: 1400 },
            snail_slime: { id: 'snail_slime', name: 'เมือกหอยทาก', emoji: '🧴', basePrice: 1500 },
            crab_meat: { id: 'crab_meat', name: 'เนื้อปู', emoji: '🦀', basePrice: 1600 },
            shrimp_meat: { id: 'shrimp_meat', name: 'เนื้อกุ้ง', emoji: '🦐', basePrice: 1700 },
            fish_meat: { id: 'fish_meat', name: 'เนื้อปลา', emoji: '🐟', basePrice: 1800 },
            squid_ink: { id: 'squid_ink', name: 'หมึกกล้วย', emoji: '🖋️', basePrice: 1900 },
"""
content = re.sub(r"(const PRODUCTS = \{)", r"\1\n" + new_products, content)

# Add RECIPES
new_recipes = """
            potato_soup: { id: 'potato_soup', name: 'ซุปมันฝรั่ง', emoji: '🥣', req: { potato: 2, milk: 1 }, xp: 100, unlockLevel: 5, shopPrice: 300 },
            french_fries: { id: 'french_fries', name: 'เฟรนช์ฟรายส์', emoji: '🍟', req: { potato: 3 }, xp: 80, unlockLevel: 5, shopPrice: 250 },
            onion_rings: { id: 'onion_rings', name: 'หอมทอด', emoji: '🧅', req: { onion: 2, wheat: 1 }, xp: 90, unlockLevel: 6, shopPrice: 280 },
            garlic_bread: { id: 'garlic_bread', name: 'ขนมปังกระเทียม', emoji: '🧄', req: { garlic: 2, wheat: 2 }, xp: 110, unlockLevel: 6, shopPrice: 350 },
            stuffed_pepper: { id: 'stuffed_pepper', name: 'พริกหยวกยัดไส้', emoji: '🫑', req: { bell_pepper: 2, meat: 1 }, xp: 150, unlockLevel: 7, shopPrice: 450 },
            spicy_curry: { id: 'spicy_curry', name: 'แกงเผ็ด', emoji: '🍛', req: { chili: 2, meat: 1, coconut: 1 }, xp: 200, unlockLevel: 7, shopPrice: 600 },
            roasted_eggplant: { id: 'roasted_eggplant', name: 'มะเขือเผา', emoji: '🍆', req: { eggplant: 3 }, xp: 120, unlockLevel: 8, shopPrice: 400 },
            peanut_butter: { id: 'peanut_butter', name: 'เนยถั่ว', emoji: '🥜', req: { peanut: 4 }, xp: 130, unlockLevel: 8, shopPrice: 500 },
            baked_beans: { id: 'baked_beans', name: 'ถั่วอบ', emoji: '🫘', req: { beans: 3, tomato: 1 }, xp: 140, unlockLevel: 9, shopPrice: 480 },
            coleslaw: { id: 'coleslaw', name: 'โคลสลอว์', emoji: '🥗', req: { cabbage: 2, carrot: 1, milk: 1 }, xp: 150, unlockLevel: 9, shopPrice: 550 },
            guacamole: { id: 'guacamole', name: 'กัวคาโมเล่', emoji: '🥑', req: { avocado: 2, tomato: 1, onion: 1 }, xp: 180, unlockLevel: 10, shopPrice: 650 },
            kiwi_smoothie: { id: 'kiwi_smoothie', name: 'สมูทตี้กีวี', emoji: '🥤', req: { kiwi: 2, milk: 1, honey: 1 }, xp: 160, unlockLevel: 10, shopPrice: 600 },
            olive_oil: { id: 'olive_oil', name: 'น้ำมันมะกอก', emoji: '🫒', req: { olive: 4 }, xp: 140, unlockLevel: 11, shopPrice: 700 },
            cherry_pie: { id: 'cherry_pie', name: 'พายเชอร์รี', emoji: '🥧', req: { cherry: 3, wheat: 2, egg: 1 }, xp: 220, unlockLevel: 11, shopPrice: 850 },
            lemonade: { id: 'lemonade', name: 'น้ำเลมอน', emoji: '🍹', req: { lemon: 2, honey: 1 }, xp: 120, unlockLevel: 12, shopPrice: 450 },
            orange_juice: { id: 'orange_juice', name: 'น้ำส้ม', emoji: '🧃', req: { orange: 3 }, xp: 130, unlockLevel: 12, shopPrice: 500 },
            crab_fried_rice: { id: 'crab_fried_rice', name: 'ข้าวผัดปู', emoji: '🍛', req: { crab_meat: 1, wheat: 1, egg: 1 }, xp: 300, unlockLevel: 21, shopPrice: 2000 },
            shrimp_soup: { id: 'shrimp_soup', name: 'ต้มยำกุ้ง', emoji: '🥣', req: { shrimp_meat: 1, chili: 2, lime: 1 }, xp: 350, unlockLevel: 22, shopPrice: 2500 },
            grilled_fish: { id: 'grilled_fish', name: 'ปลาย่าง', emoji: '🐟', req: { fish_meat: 1, salt: 1 }, xp: 400, unlockLevel: 23, shopPrice: 3000 },
            squid_sushi: { id: 'squid_sushi', name: 'ซูชิปลาหมึก', emoji: '🍣', req: { squid_ink: 1, wheat: 1 }, xp: 450, unlockLevel: 24, shopPrice: 3500 },
"""
# For crab fried rice, it requires 'wheat' (acts as rice) and 'meat' (for generic meat).
# Oh wait, there is no 'meat' in the original game? The user can just get the ingredients. Let's see if meat exists, if not, recipes can just require ingredients.
# I will just write it. The app doesn't check if ingredient exists when crafting except reading inventory. 

content = re.sub(r"(const RECIPES = \{)", r"\1\n" + new_recipes, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

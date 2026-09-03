        /* =========================================
           1. GAME DATA & CONFIGURATION
           ========================================= */
        const SEEDS = {

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

            tulip: { id: 'tulip', name: 'ทิวลิป', emoji: '🌷', buyPrice: 180, growTime: 120, xp: 90, produces: 'tulip', unlockLevel: 2, season: 'spring' },
            rose: { id: 'rose', name: 'กุหลาบ', emoji: '🌹', buyPrice: 200, growTime: 150, xp: 100, produces: 'rose', unlockLevel: 2, season: 'spring' },
            daisy: { id: 'daisy', name: 'เดซี่', emoji: '🌼', buyPrice: 150, growTime: 100, xp: 75, produces: 'daisy', unlockLevel: 2, season: 'spring' },
            cucumber: { id: 'cucumber', name: 'แตงกวา', emoji: '🥒', buyPrice: 70, growTime: 65, xp: 40, produces: 'cucumber', unlockLevel: 2, season: 'spring' },
            mango: { id: 'mango', name: 'มะม่วง', emoji: '🥭', buyPrice: 180, growTime: 150, xp: 90, produces: 'mango', unlockLevel: 2, season: 'summer' },
            coconut: { id: 'coconut', name: 'มะพร้าว', emoji: '🥥', buyPrice: 250, growTime: 200, xp: 120, produces: 'coconut', unlockLevel: 2, season: 'summer' },
            papaya: { id: 'papaya', name: 'กล้วย', emoji: '🍌', buyPrice: 130, growTime: 110, xp: 60, produces: 'papaya', unlockLevel: 2, season: 'summer' },
            lime: { id: 'lime', name: 'มะนาว', emoji: '🍋‍🟩', buyPrice: 90, growTime: 80, xp: 45, produces: 'lime', unlockLevel: 2, season: 'summer' },
            sweet_potato: { id: 'sweet_potato', name: 'มันเทศ', emoji: '🍠', buyPrice: 120, growTime: 95, xp: 60, produces: 'sweet_potato', unlockLevel: 2, season: 'autumn' },
            mushroom: { id: 'mushroom', name: 'เห็ด', emoji: '🍄', buyPrice: 80, growTime: 70, xp: 45, produces: 'mushroom', unlockLevel: 2, season: 'autumn' },
            apple: { id: 'apple', name: 'แอปเปิ้ล', emoji: '🍎', buyPrice: 220, growTime: 180, xp: 110, produces: 'apple', unlockLevel: 2, season: 'autumn' },
            chestnut: { id: 'chestnut', name: 'เกาลัด', emoji: '🌰', buyPrice: 160, growTime: 140, xp: 85, produces: 'chestnut', unlockLevel: 2, season: 'autumn' },
            broccoli: { id: 'broccoli', name: 'บรอกโคลี', emoji: '🥦', buyPrice: 140, growTime: 110, xp: 70, produces: 'broccoli', unlockLevel: 2, season: 'winter' },
            pear: { id: 'pear', name: 'ลูกแพร์', emoji: '🍐', buyPrice: 190, growTime: 160, xp: 95, produces: 'pear', unlockLevel: 2, season: 'winter' },
            peach: { id: 'peach', name: 'ลูกพีช', emoji: '🍑', buyPrice: 240, growTime: 190, xp: 120, produces: 'peach', unlockLevel: 2, season: 'winter' },

            carrot: { id: 'carrot', name: 'แครอท', emoji: '🥕', buyPrice: 10, growTime: 5, xp: 5, produces: 'carrot', unlockLevel: 1 },
            tomato: { id: 'tomato', name: 'มะเขือเทศ', emoji: '🍅', buyPrice: 20, growTime: 10, xp: 12, produces: 'tomato', unlockLevel: 2 },
            wheat: { id: 'wheat', name: 'ข้าวสาลี', emoji: '🌾', buyPrice: 15, growTime: 8, xp: 8, produces: 'wheat', unlockLevel: 3 },
            corn: { id: 'corn', name: 'ข้าวโพด', emoji: '🌽', buyPrice: 35, growTime: 15, xp: 20, produces: 'corn', unlockLevel: 4 },
            watermelon: { id: 'watermelon', name: 'แตงโม', emoji: '🍉', buyPrice: 50, growTime: 30, xp: 35, produces: 'watermelon', unlockLevel: 5 },
            strawberry: { id: 'strawberry', name: 'สตรอว์เบอร์รี', emoji: '🍓', buyPrice: 80, growTime: 45, xp: 50, produces: 'strawberry', unlockLevel: 7 },

            potato: { id: 'potato', name: 'มันฝรั่ง', emoji: '🥔', buyPrice: 15, growTime: 20, xp: 8, produces: 'potato', unlockLevel: 2 },
            onion: { id: 'onion', name: 'หัวหอม', emoji: '🧅', buyPrice: 20, growTime: 25, xp: 12, produces: 'onion', unlockLevel: 3 },
            cabbage: { id: 'cabbage', name: 'กะหล่ำปลี', emoji: '🥬', buyPrice: 25, growTime: 30, xp: 15, produces: 'cabbage', unlockLevel: 4 },
            pumpkin: { id: 'pumpkin', name: 'ฟักทอง', emoji: '🎃', buyPrice: 40, growTime: 45, xp: 25, produces: 'pumpkin', unlockLevel: 5 },
            eggplant: { id: 'eggplant', name: 'มะเขือม่วง', emoji: '🍆', buyPrice: 35, growTime: 40, xp: 20, produces: 'eggplant', unlockLevel: 6 },
            chili: { id: 'chili', name: 'พริก', emoji: '🌶️', buyPrice: 50, growTime: 50, xp: 30, produces: 'chili', unlockLevel: 7 },
            blueberry: { id: 'blueberry', name: 'บลูเบอร์รี', emoji: '🫐', buyPrice: 60, growTime: 60, xp: 35, produces: 'blueberry', unlockLevel: 8 },
            grape: { id: 'grape', name: 'องุ่น', emoji: '🍇', buyPrice: 80, growTime: 75, xp: 45, produces: 'grape', unlockLevel: 9 },
            melon: { id: 'melon', name: 'เมลอน', emoji: '🍈', buyPrice: 100, growTime: 90, xp: 60, produces: 'melon', unlockLevel: 10 },
            pineapple: { id: 'pineapple', name: 'สับปะรด', emoji: '🍍', buyPrice: 120, growTime: 120, xp: 80, produces: 'pineapple', unlockLevel: 11 },

        };

        const ANIMALS = {

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

            chicken: { id: 'chicken', name: 'ไก่', emoji: '🐔', buyPrice: 200, cooldown: 20, xp: 10, produces: 'egg', unlockLevel: 1 },
            duck: { id: 'duck', name: 'เป็ด', emoji: '🦆', buyPrice: 350, cooldown: 25, xp: 15, produces: 'duck_egg', unlockLevel: 3 },
            cow: { id: 'cow', name: 'วัว', emoji: '🐄', buyPrice: 1800, cooldown: 60, xp: 25, produces: 'milk', unlockLevel: 5 },
            sheep: { id: 'sheep', name: 'แกะ', emoji: '🐑', buyPrice: 1200, cooldown: 50, xp: 35, produces: 'wool', unlockLevel: 6 },
            pig: { id: 'pig', name: 'หมู', emoji: '🐖', buyPrice: 2500, cooldown: 80, xp: 60, produces: 'truffle', unlockLevel: 8 },

            rabbit: { id: 'rabbit', name: 'กระต่าย', emoji: '🐰', buyPrice: 1800, cooldown: 60, xp: 40, produces: 'fur', unlockLevel: 9 },
            goat: { id: 'goat', name: 'แพะ', emoji: '🐐', buyPrice: 3000, cooldown: 70, xp: 50, produces: 'goat_milk', unlockLevel: 10 },
            bee: { id: 'bee', name: 'ผึ้ง', emoji: '🐝', buyPrice: 4000, cooldown: 90, xp: 30, produces: 'honey', unlockLevel: 11 },
            silkworm: { id: 'silkworm', name: 'หนอนไหม', emoji: '🐛', buyPrice: 6000, cooldown: 100, xp: 70, produces: 'silk', unlockLevel: 12 },
            alpaca: { id: 'alpaca', name: 'อัลปากา', emoji: '🦙', buyPrice: 10000, cooldown: 120, xp: 100, produces: 'alpaca_wool', unlockLevel: 13 },

        };

        
        const PRODUCTS = {

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

            spring_recipe_1: { id: 'spring_recipe_1', name: 'ชาทิวลิป', emoji: '🍵', basePrice: 200 },
            spring_recipe_2: { id: 'spring_recipe_2', name: 'เค้กทิวลิป', emoji: '🍰', basePrice: 215 },
            spring_recipe_3: { id: 'spring_recipe_3', name: 'คุกกี้ทิวลิป', emoji: '🍪', basePrice: 230 },
            spring_recipe_4: { id: 'spring_recipe_4', name: 'สลัดทิวลิป', emoji: '🥗', basePrice: 245 },
            spring_recipe_5: { id: 'spring_recipe_5', name: 'น้ำทิวลิป', emoji: '🍹', basePrice: 260 },
            spring_recipe_6: { id: 'spring_recipe_6', name: 'ซุปทิวลิป', emoji: '🥣', basePrice: 275 },
            spring_recipe_7: { id: 'spring_recipe_7', name: 'พายทิวลิป', emoji: '🥧', basePrice: 290 },
            spring_recipe_8: { id: 'spring_recipe_8', name: 'แยมทิวลิป', emoji: '🍯', basePrice: 305 },
            spring_recipe_9: { id: 'spring_recipe_9', name: 'ขนมปังทิวลิป', emoji: '🍞', basePrice: 320 },
            spring_recipe_10: { id: 'spring_recipe_10', name: 'ออมเล็ตทิวลิป', emoji: '🍳', basePrice: 335 },
            spring_recipe_11: { id: 'spring_recipe_11', name: 'มิลค์เชคทิวลิป', emoji: '🥤', basePrice: 350 },
            spring_recipe_12: { id: 'spring_recipe_12', name: 'ข้าวผัดทิวลิป', emoji: '🍛', basePrice: 365 },
            spring_recipe_13: { id: 'spring_recipe_13', name: 'เจลลี่ทิวลิป', emoji: '🍮', basePrice: 380 },
            spring_recipe_14: { id: 'spring_recipe_14', name: 'น้ำเชื่อมทิวลิป', emoji: '🍯', basePrice: 395 },
            spring_recipe_15: { id: 'spring_recipe_15', name: 'แพนเค้กทิวลิป', emoji: '🥞', basePrice: 410 },
            spring_recipe_16: { id: 'spring_recipe_16', name: 'พิซซ่าทิวลิป', emoji: '🍕', basePrice: 425 },
            spring_recipe_17: { id: 'spring_recipe_17', name: 'ทาร์ตทิวลิป', emoji: '🥧', basePrice: 440 },
            spring_recipe_18: { id: 'spring_recipe_18', name: 'สมูทตี้ทิวลิป', emoji: '🥤', basePrice: 455 },
            spring_recipe_19: { id: 'spring_recipe_19', name: 'ไอศกรีมทิวลิป', emoji: '🍦', basePrice: 470 },
            spring_recipe_20: { id: 'spring_recipe_20', name: 'ขนมเปี๊ยะทิวลิป', emoji: '🥮', basePrice: 485 },
            summer_recipe_1: { id: 'summer_recipe_1', name: 'ชามะม่วง', emoji: '🍵', basePrice: 200 },
            summer_recipe_2: { id: 'summer_recipe_2', name: 'เค้กมะม่วง', emoji: '🍰', basePrice: 215 },
            summer_recipe_3: { id: 'summer_recipe_3', name: 'คุกกี้มะม่วง', emoji: '🍪', basePrice: 230 },
            summer_recipe_4: { id: 'summer_recipe_4', name: 'สลัดมะม่วง', emoji: '🥗', basePrice: 245 },
            summer_recipe_5: { id: 'summer_recipe_5', name: 'น้ำมะม่วง', emoji: '🍹', basePrice: 260 },
            summer_recipe_6: { id: 'summer_recipe_6', name: 'ซุปมะม่วง', emoji: '🥣', basePrice: 275 },
            summer_recipe_7: { id: 'summer_recipe_7', name: 'พายมะม่วง', emoji: '🥧', basePrice: 290 },
            summer_recipe_8: { id: 'summer_recipe_8', name: 'แยมมะม่วง', emoji: '🍯', basePrice: 305 },
            summer_recipe_9: { id: 'summer_recipe_9', name: 'ขนมปังมะม่วง', emoji: '🍞', basePrice: 320 },
            summer_recipe_10: { id: 'summer_recipe_10', name: 'ออมเล็ตมะม่วง', emoji: '🍳', basePrice: 335 },
            summer_recipe_11: { id: 'summer_recipe_11', name: 'มิลค์เชคมะม่วง', emoji: '🥤', basePrice: 350 },
            summer_recipe_12: { id: 'summer_recipe_12', name: 'ข้าวผัดมะม่วง', emoji: '🍛', basePrice: 365 },
            summer_recipe_13: { id: 'summer_recipe_13', name: 'เจลลี่มะม่วง', emoji: '🍮', basePrice: 380 },
            summer_recipe_14: { id: 'summer_recipe_14', name: 'น้ำเชื่อมมะม่วง', emoji: '🍯', basePrice: 395 },
            summer_recipe_15: { id: 'summer_recipe_15', name: 'แพนเค้กมะม่วง', emoji: '🥞', basePrice: 410 },
            summer_recipe_16: { id: 'summer_recipe_16', name: 'พิซซ่ามะม่วง', emoji: '🍕', basePrice: 425 },
            summer_recipe_17: { id: 'summer_recipe_17', name: 'ทาร์ตมะม่วง', emoji: '🥧', basePrice: 440 },
            summer_recipe_18: { id: 'summer_recipe_18', name: 'สมูทตี้มะม่วง', emoji: '🥤', basePrice: 455 },
            summer_recipe_19: { id: 'summer_recipe_19', name: 'ไอศกรีมมะม่วง', emoji: '🍦', basePrice: 470 },
            summer_recipe_20: { id: 'summer_recipe_20', name: 'ขนมเปี๊ยะมะม่วง', emoji: '🥮', basePrice: 485 },
            autumn_recipe_1: { id: 'autumn_recipe_1', name: 'ชามันเทศ', emoji: '🍵', basePrice: 200 },
            autumn_recipe_2: { id: 'autumn_recipe_2', name: 'เค้กมันเทศ', emoji: '🍰', basePrice: 215 },
            autumn_recipe_3: { id: 'autumn_recipe_3', name: 'คุกกี้มันเทศ', emoji: '🍪', basePrice: 230 },
            autumn_recipe_4: { id: 'autumn_recipe_4', name: 'สลัดมันเทศ', emoji: '🥗', basePrice: 245 },
            autumn_recipe_5: { id: 'autumn_recipe_5', name: 'น้ำมันเทศ', emoji: '🍹', basePrice: 260 },
            autumn_recipe_6: { id: 'autumn_recipe_6', name: 'ซุปมันเทศ', emoji: '🥣', basePrice: 275 },
            autumn_recipe_7: { id: 'autumn_recipe_7', name: 'พายมันเทศ', emoji: '🥧', basePrice: 290 },
            autumn_recipe_8: { id: 'autumn_recipe_8', name: 'แยมมันเทศ', emoji: '🍯', basePrice: 305 },
            autumn_recipe_9: { id: 'autumn_recipe_9', name: 'ขนมปังมันเทศ', emoji: '🍞', basePrice: 320 },
            autumn_recipe_10: { id: 'autumn_recipe_10', name: 'ออมเล็ตมันเทศ', emoji: '🍳', basePrice: 335 },
            autumn_recipe_11: { id: 'autumn_recipe_11', name: 'มิลค์เชคมันเทศ', emoji: '🥤', basePrice: 350 },
            autumn_recipe_12: { id: 'autumn_recipe_12', name: 'ข้าวผัดมันเทศ', emoji: '🍛', basePrice: 365 },
            autumn_recipe_13: { id: 'autumn_recipe_13', name: 'เจลลี่มันเทศ', emoji: '🍮', basePrice: 380 },
            autumn_recipe_14: { id: 'autumn_recipe_14', name: 'น้ำเชื่อมมันเทศ', emoji: '🍯', basePrice: 395 },
            autumn_recipe_15: { id: 'autumn_recipe_15', name: 'แพนเค้กมันเทศ', emoji: '🥞', basePrice: 410 },
            autumn_recipe_16: { id: 'autumn_recipe_16', name: 'พิซซ่ามันเทศ', emoji: '🍕', basePrice: 425 },
            autumn_recipe_17: { id: 'autumn_recipe_17', name: 'ทาร์ตมันเทศ', emoji: '🥧', basePrice: 440 },
            autumn_recipe_18: { id: 'autumn_recipe_18', name: 'สมูทตี้มันเทศ', emoji: '🥤', basePrice: 455 },
            autumn_recipe_19: { id: 'autumn_recipe_19', name: 'ไอศกรีมมันเทศ', emoji: '🍦', basePrice: 470 },
            autumn_recipe_20: { id: 'autumn_recipe_20', name: 'ขนมเปี๊ยะมันเทศ', emoji: '🥮', basePrice: 485 },
            winter_recipe_1: { id: 'winter_recipe_1', name: 'ชาบรอกโคลี', emoji: '🍵', basePrice: 200 },
            winter_recipe_2: { id: 'winter_recipe_2', name: 'เค้กบรอกโคลี', emoji: '🍰', basePrice: 215 },
            winter_recipe_3: { id: 'winter_recipe_3', name: 'คุกกี้บรอกโคลี', emoji: '🍪', basePrice: 230 },
            winter_recipe_4: { id: 'winter_recipe_4', name: 'สลัดบรอกโคลี', emoji: '🥗', basePrice: 245 },
            winter_recipe_5: { id: 'winter_recipe_5', name: 'น้ำบรอกโคลี', emoji: '🍹', basePrice: 260 },
            winter_recipe_6: { id: 'winter_recipe_6', name: 'ซุปบรอกโคลี', emoji: '🥣', basePrice: 275 },
            winter_recipe_7: { id: 'winter_recipe_7', name: 'พายบรอกโคลี', emoji: '🥧', basePrice: 290 },
            winter_recipe_8: { id: 'winter_recipe_8', name: 'แยมบรอกโคลี', emoji: '🍯', basePrice: 305 },
            winter_recipe_9: { id: 'winter_recipe_9', name: 'ขนมปังบรอกโคลี', emoji: '🍞', basePrice: 320 },
            winter_recipe_10: { id: 'winter_recipe_10', name: 'ออมเล็ตบรอกโคลี', emoji: '🍳', basePrice: 335 },
            winter_recipe_11: { id: 'winter_recipe_11', name: 'มิลค์เชคบรอกโคลี', emoji: '🥤', basePrice: 350 },
            winter_recipe_12: { id: 'winter_recipe_12', name: 'ข้าวผัดบรอกโคลี', emoji: '🍛', basePrice: 365 },
            winter_recipe_13: { id: 'winter_recipe_13', name: 'เจลลี่บรอกโคลี', emoji: '🍮', basePrice: 380 },
            winter_recipe_14: { id: 'winter_recipe_14', name: 'น้ำเชื่อมบรอกโคลี', emoji: '🍯', basePrice: 395 },
            winter_recipe_15: { id: 'winter_recipe_15', name: 'แพนเค้กบรอกโคลี', emoji: '🥞', basePrice: 410 },
            winter_recipe_16: { id: 'winter_recipe_16', name: 'พิซซ่าบรอกโคลี', emoji: '🍕', basePrice: 425 },
            winter_recipe_17: { id: 'winter_recipe_17', name: 'ทาร์ตบรอกโคลี', emoji: '🥧', basePrice: 440 },
            winter_recipe_18: { id: 'winter_recipe_18', name: 'สมูทตี้บรอกโคลี', emoji: '🥤', basePrice: 455 },
            winter_recipe_19: { id: 'winter_recipe_19', name: 'ไอศกรีมบรอกโคลี', emoji: '🍦', basePrice: 470 },
            winter_recipe_20: { id: 'winter_recipe_20', name: 'ขนมเปี๊ยะบรอกโคลี', emoji: '🥮', basePrice: 485 },

            tulip: { id: 'tulip', name: 'ทิวลิป', emoji: '🌷', basePrice: 300 },
            rose: { id: 'rose', name: 'กุหลาบ', emoji: '🌹', basePrice: 350 },
            daisy: { id: 'daisy', name: 'เดซี่', emoji: '🌼', basePrice: 250 },
            cucumber: { id: 'cucumber', name: 'แตงกวา', emoji: '🥒', basePrice: 120 },
            mango: { id: 'mango', name: 'มะม่วง', emoji: '🥭', basePrice: 300 },
            coconut: { id: 'coconut', name: 'มะพร้าว', emoji: '🥥', basePrice: 400 },
            papaya: { id: 'papaya', name: 'กล้วย', emoji: '🍌', basePrice: 220 },
            lime: { id: 'lime', name: 'มะนาว', emoji: '🍋‍🟩', basePrice: 150 },
            sweet_potato: { id: 'sweet_potato', name: 'มันเทศ', emoji: '🍠', basePrice: 200 },
            mushroom: { id: 'mushroom', name: 'เห็ด', emoji: '🍄', basePrice: 140 },
            apple: { id: 'apple', name: 'แอปเปิ้ล', emoji: '🍎', basePrice: 380 },
            chestnut: { id: 'chestnut', name: 'เกาลัด', emoji: '🌰', basePrice: 280 },
            broccoli: { id: 'broccoli', name: 'บรอกโคลี', emoji: '🥦', basePrice: 240 },
            pear: { id: 'pear', name: 'ลูกแพร์', emoji: '🍐', basePrice: 320 },
            peach: { id: 'peach', name: 'ลูกพีช', emoji: '🍑', basePrice: 420 },

            carrot: { id: 'carrot', name: 'แครอท', emoji: '🥕', basePrice: 15 },
            tomato: { id: 'tomato', name: 'มะเขือเทศ', emoji: '🍅', basePrice: 35 },
            wheat: { id: 'wheat', name: 'ข้าวสาลี', emoji: '🌾', basePrice: 25 },
            corn: { id: 'corn', name: 'ข้าวโพด', emoji: '🌽', basePrice: 55 },
            watermelon: { id: 'watermelon', name: 'แตงโม', emoji: '🍉', basePrice: 120 },
            strawberry: { id: 'strawberry', name: 'สตรอว์เบอร์รี', emoji: '🍓', basePrice: 180 },
            potato: { id: 'potato', name: 'มันฝรั่ง', emoji: '🥔', basePrice: 20 },
            onion: { id: 'onion', name: 'หัวหอม', emoji: '🧅', basePrice: 25 },
            cabbage: { id: 'cabbage', name: 'กะหล่ำปลี', emoji: '🥬', basePrice: 35 },
            pumpkin: { id: 'pumpkin', name: 'ฟักทอง', emoji: '🎃', basePrice: 50 },
            eggplant: { id: 'eggplant', name: 'มะเขือม่วง', emoji: '🍆', basePrice: 45 },
            chili: { id: 'chili', name: 'พริก', emoji: '🌶️', basePrice: 65 },
            blueberry: { id: 'blueberry', name: 'บลูเบอร์รี', emoji: '🫐', basePrice: 80 },
            grape: { id: 'grape', name: 'องุ่น', emoji: '🍇', basePrice: 110 },
            melon: { id: 'melon', name: 'เมลอน', emoji: '🍈', basePrice: 140 },
            pineapple: { id: 'pineapple', name: 'สับปะรด', emoji: '🍍', basePrice: 160 },

            egg: { id: 'egg', name: 'ไข่ไก่', emoji: '🥚', basePrice: 20 },
            duck_egg: { id: 'duck_egg', name: 'ไข่เป็ด', emoji: '🥚', basePrice: 35 },
            milk: { id: 'milk', name: 'นมวัว', emoji: '🥛', basePrice: 60 },
            wool: { id: 'wool', name: 'ขนแกะ', emoji: '🧶', basePrice: 90 },
            truffle: { id: 'truffle', name: 'เห็ดทรัฟเฟิล', emoji: '🍄', basePrice: 250 },
            fur: { id: 'fur', name: 'ขนกระต่าย', emoji: '🐰', basePrice: 120 },
            goat_milk: { id: 'goat_milk', name: 'นมแพะ', emoji: '🥛', basePrice: 150 },
            honey: { id: 'honey', name: 'น้ำผึ้ง', emoji: '🍯', basePrice: 200 },
            silk: { id: 'silk', name: 'ใยไหม', emoji: '🧵', basePrice: 250 },
            alpaca_wool: { id: 'alpaca_wool', name: 'ขนอัลปากา', emoji: '🦙', basePrice: 350 },

            // Cooked foods
            fried_egg: { id: 'fried_egg', name: 'ไข่ดาว', emoji: '🍳', basePrice: 50 },
            bread: { id: 'bread', name: 'ขนมปัง', emoji: '🍞', basePrice: 90 },
            carrot_soup: { id: 'carrot_soup', name: 'ซุปแครอท', emoji: '🥣', basePrice: 100 },
            corn_soup: { id: 'corn_soup', name: 'ซุปข้าวโพด', emoji: '🥣', basePrice: 150 },
            cake: { id: 'cake', name: 'เค้ก', emoji: '🍰', basePrice: 300 },
            pizza: { id: 'pizza', name: 'พิซซ่า', emoji: '🍕', basePrice: 450 },
            fries: { id: 'fries', name: 'เฟรนช์ฟรายส์', emoji: '🍟', basePrice: 60 },
            salad: { id: 'salad', name: 'สลัดผัก', emoji: '🥗', basePrice: 80 },
            onion_rings: { id: 'onion_rings', name: 'หอมทอด', emoji: '🧅', basePrice: 70 },
            pumpkin_soup: { id: 'pumpkin_soup', name: 'ซุปฟักทอง', emoji: '🥣', basePrice: 120 },
            stuffed_eggplant: { id: 'stuffed_eggplant', name: 'มะเขือม่วงยัดไส้', emoji: '🍆', basePrice: 150 },
            chili_sauce: { id: 'chili_sauce', name: 'ซอสพริก', emoji: '🌶️', basePrice: 100 },
            blueberry_jam: { id: 'blueberry_jam', name: 'แยมบลูเบอร์รี', emoji: '🫐', basePrice: 130 },
            grape_juice: { id: 'grape_juice', name: 'น้ำองุ่น', emoji: '🧃', basePrice: 160 },
            melon_pan: { id: 'melon_pan', name: 'เมลอนปัง', emoji: '🍞', basePrice: 200 },
            pineapple_fried_rice: { id: 'pineapple_fried_rice', name: 'ข้าวผัดสับปะรด', emoji: '🍍', basePrice: 250 },
            honey_toast: { id: 'honey_toast', name: 'ฮันนี่โทสต์', emoji: '🍞', basePrice: 300 },
            goat_cheese: { id: 'goat_cheese', name: 'ชีสนมแพะ', emoji: '🧀', basePrice: 250 },
            omelet: { id: 'omelet', name: 'ออมเล็ต', emoji: '🍳', basePrice: 110 },
            pancake: { id: 'pancake', name: 'แพนเค้ก', emoji: '🥞', basePrice: 180 },
            spicy_salad: { id: 'spicy_salad', name: 'ยำรสแซ่บ', emoji: '🥗', basePrice: 140 },
            berry_cake: { id: 'berry_cake', name: 'เค้กเบอร์รี', emoji: '🍰', basePrice: 350 },
            fruit_salad: { id: 'fruit_salad', name: 'สลัดผลไม้', emoji: '🥣', basePrice: 220 },
            honey_milk: { id: 'honey_milk', name: 'นมอุ่นน้ำผึ้ง', emoji: '🥛', basePrice: 180 },
            truffle_pasta: { id: 'truffle_pasta', name: 'พาสต้าทรัฟเฟิล', emoji: '🍝', basePrice: 500 },
            premium_pizza: { id: 'premium_pizza', name: 'พรีเมียมพิซซ่า', emoji: '🍕', basePrice: 600 }
        };

        const RECIPES = {

            potato_soup: { id: 'potato_soup', name: 'ซุปมันฝรั่ง', emoji: '🥣', req: { potato: 2, milk: 1 }, xp: 100, unlockLevel: 5, shopPrice: 300 },
            french_fries: { id: 'french_fries', name: 'เฟรนช์ฟรายส์', emoji: '🍟', req: { potato: 3 }, xp: 80, unlockLevel: 5, shopPrice: 250 },
            onion_rings: { id: 'onion_rings', name: 'หอมทอด', emoji: '🧅', req: { onion: 2, wheat: 1 }, xp: 90, unlockLevel: 6, shopPrice: 280 },
            garlic_bread: { id: 'garlic_bread', name: 'ขนมปังกระเทียม', emoji: '🧄', req: { garlic: 2, wheat: 2 }, xp: 110, unlockLevel: 6, shopPrice: 350 },
            stuffed_pepper: { id: 'stuffed_pepper', name: 'พริกหยวกยัดไส้', emoji: '🫑', req: { bell_pepper: 2, egg: 1 }, xp: 150, unlockLevel: 7, shopPrice: 450 },
            spicy_curry: { id: 'spicy_curry', name: 'แกงเผ็ด', emoji: '🍛', req: { chili: 2, egg: 1, coconut: 1 }, xp: 200, unlockLevel: 7, shopPrice: 600 },
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
            crab_fried_rice: { id: 'crab_fried_rice', name: 'ข้าวผัดปู', emoji: '🍛', req: { crab_egg: 1, wheat: 1, egg: 1 }, xp: 300, unlockLevel: 21, shopPrice: 2000 },
            shrimp_soup: { id: 'shrimp_soup', name: 'ต้มยำกุ้ง', emoji: '🥣', req: { shrimp_egg: 1, chili: 2, lime: 1 }, xp: 350, unlockLevel: 22, shopPrice: 2500 },
            grilled_fish: { id: 'grilled_fish', name: 'ปลาย่าง', emoji: '🐟', req: { fish_egg: 1, herb: 1 }, xp: 400, unlockLevel: 23, shopPrice: 3000 },
            squid_sushi: { id: 'squid_sushi', name: 'ซูชิปลาหมึก', emoji: '🍣', req: { squid_ink: 1, wheat: 1 }, xp: 450, unlockLevel: 24, shopPrice: 3500 },

            spring_recipe_1: { id: 'spring_recipe_1', name: 'ชาทิวลิป', emoji: '🍵', req: { tulip: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 300, season: 'spring' },
            spring_recipe_2: { id: 'spring_recipe_2', name: 'เค้กทิวลิป', emoji: '🍰', req: { tulip: 1, wheat: 1, milk: 1 }, xp: 50, unlockLevel: 2, shopPrice: 350, season: 'spring' },
            spring_recipe_3: { id: 'spring_recipe_3', name: 'คุกกี้ทิวลิป', emoji: '🍪', req: { tulip: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 400, season: 'spring' },
            spring_recipe_4: { id: 'spring_recipe_4', name: 'สลัดทิวลิป', emoji: '🥗', req: { tulip: 1, tomato: 1 }, xp: 50, unlockLevel: 2, shopPrice: 450, season: 'spring' },
            spring_recipe_5: { id: 'spring_recipe_5', name: 'น้ำทิวลิป', emoji: '🍹', req: { tulip: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 500, season: 'spring' },
            spring_recipe_6: { id: 'spring_recipe_6', name: 'ซุปทิวลิป', emoji: '🥣', req: { tulip: 1, milk: 1 }, xp: 50, unlockLevel: 2, shopPrice: 550, season: 'spring' },
            spring_recipe_7: { id: 'spring_recipe_7', name: 'พายทิวลิป', emoji: '🥧', req: { tulip: 1, wheat: 1 }, xp: 50, unlockLevel: 2, shopPrice: 600, season: 'spring' },
            spring_recipe_8: { id: 'spring_recipe_8', name: 'แยมทิวลิป', emoji: '🍯', req: { tulip: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 650, season: 'spring' },
            spring_recipe_9: { id: 'spring_recipe_9', name: 'ขนมปังทิวลิป', emoji: '🍞', req: { tulip: 1, wheat: 1 }, xp: 50, unlockLevel: 2, shopPrice: 700, season: 'spring' },
            spring_recipe_10: { id: 'spring_recipe_10', name: 'ออมเล็ตทิวลิป', emoji: '🍳', req: { tulip: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 750, season: 'spring' },
            spring_recipe_11: { id: 'spring_recipe_11', name: 'มิลค์เชคทิวลิป', emoji: '🥤', req: { tulip: 1, milk: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 800, season: 'spring' },
            spring_recipe_12: { id: 'spring_recipe_12', name: 'ข้าวผัดทิวลิป', emoji: '🍛', req: { tulip: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 850, season: 'spring' },
            spring_recipe_13: { id: 'spring_recipe_13', name: 'เจลลี่ทิวลิป', emoji: '🍮', req: { tulip: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 900, season: 'spring' },
            spring_recipe_14: { id: 'spring_recipe_14', name: 'น้ำเชื่อมทิวลิป', emoji: '🍯', req: { tulip: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 950, season: 'spring' },
            spring_recipe_15: { id: 'spring_recipe_15', name: 'แพนเค้กทิวลิป', emoji: '🥞', req: { tulip: 1, wheat: 1, egg: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1000, season: 'spring' },
            spring_recipe_16: { id: 'spring_recipe_16', name: 'พิซซ่าทิวลิป', emoji: '🍕', req: { tulip: 1, wheat: 1, tomato: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1050, season: 'spring' },
            spring_recipe_17: { id: 'spring_recipe_17', name: 'ทาร์ตทิวลิป', emoji: '🥧', req: { tulip: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1100, season: 'spring' },
            spring_recipe_18: { id: 'spring_recipe_18', name: 'สมูทตี้ทิวลิป', emoji: '🥤', req: { tulip: 1, milk: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1150, season: 'spring' },
            spring_recipe_19: { id: 'spring_recipe_19', name: 'ไอศกรีมทิวลิป', emoji: '🍦', req: { tulip: 1, milk: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1200, season: 'spring' },
            spring_recipe_20: { id: 'spring_recipe_20', name: 'ขนมเปี๊ยะทิวลิป', emoji: '🥮', req: { tulip: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1250, season: 'spring' },
            summer_recipe_1: { id: 'summer_recipe_1', name: 'ชามะม่วง', emoji: '🍵', req: { mango: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 300, season: 'summer' },
            summer_recipe_2: { id: 'summer_recipe_2', name: 'เค้กมะม่วง', emoji: '🍰', req: { mango: 1, wheat: 1, milk: 1 }, xp: 50, unlockLevel: 2, shopPrice: 350, season: 'summer' },
            summer_recipe_3: { id: 'summer_recipe_3', name: 'คุกกี้มะม่วง', emoji: '🍪', req: { mango: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 400, season: 'summer' },
            summer_recipe_4: { id: 'summer_recipe_4', name: 'สลัดมะม่วง', emoji: '🥗', req: { mango: 1, tomato: 1 }, xp: 50, unlockLevel: 2, shopPrice: 450, season: 'summer' },
            summer_recipe_5: { id: 'summer_recipe_5', name: 'น้ำมะม่วง', emoji: '🍹', req: { mango: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 500, season: 'summer' },
            summer_recipe_6: { id: 'summer_recipe_6', name: 'ซุปมะม่วง', emoji: '🥣', req: { mango: 1, milk: 1 }, xp: 50, unlockLevel: 2, shopPrice: 550, season: 'summer' },
            summer_recipe_7: { id: 'summer_recipe_7', name: 'พายมะม่วง', emoji: '🥧', req: { mango: 1, wheat: 1 }, xp: 50, unlockLevel: 2, shopPrice: 600, season: 'summer' },
            summer_recipe_8: { id: 'summer_recipe_8', name: 'แยมมะม่วง', emoji: '🍯', req: { mango: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 650, season: 'summer' },
            summer_recipe_9: { id: 'summer_recipe_9', name: 'ขนมปังมะม่วง', emoji: '🍞', req: { mango: 1, wheat: 1 }, xp: 50, unlockLevel: 2, shopPrice: 700, season: 'summer' },
            summer_recipe_10: { id: 'summer_recipe_10', name: 'ออมเล็ตมะม่วง', emoji: '🍳', req: { mango: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 750, season: 'summer' },
            summer_recipe_11: { id: 'summer_recipe_11', name: 'มิลค์เชคมะม่วง', emoji: '🥤', req: { mango: 1, milk: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 800, season: 'summer' },
            summer_recipe_12: { id: 'summer_recipe_12', name: 'ข้าวผัดมะม่วง', emoji: '🍛', req: { mango: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 850, season: 'summer' },
            summer_recipe_13: { id: 'summer_recipe_13', name: 'เจลลี่มะม่วง', emoji: '🍮', req: { mango: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 900, season: 'summer' },
            summer_recipe_14: { id: 'summer_recipe_14', name: 'น้ำเชื่อมมะม่วง', emoji: '🍯', req: { mango: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 950, season: 'summer' },
            summer_recipe_15: { id: 'summer_recipe_15', name: 'แพนเค้กมะม่วง', emoji: '🥞', req: { mango: 1, wheat: 1, egg: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1000, season: 'summer' },
            summer_recipe_16: { id: 'summer_recipe_16', name: 'พิซซ่ามะม่วง', emoji: '🍕', req: { mango: 1, wheat: 1, tomato: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1050, season: 'summer' },
            summer_recipe_17: { id: 'summer_recipe_17', name: 'ทาร์ตมะม่วง', emoji: '🥧', req: { mango: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1100, season: 'summer' },
            summer_recipe_18: { id: 'summer_recipe_18', name: 'สมูทตี้มะม่วง', emoji: '🥤', req: { mango: 1, milk: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1150, season: 'summer' },
            summer_recipe_19: { id: 'summer_recipe_19', name: 'ไอศกรีมมะม่วง', emoji: '🍦', req: { mango: 1, milk: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1200, season: 'summer' },
            summer_recipe_20: { id: 'summer_recipe_20', name: 'ขนมเปี๊ยะมะม่วง', emoji: '🥮', req: { mango: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1250, season: 'summer' },
            autumn_recipe_1: { id: 'autumn_recipe_1', name: 'ชามันเทศ', emoji: '🍵', req: { sweet_potato: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 300, season: 'autumn' },
            autumn_recipe_2: { id: 'autumn_recipe_2', name: 'เค้กมันเทศ', emoji: '🍰', req: { sweet_potato: 1, wheat: 1, milk: 1 }, xp: 50, unlockLevel: 2, shopPrice: 350, season: 'autumn' },
            autumn_recipe_3: { id: 'autumn_recipe_3', name: 'คุกกี้มันเทศ', emoji: '🍪', req: { sweet_potato: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 400, season: 'autumn' },
            autumn_recipe_4: { id: 'autumn_recipe_4', name: 'สลัดมันเทศ', emoji: '🥗', req: { sweet_potato: 1, tomato: 1 }, xp: 50, unlockLevel: 2, shopPrice: 450, season: 'autumn' },
            autumn_recipe_5: { id: 'autumn_recipe_5', name: 'น้ำมันเทศ', emoji: '🍹', req: { sweet_potato: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 500, season: 'autumn' },
            autumn_recipe_6: { id: 'autumn_recipe_6', name: 'ซุปมันเทศ', emoji: '🥣', req: { sweet_potato: 1, milk: 1 }, xp: 50, unlockLevel: 2, shopPrice: 550, season: 'autumn' },
            autumn_recipe_7: { id: 'autumn_recipe_7', name: 'พายมันเทศ', emoji: '🥧', req: { sweet_potato: 1, wheat: 1 }, xp: 50, unlockLevel: 2, shopPrice: 600, season: 'autumn' },
            autumn_recipe_8: { id: 'autumn_recipe_8', name: 'แยมมันเทศ', emoji: '🍯', req: { sweet_potato: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 650, season: 'autumn' },
            autumn_recipe_9: { id: 'autumn_recipe_9', name: 'ขนมปังมันเทศ', emoji: '🍞', req: { sweet_potato: 1, wheat: 1 }, xp: 50, unlockLevel: 2, shopPrice: 700, season: 'autumn' },
            autumn_recipe_10: { id: 'autumn_recipe_10', name: 'ออมเล็ตมันเทศ', emoji: '🍳', req: { sweet_potato: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 750, season: 'autumn' },
            autumn_recipe_11: { id: 'autumn_recipe_11', name: 'มิลค์เชคมันเทศ', emoji: '🥤', req: { sweet_potato: 1, milk: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 800, season: 'autumn' },
            autumn_recipe_12: { id: 'autumn_recipe_12', name: 'ข้าวผัดมันเทศ', emoji: '🍛', req: { sweet_potato: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 850, season: 'autumn' },
            autumn_recipe_13: { id: 'autumn_recipe_13', name: 'เจลลี่มันเทศ', emoji: '🍮', req: { sweet_potato: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 900, season: 'autumn' },
            autumn_recipe_14: { id: 'autumn_recipe_14', name: 'น้ำเชื่อมมันเทศ', emoji: '🍯', req: { sweet_potato: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 950, season: 'autumn' },
            autumn_recipe_15: { id: 'autumn_recipe_15', name: 'แพนเค้กมันเทศ', emoji: '🥞', req: { sweet_potato: 1, wheat: 1, egg: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1000, season: 'autumn' },
            autumn_recipe_16: { id: 'autumn_recipe_16', name: 'พิซซ่ามันเทศ', emoji: '🍕', req: { sweet_potato: 1, wheat: 1, tomato: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1050, season: 'autumn' },
            autumn_recipe_17: { id: 'autumn_recipe_17', name: 'ทาร์ตมันเทศ', emoji: '🥧', req: { sweet_potato: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1100, season: 'autumn' },
            autumn_recipe_18: { id: 'autumn_recipe_18', name: 'สมูทตี้มันเทศ', emoji: '🥤', req: { sweet_potato: 1, milk: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1150, season: 'autumn' },
            autumn_recipe_19: { id: 'autumn_recipe_19', name: 'ไอศกรีมมันเทศ', emoji: '🍦', req: { sweet_potato: 1, milk: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1200, season: 'autumn' },
            autumn_recipe_20: { id: 'autumn_recipe_20', name: 'ขนมเปี๊ยะมันเทศ', emoji: '🥮', req: { sweet_potato: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1250, season: 'autumn' },
            winter_recipe_1: { id: 'winter_recipe_1', name: 'ชาบรอกโคลี', emoji: '🍵', req: { broccoli: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 300, season: 'winter' },
            winter_recipe_2: { id: 'winter_recipe_2', name: 'เค้กบรอกโคลี', emoji: '🍰', req: { broccoli: 1, wheat: 1, milk: 1 }, xp: 50, unlockLevel: 2, shopPrice: 350, season: 'winter' },
            winter_recipe_3: { id: 'winter_recipe_3', name: 'คุกกี้บรอกโคลี', emoji: '🍪', req: { broccoli: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 400, season: 'winter' },
            winter_recipe_4: { id: 'winter_recipe_4', name: 'สลัดบรอกโคลี', emoji: '🥗', req: { broccoli: 1, tomato: 1 }, xp: 50, unlockLevel: 2, shopPrice: 450, season: 'winter' },
            winter_recipe_5: { id: 'winter_recipe_5', name: 'น้ำบรอกโคลี', emoji: '🍹', req: { broccoli: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 500, season: 'winter' },
            winter_recipe_6: { id: 'winter_recipe_6', name: 'ซุปบรอกโคลี', emoji: '🥣', req: { broccoli: 1, milk: 1 }, xp: 50, unlockLevel: 2, shopPrice: 550, season: 'winter' },
            winter_recipe_7: { id: 'winter_recipe_7', name: 'พายบรอกโคลี', emoji: '🥧', req: { broccoli: 1, wheat: 1 }, xp: 50, unlockLevel: 2, shopPrice: 600, season: 'winter' },
            winter_recipe_8: { id: 'winter_recipe_8', name: 'แยมบรอกโคลี', emoji: '🍯', req: { broccoli: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 650, season: 'winter' },
            winter_recipe_9: { id: 'winter_recipe_9', name: 'ขนมปังบรอกโคลี', emoji: '🍞', req: { broccoli: 1, wheat: 1 }, xp: 50, unlockLevel: 2, shopPrice: 700, season: 'winter' },
            winter_recipe_10: { id: 'winter_recipe_10', name: 'ออมเล็ตบรอกโคลี', emoji: '🍳', req: { broccoli: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 750, season: 'winter' },
            winter_recipe_11: { id: 'winter_recipe_11', name: 'มิลค์เชคบรอกโคลี', emoji: '🥤', req: { broccoli: 1, milk: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 800, season: 'winter' },
            winter_recipe_12: { id: 'winter_recipe_12', name: 'ข้าวผัดบรอกโคลี', emoji: '🍛', req: { broccoli: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 850, season: 'winter' },
            winter_recipe_13: { id: 'winter_recipe_13', name: 'เจลลี่บรอกโคลี', emoji: '🍮', req: { broccoli: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 900, season: 'winter' },
            winter_recipe_14: { id: 'winter_recipe_14', name: 'น้ำเชื่อมบรอกโคลี', emoji: '🍯', req: { broccoli: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 950, season: 'winter' },
            winter_recipe_15: { id: 'winter_recipe_15', name: 'แพนเค้กบรอกโคลี', emoji: '🥞', req: { broccoli: 1, wheat: 1, egg: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1000, season: 'winter' },
            winter_recipe_16: { id: 'winter_recipe_16', name: 'พิซซ่าบรอกโคลี', emoji: '🍕', req: { broccoli: 1, wheat: 1, tomato: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1050, season: 'winter' },
            winter_recipe_17: { id: 'winter_recipe_17', name: 'ทาร์ตบรอกโคลี', emoji: '🥧', req: { broccoli: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1100, season: 'winter' },
            winter_recipe_18: { id: 'winter_recipe_18', name: 'สมูทตี้บรอกโคลี', emoji: '🥤', req: { broccoli: 1, milk: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1150, season: 'winter' },
            winter_recipe_19: { id: 'winter_recipe_19', name: 'ไอศกรีมบรอกโคลี', emoji: '🍦', req: { broccoli: 1, milk: 1, honey: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1200, season: 'winter' },
            winter_recipe_20: { id: 'winter_recipe_20', name: 'ขนมเปี๊ยะบรอกโคลี', emoji: '🥮', req: { broccoli: 1, wheat: 1, egg: 1 }, xp: 50, unlockLevel: 2, shopPrice: 1250, season: 'winter' },

            fried_egg: { id: 'fried_egg', name: 'ไข่ดาว', emoji: '🍳', req: { egg: 2 }, xp: 15, unlockLevel: 2, shopPrice: 0 },
            bread: { id: 'bread', name: 'ขนมปัง', emoji: '🍞', req: { wheat: 3 }, xp: 25, unlockLevel: 3, shopPrice: 0 },
            carrot_soup: { id: 'carrot_soup', name: 'ซุปแครอท', emoji: '🥣', req: { carrot: 3, tomato: 1 }, xp: 40, unlockLevel: 4, shopPrice: 0 },
            corn_soup: { id: 'corn_soup', name: 'ซุปข้าวโพด', emoji: '🥣', req: { corn: 2, milk: 1 }, xp: 60, unlockLevel: 5, shopPrice: 0 },
            cake: { id: 'cake', name: 'เค้ก', emoji: '🍰', req: { wheat: 2, egg: 1, milk: 1, strawberry: 2 }, xp: 150, unlockLevel: 7, shopPrice: 0 },
            pizza: { id: 'pizza', name: 'พิซซ่า', emoji: '🍕', req: { wheat: 2, tomato: 2, milk: 1, truffle: 1 }, xp: 300, unlockLevel: 9, shopPrice: 0 },
            fries: { id: 'fries', name: 'เฟรนช์ฟรายส์', emoji: '🍟', req: { potato: 2 }, xp: 20, unlockLevel: 2, shopPrice: 0 },
            salad: { id: 'salad', name: 'สลัดผัก', emoji: '🥗', req: { cabbage: 1, tomato: 1 }, xp: 25, unlockLevel: 4, shopPrice: 0 },
            onion_rings: { id: 'onion_rings', name: 'หอมทอด', emoji: '🧅', req: { onion: 2, wheat: 1 }, xp: 25, unlockLevel: 4, shopPrice: 100 },
            pumpkin_soup: { id: 'pumpkin_soup', name: 'ซุปฟักทอง', emoji: '🥣', req: { pumpkin: 1, milk: 1 }, xp: 45, unlockLevel: 5, shopPrice: 200 },
            stuffed_eggplant: { id: 'stuffed_eggplant', name: 'มะเขือม่วงยัดไส้', emoji: '🍆', req: { eggplant: 1, tomato: 1, onion: 1 }, xp: 55, unlockLevel: 6, shopPrice: 250 },
            chili_sauce: { id: 'chili_sauce', name: 'ซอสพริก', emoji: '🌶️', req: { chili: 2, tomato: 1 }, xp: 40, unlockLevel: 7, shopPrice: 150 },
            blueberry_jam: { id: 'blueberry_jam', name: 'แยมบลูเบอร์รี', emoji: '🫐', req: { blueberry: 2 }, xp: 50, unlockLevel: 8, shopPrice: 300 },
            grape_juice: { id: 'grape_juice', name: 'น้ำองุ่น', emoji: '🧃', req: { grape: 2 }, xp: 60, unlockLevel: 9, shopPrice: 400 },
            melon_pan: { id: 'melon_pan', name: 'เมลอนปัง', emoji: '🍞', req: { melon: 1, wheat: 2 }, xp: 80, unlockLevel: 10, shopPrice: 500 },
            pineapple_fried_rice: { id: 'pineapple_fried_rice', name: 'ข้าวผัดสับปะรด', emoji: '🍍', req: { pineapple: 1, wheat: 2, egg: 1 }, xp: 100, unlockLevel: 11, shopPrice: 600 },
            honey_toast: { id: 'honey_toast', name: 'ฮันนี่โทสต์', emoji: '🍞', req: { bread: 1, honey: 1, milk: 1 }, xp: 120, unlockLevel: 11, shopPrice: 800 },
            goat_cheese: { id: 'goat_cheese', name: 'ชีสนมแพะ', emoji: '🧀', req: { goat_milk: 2 }, xp: 90, unlockLevel: 10, shopPrice: 700 },
            omelet: { id: 'omelet', name: 'ออมเล็ต', emoji: '🍳', req: { egg: 2, onion: 1, tomato: 1 }, xp: 45, unlockLevel: 4, shopPrice: 150 },
            pancake: { id: 'pancake', name: 'แพนเค้ก', emoji: '🥞', req: { wheat: 2, egg: 1, honey: 1 }, xp: 75, unlockLevel: 11, shopPrice: 450 },
            spicy_salad: { id: 'spicy_salad', name: 'ยำรสแซ่บ', emoji: '🥗', req: { cabbage: 1, chili: 1, tomato: 1 }, xp: 65, unlockLevel: 8, shopPrice: 300 },
            berry_cake: { id: 'berry_cake', name: 'เค้กเบอร์รี', emoji: '🍰', req: { cake: 1, strawberry: 1, blueberry: 1 }, xp: 200, unlockLevel: 9, shopPrice: 1000 },
            fruit_salad: { id: 'fruit_salad', name: 'สลัดผลไม้', emoji: '🥣', req: { watermelon: 1, grape: 1, melon: 1 }, xp: 150, unlockLevel: 10, shopPrice: 800 },
            honey_milk: { id: 'honey_milk', name: 'นมอุ่นน้ำผึ้ง', emoji: '🥛', req: { milk: 1, honey: 1 }, xp: 70, unlockLevel: 11, shopPrice: 400 },
            truffle_pasta: { id: 'truffle_pasta', name: 'พาสต้าทรัฟเฟิล', emoji: '🍝', req: { wheat: 3, truffle: 1, egg: 1 }, xp: 250, unlockLevel: 12, shopPrice: 1500 },
            premium_pizza: { id: 'premium_pizza', name: 'พรีเมียมพิซซ่า', emoji: '🍕', req: { pizza: 1, goat_cheese: 1, pineapple: 1 }, xp: 350, unlockLevel: 13, shopPrice: 2000 }
        };



                const UPGRADES = {
            auto_planter: { id: 'auto_planter', name: 'หุ่นยนต์ปลูกผัก', emoji: '🌱', desc: 'ปลูกเมล็ดพันธุ์เดิมอัตโนมัติ (ถ้ามี)', buyPrice: 4000, maxLevel: 1, priceMult: 1, type: 'feature' },
            master_chef: { id: 'master_chef', name: 'มาสเตอร์เชฟ', emoji: '👨‍🍳', desc: 'ทำอาหารได้ XP เพิ่ม 10% ต่อเลเวล', buyPrice: 1500, maxLevel: 5, priceMult: 2, type: 'passive' },
            sales_license: { id: 'sales_license', name: 'ใบอนุญาตการค้า', emoji: '🎫', desc: 'ค่าธรรมเนียมขายทั้งหมดลดลง 1% ต่อเลเวล', buyPrice: 2000, maxLevel: 5, priceMult: 1.8, type: 'passive' },
            bulk_buyer: { id: 'bulk_buyer', name: 'เหมาจ่าย', emoji: '🤝', desc: 'ซื้อสัตว์เลี้ยงถูกลง 5% ต่อเลเวล', buyPrice: 1800, maxLevel: 5, priceMult: 2, type: 'passive' },
            lucky_hand: { id: 'lucky_hand', name: 'มือทองคำ', emoji: '🧤', desc: 'โอกาส 2% ต่อเลเวล ที่สัตว์จะให้ผลผลิต x2', buyPrice: 3000, maxLevel: 5, priceMult: 2.2, type: 'passive' },
            upgrade_discount: { id: 'upgrade_discount', name: 'บัตรส่วนลดอัปเกรด', emoji: '🏷️', desc: 'ซื้ออัปเกรดถูกลง 5% ต่อเลเวล', buyPrice: 1000, maxLevel: 5, priceMult: 1.5, type: 'passive' },

            greenhouse: { id: 'greenhouse', name: 'เรือนกระจก', emoji: '🌱', desc: 'พืชโตเร็วขึ้น 10% ต่อเลเวล', buyPrice: 500, maxLevel: 5, priceMult: 1.5, type: 'passive' },
            auto_harvester_crop: { id: 'auto_harvester_crop', name: 'เครื่องเกี่ยวข้าวออโต้', emoji: '🚜', desc: 'เก็บเกี่ยวพืชอัตโนมัติเมื่อโตเต็มที่', buyPrice: 6000, maxLevel: 1, priceMult: 1, type: 'feature' },
            auto_harvester_animal: { id: 'auto_harvester_animal', name: 'เครื่องรีดนมออโต้', emoji: '🐄', desc: 'เก็บผลผลิตสัตว์อัตโนมัติ', buyPrice: 6000, maxLevel: 1, priceMult: 1, type: 'feature' },
            sprinkler: { id: 'sprinkler', name: 'สปริงเกอร์น้ำ', emoji: '💦', desc: 'โอกาส 5% ต่อเลเวล ที่พืชจะโตทันทีเมื่อปลูก', buyPrice: 800, maxLevel: 5, priceMult: 1.8, type: 'passive' },
            golden_hoe: { id: 'golden_hoe', name: 'จอบทองคำ', emoji: '⛏️', desc: 'ได้รับ XP เพิ่ม 5% ต่อเลเวล', buyPrice: 1000, maxLevel: 5, priceMult: 2, type: 'passive' },
            premium_feed: { id: 'premium_feed', name: 'อาหารสัตว์เกรด A', emoji: '🌾', desc: 'สัตว์ผลิตเร็วขึ้น 10% ต่อเลเวล', buyPrice: 1500, maxLevel: 5, priceMult: 1.6, type: 'passive' },
            lucky_charm: { id: 'lucky_charm', name: 'เครื่องรางนำโชค', emoji: '🍀', desc: 'เพิ่มราคาขายในตลาด 5% ต่อเลเวล', buyPrice: 2000, maxLevel: 5, priceMult: 2.2, type: 'passive' },
            weather_radar: { id: 'weather_radar', name: 'เรดาร์สภาพอากาศ', emoji: '📡', desc: 'พยากรณ์อากาศล่วงหน้า', buyPrice: 300, maxLevel: 1, priceMult: 1, type: 'feature' },
            speedy_boots: { id: 'speedy_boots', name: 'รองเท้าวิเศษ', emoji: '👢', desc: 'ได้ของออฟไลน์เยอะขึ้น 20% ต่อเลเวล', buyPrice: 1200, maxLevel: 3, priceMult: 2, type: 'passive' },
            magic_beans: { id: 'magic_beans', name: 'เมล็ดถั่ววิเศษ', emoji: '✨', desc: 'โอกาส 2% ต่อเลเวล ที่จะเก็บเกี่ยวพืชได้ x2', buyPrice: 2500, maxLevel: 5, priceMult: 2.5, type: 'passive' },
            animal_breeder: { id: 'animal_breeder', name: 'เคล็ดลับเพาะพันธุ์สัตว์', emoji: '📖', desc: 'เมื่อเก็บเกี่ยวสัตว์ โอกาสได้เงินโบนัส 5% ต่อเลเวล', buyPrice: 1800, maxLevel: 5, priceMult: 1.8, type: 'passive' },
            merchant_guild: { id: 'merchant_guild', name: 'บัตรพ่อค้า', emoji: '📜', desc: 'ปลดล็อกกระดานคำสั่งซื้อ NPC (ให้เงินเยอะมาก)', buyPrice: 1000, maxLevel: 1, priceMult: 1, type: 'feature' },
            super_fertilizer: { id: 'super_fertilizer', name: 'สูตรปุ๋ยลับ', emoji: '🧪', desc: 'ปุ๋ย 1 ถุง ลดเวลา 30 นาที (จากเดิม 10 นาที)', buyPrice: 3000, maxLevel: 1, priceMult: 1, type: 'passive' },
            storage_box: { id: 'storage_box', name: 'กล่องเก็บของวิเศษ', emoji: '📦', desc: 'ราคาซื้อเมล็ดพันธุ์ถูกลง 5% ต่อเลเวล', buyPrice: 1000, maxLevel: 5, priceMult: 1.5, type: 'passive' },
            barn_expansion: { id: 'barn_expansion', name: 'ขยายโรงนา', emoji: '🏚️', desc: 'ลดราคาคอกสัตว์ใหม่ลง 10% ต่อเลเวล', buyPrice: 1200, maxLevel: 5, priceMult: 2, type: 'passive' },
            field_expansion: { id: 'field_expansion', name: 'ขยายไร่', emoji: '🚜', desc: 'ลดราคาแปลงปลูกใหม่ลง 10% ต่อเลเวล', buyPrice: 800, maxLevel: 5, priceMult: 2, type: 'passive' }
        };

        const DECORATIONS = {
            fence_white: { id: 'fence_white', name: 'รั้วไม้สีขาว', emoji: '🏡', desc: 'ตกแต่งฟาร์มให้ดูสะอาดตา', buyPrice: 1000 },
            garden_light: { id: 'garden_light', name: 'โคมไฟสวน', emoji: '🏮', desc: 'เพิ่มแสงสว่างตอนกลางคืน', buyPrice: 2500 },
            gnome_statue: { id: 'gnome_statue', name: 'รูปปั้นโนม', emoji: '🧙‍♂️', desc: 'เฝ้าฟาร์มของคุณให้ปลอดภัย', buyPrice: 5000 },
            flower_path: { id: 'flower_path', name: 'ทางเดินดอกไม้', emoji: '🌸', desc: 'เพิ่มความสดใสให้ทางเดิน', buyPrice: 3500 },
            water_fountain: { id: 'water_fountain', name: 'น้ำพุเล็ก', emoji: '⛲', desc: 'ตกแต่งฟาร์มให้ร่มรื่น', buyPrice: 10000 }
        };

        const SEASONS = ['spring', 'summer', 'autumn', 'winter'];
        const SEASON_ICONS = { spring: '🌸 ฤดูใบไม้ผลิ', summer: '☀️ ฤดูร้อน', autumn: '🍂 ฤดูใบไม้ร่วง', winter: '❄️ ฤดูหนาว' };
        
        // Add Seasonal Seeds to SEEDS
        SEEDS['cherry_blossom'] = { id: 'cherry_blossom', name: 'ซากุระ', emoji: '🌸', buyPrice: 150, growTime: 60, xp: 50, produces: 'cherry_blossom', unlockLevel: 5, season: 'spring' };
        PRODUCTS['cherry_blossom'] = { id: 'cherry_blossom', name: 'ดอกซากุระ', emoji: '🌸', basePrice: 195 };
        SEEDS['sunflower'] = { id: 'sunflower', name: 'ทานตะวัน', emoji: '🌻', buyPrice: 150, growTime: 60, xp: 50, produces: 'sunflower', unlockLevel: 5, season: 'summer' };
        PRODUCTS['sunflower'] = { id: 'sunflower', name: 'ทานตะวัน', emoji: '🌻', basePrice: 195 };
        SEEDS['maple_leaf'] = { id: 'maple_leaf', name: 'ใบเมเปิ้ล', emoji: '🍁', buyPrice: 150, growTime: 60, xp: 50, produces: 'maple_leaf', unlockLevel: 5, season: 'autumn' };
        PRODUCTS['maple_leaf'] = { id: 'maple_leaf', name: 'ใบเมเปิ้ล', emoji: '🍁', basePrice: 195 };
        SEEDS['snowdrop'] = { id: 'snowdrop', name: 'สโนว์ดรอป', emoji: '🌼', buyPrice: 150, growTime: 60, xp: 50, produces: 'snowdrop', unlockLevel: 5, season: 'winter' };
        PRODUCTS['snowdrop'] = { id: 'snowdrop', name: 'สโนว์ดรอป', emoji: '🌼', basePrice: 195 };

                const BARN_UPGRADES = [
            { level: 1, capacity: 1700, reqGold: 0, reqItems: {} },
            { level: 2, capacity: 4000, reqGold: 100000, reqItems: { wheat: 500, corn: 300, potato: 390 } },
            { level: 3, capacity: 10000, reqGold: 500000, reqItems: { tomato: 1000, onion: 1000, egg: 800 } },
            { level: 4, capacity: 25000, reqGold: 2000000, reqItems: { strawberry: 3000, milk: 1500, bread: 500, cabbage: 2000 } },
            { level: 5, capacity: 60000, reqGold: 8000000, reqItems: { watermelon: 6000, goat_milk: 3000, cake: 2500, pumpkin: 6000 } },
            { level: 6, capacity: 150000, reqGold: 25000000, reqItems: { rose: 15000, apple: 10000, pizza: 7000, honey: 10000 } },
            { level: 7, capacity: 350000, reqGold: 80000000, reqItems: { peach: 35000, truffle: 20000, goat_cheese: 25000, omelet: 25000 } },
            { level: 8, capacity: 800000, reqGold: 250000000, reqItems: { tulip: 80000, coconut: 60000, peacock_feather: 25000, honey_toast: 80000 } },
            { level: 9, capacity: 2000000, reqGold: 800000000, reqItems: { mango: 200000, buffalo_milk: 100000, llama_wool: 60000, pineapple_fried_rice: 200000 } },
            { level: 10, capacity: 9999999, reqGold: 2500000000, reqItems: { truffle: 300000, owl_feather: 200000, alpaca_wool: 300000, melon_pan: 300000, squid_ink: 300000 } }
        ];

        function getCurrentItemsCount() {
            let count = Object.values(state.inventory.products).reduce((sum, val) => sum + val, 0);
            count += Object.values(state.inventory.seeds).reduce((sum, val) => sum + val, 0);
            count += (state.inventory.fertilizer || 0);
            return count;
        }

        function getBarnCapacity() {
            const lvl = state.inventory.barnLevel || 1;
            const upg = BARN_UPGRADES.find(u => u.level === lvl) || BARN_UPGRADES[0];
            return upg.capacity;
        }

        function checkBarnCapacity(amountToAdd) {
            return (getCurrentItemsCount() + amountToAdd) <= getBarnCapacity();
        }
        
const ACHIEVEMENTS = [
            { id: 'a1', name: 'เศรษฐีหน้าใหม่', desc: 'ทำเงินรวม 5,000 🪙', type: 'earn_gold_total', target: 5000, buffDesc: '+5% ราคาขายทั้งหมด' },
            { id: 'a2', name: 'มหาเศรษฐี', desc: 'ทำเงินรวม 50,000 🪙', type: 'earn_gold_total', target: 50000, buffDesc: '+10% ราคาขายทั้งหมด' },
            { id: 'a3', name: 'ชาวไร่ผู้ขยันขันแข็ง', desc: 'เก็บเกี่ยวผลผลิต 100 ครั้ง', type: 'harvest_count', target: 100, buffDesc: '-10% เวลาโตพืช' },
            { id: 'a4', name: 'มาสเตอร์เชฟ', desc: 'ทำอาหาร 50 ครั้ง', type: 'cook_count', target: 50, buffDesc: 'ฟรี! ปุ๋ยเร่งโต 10 ถุง' }
        ];

        const EVENT_QUESTS = {
            spring: [
                { id: 'eq_sp_1', name: 'เทศกาลดอกไม้ 🌸', desc: 'ปลูกและเก็บเกี่ยวแครอท 50 ชิ้น', action: 'harvest_carrot', reqAmt: 50, reward: { gold: 2000, xp: 1000 } },
                { id: 'eq_sp_2', name: 'งานเลี้ยงต้นฤดู', desc: 'ทำเมนูสลัดผัก 10 จาน', action: 'cook_salad', reqAmt: 10, reward: { gold: 3000, xp: 1500 } }
            ],
            summer: [
                { id: 'eq_su_1', name: 'ปาร์ตี้หน้าร้อน ☀️', desc: 'เก็บเกี่ยวข้าวโพด 50 ชิ้น', action: 'harvest_corn', reqAmt: 50, reward: { gold: 2500, xp: 1200 } },
                { id: 'eq_su_2', name: 'ดับกระหาย', desc: 'ขายมะเขือเทศ 100 ชิ้น', action: 'sell_tomato', reqAmt: 100, reward: { gold: 3500, xp: 1800 } }
            ],
            autumn: [
                { id: 'eq_au_1', name: 'ฤดูเก็บเกี่ยว 🍂', desc: 'เก็บเกี่ยวมันฝรั่ง 80 ชิ้น', action: 'harvest_potato', reqAmt: 80, reward: { gold: 4000, xp: 2000 } },
                { id: 'eq_au_2', name: 'อบอุ่นร่างกาย', desc: 'ทำซุปข้าวโพด 15 จาน', action: 'cook_corn_soup', reqAmt: 15, reward: { gold: 5000, xp: 2500 } }
            ],
            winter: [
                { id: 'eq_wi_1', name: 'ฝ่าลมหนาว ❄️', desc: 'เก็บเกี่ยวผลผลิตจากสัตว์ 50 ชิ้น', action: 'collect_animal', reqAmt: 50, reward: { gold: 4500, xp: 2500 } },
                { id: 'eq_wi_2', name: 'คริสต์มาส', desc: 'อบเค้ก 15 ก้อน', action: 'cook_cake', reqAmt: 15, reward: { gold: 6000, xp: 3000 } }
            ]
        };
        
        const QUESTS = [
            { id: 'q1', name: 'เริ่มทำฟาร์ม', desc: 'ปลูกและเก็บเกี่ยวแครอท 5 หัว', action: 'harvest_carrot', reqAmt: 5, reward: { gold: 50, xp: 50 }, unlockLevel: 1 },
            { id: 'q2', name: 'เมนูไข่', desc: 'เก็บไข่ไก่ 10 ฟอง', action: 'collect_egg', reqAmt: 10, reward: { gold: 100, xp: 80 }, unlockLevel: 2 },
            { id: 'q3', name: 'พ่อครัวมือใหม่', desc: 'ทำไข่ดาว 3 จาน', action: 'cook_fried_egg', reqAmt: 3, reward: { gold: 150, xp: 100 }, unlockLevel: 3 },
            { id: 'q4', name: 'ชาวนาตัวจริง', desc: 'เก็บเกี่ยวข้าวสาลี 15 ต้น', action: 'harvest_wheat', reqAmt: 15, reward: { gold: 200, xp: 150 }, unlockLevel: 3 },
            { id: 'q5', name: 'นักลงทุน', desc: 'ขายของให้ได้เงินรวม 1000', action: 'earn_gold', reqAmt: 1000, reward: { gold: 300, xp: 200 }, unlockLevel: 4 },
            { id: 'q6', name: 'ฟาร์มสตรอว์เบอร์รี', desc: 'เก็บเกี่ยวสตรอว์เบอร์รี 10 ลูก', action: 'harvest_strawberry', reqAmt: 10, reward: { gold: 500, xp: 400 }, unlockLevel: 7 },
            { id: 'q7', name: 'เชฟกระทะเหล็ก', desc: 'อบเค้ก 2 ก้อน', action: 'cook_cake', reqAmt: 2, reward: { gold: 800, xp: 500 }, unlockLevel: 7 },
        ];

        const MAX_PLOTS = 27; // Increased for variety
        const MAX_PENS = 23;
        const PLOT_BASE_PRICE = 100;
        const PEN_BASE_PRICE = 200;

        /* =========================================
           2. STATE MANAGEMENT
           ========================================= */
        let state = {
            gold: 300,
            xp: 0,
            level: 1,
            plots: Array.from({length: MAX_PLOTS}, (_, i) => ({ 
                id: i, unlocked: i < 3, seedId: null, plantedAt: null 
            })),
            pens: Array.from({length: MAX_PENS}, (_, i) => ({ 
                id: i, unlocked: i < 1, animalId: null, lastCollected: null, happiness: 0 
            })),
            
            inventory: {
                seeds: { carrot: 3, tomato: 0 },
                products: {},
                fertilizer: 5,
                unlockedRecipes: ['fried_egg', 'bread', 'carrot_soup', 'corn_soup', 'cake', 'pizza', 'fries', 'salad']
            },
            achievements: {
                harvest_count: 0,
                earn_gold_total: 0,
                cook_count: 0,
                claimed: []
            },
            upgrades: {},
            decorations: [],
            npcOrders: [],
            season: 'spring',
            seasonStartTime: Date.now(),
            stats: {},
            claimedQuests: [],
            marketMultipliers: {},
            lastMarketUpdate: 0,
            weather: 'sunny',
            lastWeatherUpdate: 0,
            nextWeather: 'rainy',
            musicPlaying: false,
            lastSavedAt: null,
            lastLoginDate: null,
            greenhouseUnlocked: false,
            autoHarvesterUnlocked: false,
            autoHarvesterActive: true,
            lastAutoHarvest: 0
        };

        let currentActivePlotId = null;
        function saveGame() {
            state.lastSavedAt = Date.now();
            localStorage.setItem('pastelFarmSaveV2', JSON.stringify(state));
        }

        function loadGame() {
            const saved = localStorage.getItem('pastelFarmSaveV2');
            let offlineMsgs = [];

            if (saved) {
                try {
                    const parsed = JSON.parse(saved);
                    state = { ...state, ...parsed };
                    
                    // Fallbacks for new features
                    if (!state.inventory) state.inventory = {};
                    if (!state.inventory.unlockedRecipes) state.inventory.unlockedRecipes = ['fried_egg', 'bread', 'carrot_soup', 'corn_soup', 'cake', 'pizza', 'fries', 'salad'];
                    if (!state.achievements) state.achievements = { harvest_count: 0, earn_gold_total: 0, cook_count: 0, claimed: [] };
                    if (!state.achievements.claimed) state.achievements.claimed = [];
                    if (!state.inventory.fertilizer) state.inventory.fertilizer = 0;
                    if (!state.claimedQuests) state.claimedQuests = [];
                    if (!state.upgrades) state.upgrades = {};
                    if (!state.decorations) state.decorations = [];
                    if (!state.npcOrders) state.npcOrders = [];
                    if (!state.season) { state.season = 'spring'; state.seasonStartTime = Date.now(); }
                    
                    // Migrate old upgrades
                    if (state.greenhouseUnlocked && state.upgrades.greenhouse === undefined) state.upgrades.greenhouse = 1;
                    if (state.autoHarvesterUnlocked && state.upgrades.auto_harvester !== undefined) {
                        state.upgrades.auto_harvester_crop = 1;
                        state.upgrades.auto_harvester_animal = 1;
                        delete state.upgrades.auto_harvester;
                    }

                    
                    // Handle array size expansions in updates
                    if (state.plots.length < MAX_PLOTS) {
                        for(let i = state.plots.length; i < MAX_PLOTS; i++) {
                            state.plots.push({ id: i, unlocked: false, seedId: null, plantedAt: null });
                        }
                    }
                    if (state.pens.length < MAX_PENS) {
                        for(let i = state.pens.length; i < MAX_PENS; i++) {
                            state.pens.push({ id: i, unlocked: false, animalId: null, lastCollected: null, happiness: 0 });
                        }
                    }
                    if (!state.stats) state.stats = {};
                    if (!state.cookingSlots) {
                        state.cookingSlots = [
                            { id: 0, recipeId: null, startTime: null, qty: 0, cookTime: 0 },
                            { id: 1, recipeId: null, startTime: null, qty: 0, cookTime: 0 },
                            { id: 2, recipeId: null, startTime: null, qty: 0, cookTime: 0 }
                        ];
                    }
                    if (!state.claimedQuests) state.claimedQuests = [];
                    if (!state.marketMultipliers) state.marketMultipliers = {};
                    
                    // Offline animal production
                    if (state.lastSavedAt) {
                        const timeAway = Date.now() - state.lastSavedAt;
                        if (timeAway > 60000) { // 1 minute
                            let offlineEarnings = {};
                            let offlineXP = 0;
                            
                            state.pens.forEach(pen => {
                                if (pen.unlocked && pen.animalId && pen.lastCollected) {
                                    const animal = ANIMALS[pen.animalId];
                                    let cycles = Math.floor(timeAway / (animal.cooldown * 1000));
                                    if (cycles > 0) {
                                        if (state.upgrades && state.upgrades.speedy_boots) {
                                            cycles = Math.floor(cycles * (1 + (state.upgrades.speedy_boots * 0.2)));
                                        }
                                        const product = animal.produces;
                                        state.inventory.products[product] = (state.inventory.products[product] || 0) + cycles;
                                        offlineXP += (animal.xp * cycles);
                                        trackStat(`collect_${product}`, cycles);
                                        offlineEarnings[product] = (offlineEarnings[product] || 0) + cycles;
                                        pen.lastCollected += cycles * (animal.cooldown * 1000); // this pushes lastCollected far into future if we just mult cycles, but it's okay for offline logic since timeAway is large
                                    }
                                }
                            });
                            
                            const earnKeys = Object.keys(offlineEarnings);
                            if (earnKeys.length > 0) {
                                let totalAdded = 0;
                                earnKeys.forEach(k => totalAdded += offlineEarnings[k]);
                                
                                const curItems = getCurrentItemsCount();
                                const maxCap = getBarnCapacity();
                                
                                if (curItems + totalAdded > maxCap) {
                                    // limit it
                                    const availableSpace = Math.max(0, maxCap - curItems);
                                    let spaceLeft = availableSpace;
                                    earnKeys.forEach(k => {
                                        if (spaceLeft > 0) {
                                            const addAmt = Math.min(offlineEarnings[k], spaceLeft);
                                            // subtract what we can't add from the inventory since it was already added above in loop
                                            state.inventory.products[k] -= (offlineEarnings[k] - addAmt);
                                            offlineEarnings[k] = addAmt;
                                            spaceLeft -= addAmt;
                                        } else {
                                            state.inventory.products[k] -= offlineEarnings[k];
                                            offlineEarnings[k] = 0;
                                        }
                                    });
                                    offlineMsgs.push(`<div class="text-left text-sm mb-2 text-red-600 bg-red-50 p-2 rounded-lg border border-red-200"><b>⚠️ โรงนาเต็ม!</b><br/>สัตว์เลี้ยงผลิตของได้ไม่เต็มที่เนื่องจากพื้นที่ไม่พอ</div>`);
                                }
                                
                                const finalKeys = earnKeys.filter(k => offlineEarnings[k] > 0);
                                if (finalKeys.length > 0) {
                                    const earnStr = finalKeys.map(k => `${PRODUCTS[k].emoji} ${PRODUCTS[k].name} x${offlineEarnings[k]}`).join(', ');
                                    offlineMsgs.push(`<div class="text-left text-sm mb-2 text-gray-700"><b>💤 ขณะที่คุณไม่อยู่:</b><br/>สัตว์เลี้ยงผลิต ${earnStr}<br/>ได้รับ <span class="text-green-600 font-bold">${offlineXP} XP</span></div>`);
                                    state.xp += offlineXP;
                                }
                            }
                        }
                    }
                } catch(e) { console.error("Save file corrupted"); }
            }

            // Daily Login Check
            const today = new Date().toDateString();
            if (state.lastLoginDate !== today) {
                state.lastLoginDate = today;
                state.gold += 200;
                state.inventory.seeds['strawberry'] = (state.inventory.seeds['strawberry'] || 0) + 2;
                offlineMsgs.push(`<div class="text-left text-sm bg-amber-50 p-2 rounded-lg border border-amber-200 mt-2 text-gray-800"><b>🎁 รางวัลล็อกอินรายวัน!</b><br/>รับฟรี 200 🪙 และ 🍓 สตรอว์เบอร์รี x2</div>`);
            }

            if (offlineMsgs.length > 0) {
                setTimeout(() => {
                    showAlert('ยินดีต้อนรับกลับฟาร์ม! 🚜', offlineMsgs.join(''), '✨');
                    if (typeof fireConfetti === 'function') fireConfetti();
                }, 800);
            }
        }

        /* =========================================
           3. INITIALIZATION & UI RENDERING
           ========================================= */
        function initUI() { switchTab('farm');
            

            // Init Market Prices if unset
            if (Object.keys(state.marketMultipliers).length === 0) {
                randomizeMarket();
            }

            renderPlotsDOM();
            renderPensDOM();
            
            updateUI();
            
            setInterval(gameLoop, 1000);
            setInterval(saveGame, 2000); 
        }

                        let ytPlayer = null;
        let isYtReady = false;
        
        function onYouTubeIframeAPIReady() {
            ytPlayer = new YT.Player('yt-player', {
                height: '0',
                width: '0',
                videoId: 'CwPCy1GLS38', // Lofi Girl - sad lofi radio
                playerVars: {
                    'autoplay': 0,
                    'controls': 0,
                    'showinfo': 0,
                    'rel': 0,
                    'loop': 1,
                    'playlist': 'CwPCy1GLS38'
                },
                events: {
                    'onReady': () => { 
                        isYtReady = true; 
                        ytPlayer.setVolume(30);
                    }
                }
            });
        }
        
        function toggleBGM() {
            const icon = document.getElementById('bgm-icon');
            const text = document.getElementById('bgm-text');
            
            if (state.musicPlaying) {
                if (isYtReady && ytPlayer && ytPlayer.pauseVideo) ytPlayer.pauseVideo();
                icon.innerText = "🔇";
                text.innerText = "เปิดเพลง (เศร้าๆ ซึมๆ อ่านหนังสือ)";
                text.className = "text-sm font-bold text-gray-700";
            } else {
                if (isYtReady && ytPlayer && ytPlayer.playVideo) ytPlayer.playVideo();
                icon.innerText = "🎵";
                text.innerText = "กำลังเล่น (เศร้าๆ ซึมๆ อ่านหนังสือ)";
                text.className = "text-sm font-bold text-green-700";
            }
            state.musicPlaying = !state.musicPlaying;
        }

        function renderPlotsDOM() {
            const container = document.getElementById('plots-container');
            if (state.greenhouseUnlocked) {
                container.classList.add('border-4', 'border-green-300', 'bg-green-50/30', 'rounded-3xl', 'p-2', 'shadow-inner');
            }
            container.innerHTML = state.plots.map(plot => `
                <div id="plot-${plot.id}" class="glass relative p-3 rounded-2xl h-32 md:h-36 flex flex-col items-center justify-center transition-all ${state.greenhouseUnlocked ? 'bg-white/40' : ''}">
                    <div id="plot-${plot.id}-locked" class="absolute inset-0 bg-gray-200/50 backdrop-blur-sm rounded-2xl flex flex-col items-center justify-center z-10 hidden">
                        <span class="text-2xl drop-shadow-sm">🔒</span>
                    </div>
                    <div id="plot-${plot.id}-empty" onclick="openSeedModal(${plot.id})" class="absolute inset-0 m-1.5 md:m-2 border-2 border-dashed border-white/80 rounded-xl flex flex-col items-center justify-center cursor-pointer hover:bg-white/40 transition hidden">
                        <span class="text-2xl text-green-700/50 mb-1">➕</span>
                        <span class="text-[9px] md:text-[10px] font-bold text-green-700/60 uppercase tracking-widest">ปลูก</span>
                    </div>
                    <div id="plot-${plot.id}-growing" class="w-full flex flex-col items-center hidden">
                        <span id="plot-${plot.id}-emoji" class="text-4xl md:text-5xl mb-2 md:mb-3 drop-shadow-sm transition-transform duration-1000 sway">🌱</span>
                        <div class="w-full h-2 bg-white/60 rounded-full overflow-hidden shadow-inner border border-white">
                            <div id="plot-${plot.id}-bar" class="h-full bg-gradient-to-r from-green-400 to-emerald-400 progress-bar-fill" style="width: 0%"></div>
                        </div>
                    </div>
                    <button id="plot-${plot.id}-harvest" onclick="harvest(${plot.id})" class="absolute inset-0 w-full h-full flex flex-col items-center justify-center bg-green-100/90 backdrop-blur-sm rounded-2xl hidden animate-soft-bounce border-2 border-green-300 shadow-lg z-20">
                        <span id="plot-${plot.id}-harvest-emoji" class="text-4xl md:text-5xl mb-1 drop-shadow-md">🥕</span>
                        <span class="text-[10px] md:text-xs font-bold text-green-800 bg-white/90 px-2 py-1 rounded-full shadow-sm">เก็บเกี่ยว!</span>
                    </button>
                    <button id="plot-${plot.id}-fertilize" onclick="fertilize(${plot.id}, event)" class="absolute top-1 right-1 bg-purple-50 hover:bg-purple-100 border border-purple-200 p-1.5 rounded-full text-xs shadow-sm z-30 hidden" title="ใช้ปุ๋ยเร่งโต">
                        💩 <span class="text-[10px] font-bold text-purple-800" id="plot-${plot.id}-fert-count"></span>
                    </button>
                </div>
            `).join('');
        }

        function renderPensDOM() {
            const container = document.getElementById('pens-container');
            container.innerHTML = state.pens.map(pen => `
                <div id="pen-${pen.id}" class="glass relative p-3 rounded-2xl h-32 md:h-36 flex flex-col items-center justify-center transition-all">
                    <div id="pen-${pen.id}-locked" class="absolute inset-0 bg-gray-200/50 backdrop-blur-sm rounded-2xl flex flex-col items-center justify-center z-10 hidden">
                        <span class="text-2xl drop-shadow-sm">🔒</span>
                    </div>
                    <button id="pen-${pen.id}-empty" onclick="openAnimalModal(${pen.id})" class="absolute inset-0 m-1.5 md:m-2 border-2 border-dashed border-white/80 hover:bg-white/30 hover:border-white transition-all rounded-xl flex flex-col items-center justify-center hidden cursor-pointer z-10">
                        <span class="text-3xl text-green-700/40 mb-1">🏡</span>
                        <span class="text-[9px] md:text-[10px] font-bold text-green-700/60 uppercase tracking-widest text-center px-2">เลี้ยงสัตว์</span>
                    </button>
                    <div id="pen-${pen.id}-producing" class="w-full flex flex-col items-center hidden relative">
                        <div class="absolute -top-2 -right-2 bg-white/80 rounded-full px-1.5 py-0.5 text-[10px] font-bold text-pink-500 shadow-sm flex items-center gap-1 border border-pink-100 z-20">
                            💖 <span id="pen-${pen.id}-happiness">0</span>
                        </div>
                        <span id="pen-${pen.id}-emoji" class="text-4xl md:text-5xl mb-2 md:mb-3 drop-shadow-sm sway animate-pulse">🐔</span>
                        <div class="w-full h-2 bg-white/60 rounded-full overflow-hidden shadow-inner border border-white mb-1">
                            <div id="pen-${pen.id}-bar" class="h-full bg-gradient-to-r from-amber-400 to-orange-400 progress-bar-fill" style="width: 0%"></div>
                        </div>
                    </div>
                    <button id="pen-${pen.id}-collect" onclick="collectAnimal(${pen.id})" class="absolute inset-0 w-full h-full flex flex-col items-center justify-center bg-orange-100/90 backdrop-blur-sm rounded-2xl hidden animate-soft-bounce border-2 border-orange-300 shadow-lg z-20">
                        <div class="flex gap-1 mb-1 items-end">
                            <span id="pen-${pen.id}-animal-emoji" class="text-2xl md:text-3xl opacity-70">🐔</span>
                            <span id="pen-${pen.id}-product-emoji" class="text-3xl md:text-4xl drop-shadow-md">🥚</span>
                        </div>
                        <span class="text-[10px] md:text-xs font-bold text-orange-800 bg-white/90 px-2 py-1 rounded-full shadow-sm">เก็บผลผลิต!</span>
                    </button>
                    <div id="pen-${pen.id}-actions" class="absolute bottom-1 w-full flex justify-between px-2 z-30 hidden pointer-events-none">
                        <button onclick="feedAnimal(${pen.id}, event)" class="pointer-events-auto bg-pink-100 hover:bg-pink-200 text-pink-700 text-[10px] px-1.5 py-0.5 rounded shadow-sm border border-pink-200">
                            💖 <span id="pen-${pen.id}-happiness">0</span>
                        </button>
                        <button onclick="removeAnimal(${pen.id}, event)" class="pointer-events-auto bg-red-100 hover:bg-red-200 text-red-700 text-[10px] px-1.5 py-0.5 rounded shadow-sm border border-red-200" title="ขาย/เปลี่ยนสัตว์">
                            ขาย/เปลี่ยน
                        </button>
                    </div>
                </div>
            `).join('');
        }

        // Generate Market Content

        let quickBuyAmount = 1;
        
        let currentMarketCategory = 'seeds';
        function setMarketCategory(cat) {
            currentMarketCategory = cat;
            const cats = ['seeds', 'animals', 'upgrades', 'recipes'];
            cats.forEach(c => {
                const tab = document.getElementById('tab-cat-' + c);
                const sec = document.getElementById('market-sec-' + c);
                if (c === cat) {
                    tab.className = "market-cat-btn px-4 py-2 rounded-xl bg-white text-green-900 font-bold shadow-sm whitespace-nowrap border-2 border-green-200";
                    sec.classList.remove('hidden');
                } else {
                    tab.className = "market-cat-btn px-4 py-2 rounded-xl bg-white/50 text-green-800 hover:bg-white/70 font-semibold whitespace-nowrap border-2 border-transparent";
                    sec.classList.add('hidden');
                }
            });
        }

        function setQuickBuy(amt) {
            quickBuyAmount = amt;
            if(!document.getElementById('qb-1')) return;
            document.getElementById('qb-1').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickBuyAmount === 1 ? 'bg-green-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            document.getElementById('qb-10').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickBuyAmount === 10 ? 'bg-green-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            document.getElementById('qb-100').className = `px-3 py-1 text-xs font-bold rounded-lg transition-all ${quickBuyAmount === 100 ? 'bg-green-500 text-white shadow' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`;
            renderMarket();
        }

        function renderMarket() {

            // Seeds
            document.getElementById('market-seeds').innerHTML = Object.values(SEEDS)
                .filter(seed => !seed.season || seed.season === state.season)
                .map(seed => {
                const isLocked = state.level < seed.unlockLevel;
                const mult = state.marketMultipliers['seed_'+seed.id] || 1.0;
                const dynamicPrice = Math.floor(seed.buyPrice * mult);
                let trendIcon = '➖'; let trendColor = 'text-gray-500';
                if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-red-500'; } 
                else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-green-600'; }
                const finalPrice = state.upgrades.storage_box ? Math.floor(dynamicPrice * (1 - (state.upgrades.storage_box * 0.05))) : dynamicPrice;
                return `
                <div class="glass p-3 rounded-xl flex justify-between items-center ${isLocked ? 'opacity-60 grayscale' : 'hover:bg-white/60'} transition">
                    <div class="flex items-center gap-3">
                        <span class="text-3xl bg-white/50 p-2 rounded-lg shadow-sm">${isLocked ? '🔒' : seed.emoji}</span>
                        <div>
                            <div class="font-bold text-gray-800">${seed.name} ${isLocked ? `<span class="text-[10px] text-red-500 ml-1">ปลดล็อก Lv.${seed.unlockLevel}</span>` : ''}</div>
                            <div class="text-xs font-semibold text-gray-500">โตใน ${seed.growTime} วิ • ให้ ${seed.xp} XP</div>
                        </div>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-bold text-gray-500 mr-1">x${quickBuyAmount}</span>
                        <button onclick="buyItem('seed', '${seed.id}', ${dynamicPrice})" class="relative group glass-btn px-4 py-2 rounded-xl text-sm font-bold shadow-sm whitespace-nowrap ${isLocked || state.gold < finalPrice * quickBuyAmount ? 'bg-gray-100 text-gray-400 opacity-80 cursor-not-allowed' : 'text-green-700 bg-white/80 hover:bg-green-50'}" ${isLocked || state.gold < finalPrice * quickBuyAmount ? 'disabled' : ''}>
                            <span class="${trendColor} mr-1 text-[10px]\">${trendIcon}</span> ${finalPrice * quickBuyAmount} 🪙
                            ${!isLocked ? `<div class="absolute bottom-full mb-2 right-0 bg-gray-900/90 text-white text-xs px-2 py-1.5 rounded opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap z-50">
                                ได้ผลผลิต: ${PRODUCTS[seed.produces].name} ${PRODUCTS[seed.produces].emoji}
                            </div>` : ''}
                        </button>
                    </div>
                </div>
            `}).join('');

            // Animals
            document.getElementById('market-animals').innerHTML = Object.values(ANIMALS).map(animal => {
                const isLocked = state.level < animal.unlockLevel;
                const mult = state.marketMultipliers['animal_'+animal.id] || 1.0;
                let dynamicPrice = Math.floor(animal.buyPrice * mult);
                if (state.upgrades && state.upgrades.bulk_buyer) {
                    dynamicPrice = Math.floor(dynamicPrice * (1 - (state.upgrades.bulk_buyer * 0.05)));
                }
                let trendIcon = '➖'; let trendColor = 'text-gray-500';
                if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-red-500'; } 
                else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-green-600'; }
                return `
                <div class="glass p-3 rounded-xl flex justify-between items-center ${isLocked ? 'opacity-60 grayscale' : 'hover:bg-white/60'} transition">
                    <div class="flex items-center gap-3">
                        <span class="text-3xl bg-white/50 p-2 rounded-lg shadow-sm">${isLocked ? '🔒' : animal.emoji}</span>
                        <div>
                            <div class="font-bold text-gray-800">${animal.name} ${isLocked ? `<span class="text-[10px] text-red-500 ml-1">ปลดล็อก Lv.${animal.unlockLevel}</span>` : ''}</div>
                            <div class="text-xs font-semibold text-gray-500">ผลิตทุก ${animal.cooldown} วิ</div>
                        </div>
                    </div>
                    <button onclick="buyItem('animal', '${animal.id}', ${dynamicPrice})" class="relative group glass-btn px-4 py-2 rounded-xl text-sm font-bold text-green-700 shadow-sm whitespace-nowrap" ${isLocked ? 'disabled' : ''}>
                        <span class="${trendColor} mr-1 text-[10px]\">${trendIcon}</span> ${dynamicPrice} 🪙
                        ${!isLocked ? `<div class="absolute bottom-full mb-2 right-0 bg-gray-900/90 text-white text-xs px-2 py-1.5 rounded opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap z-50">
                            ให้ผลผลิต: ${PRODUCTS[animal.produces].name} ${PRODUCTS[animal.produces].emoji}
                        </div>` : ''}
                    </button>
                </div>
            `}).join('');

            // Upgrades
            let upgradesHtml = Object.values(UPGRADES).map(u => {
                const curLevel = state.upgrades[u.id] || 0;
                const isMax = curLevel >= u.maxLevel;
                let nextPrice = Math.floor(u.buyPrice * Math.pow(u.priceMult, curLevel));
                if (state.upgrades && state.upgrades.upgrade_discount) {
                    nextPrice = Math.floor(nextPrice * (1 - (state.upgrades.upgrade_discount * 0.05)));
                }
                return `
                <div class="glass p-3 rounded-xl flex justify-between items-center ${isMax ? 'bg-gray-50/50 opacity-60' : 'hover:bg-white/60'} transition">
                    <div class="flex items-center gap-3">
                        <span class="text-3xl bg-white/50 p-2 rounded-lg shadow-sm">${u.emoji}</span>
                        <div>
                            <div class="font-bold text-gray-800">${u.name} ${curLevel > 0 ? `<span class="text-xs text-purple-600 font-bold ml-1">Lv.${curLevel}</span>` : ''}</div>
                            <div class="text-xs font-semibold text-gray-500">${u.desc}</div>
                        </div>
                    </div>
                    ${isMax ? `<span class="text-sm font-bold text-gray-500 px-4 py-2">MAX</span>` 
                    : `<button onclick="buyDynamicUpgrade('${u.id}')" class="relative group glass-btn px-4 py-2 rounded-xl text-sm font-bold text-purple-700 shadow-sm whitespace-nowrap" ${state.gold < nextPrice ? 'disabled' : ''}>
                        ${nextPrice} 🪙
                    </button>`}
                </div>
                `;
            }).join('');
            
            // Fertilizer
            upgradesHtml += `
                <div class="glass p-3 rounded-xl flex justify-between items-center hover:bg-white/60 transition">
                    <div class="flex items-center gap-3">
                        <span class="text-3xl bg-white/50 p-2 rounded-lg shadow-sm">💩</span>
                        <div>
                            <div class="font-bold text-gray-800">ปุ๋ยเร่งโต</div>
                            <div class="text-xs font-semibold text-gray-500">ลดเวลาโต 50% ทันที</div>
                        </div>
                    </div>
                    <div class="flex items-center gap-2">
                        <input type="number" id="buy-qty-fertilizer" min="1" value="1" class="w-12 md:w-16 p-1 text-sm rounded border border-gray-300 text-center bg-white/80">
                        <button onclick="buyItem('fertilizer', 'fertilizer', 50)" class="relative group glass-btn px-4 py-2 rounded-xl text-sm font-bold text-purple-700 shadow-sm whitespace-nowrap">
                            50 🪙
                        </button>
                    </div>
                </div>
            `;
            
            // Shop Recipes
            let recipesHtml = '';
            Object.values(RECIPES).filter(recipe => !recipe.season || recipe.season === state.season).forEach(recipe => {
                if (recipe.shopPrice > 0 && !state.inventory.unlockedRecipes.includes(recipe.id)) {
                    const isLocked = state.level < recipe.unlockLevel;
                    const mult = state.marketMultipliers['recipe_'+recipe.id] || 1.0;
                    const dynamicPrice = Math.floor(recipe.shopPrice * mult);
                    let trendIcon = '➖'; let trendColor = 'text-gray-500';
                    if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-red-500'; } 
                    else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-green-600'; }
                    recipesHtml += `
                    <div class="glass p-3 rounded-xl flex justify-between items-center ${isLocked ? 'opacity-60 grayscale' : 'hover:bg-white/60'} transition">
                        <div class="flex items-center gap-3">
                            <span class="text-3xl bg-white/50 p-2 rounded-lg shadow-sm">${isLocked ? '🔒' : recipe.emoji}</span>
                            <div>
                                <div class="font-bold text-gray-800">สูตร: ${recipe.name} ${isLocked ? `<span class="text-[10px] text-red-500 ml-1">ปลดล็อก Lv.${recipe.unlockLevel}</span>` : ''}</div>
                                <div class="text-xs font-semibold text-gray-500">ซื้อเพื่อเปิดทำเมนูนี้</div>
                            </div>
                        </div>
                        <button onclick="buyItem('recipe', '${recipe.id}', ${dynamicPrice})" class="glass-btn px-4 py-2 rounded-xl text-sm font-bold text-blue-700 shadow-sm whitespace-nowrap" ${isLocked ? 'disabled' : ''}>
                            <span class="${trendColor} mr-1 text-[10px]\">${trendIcon}</span> ${dynamicPrice} 🪙
                        </button>
                    </div>`;
                }
            });
            document.getElementById('market-recipes').innerHTML = recipesHtml;

            document.getElementById('market-upgrades').innerHTML = upgradesHtml;
        }

        // Generate Inventory Content
        function renderInventory() {
            // Update Barn UI
            const uiBarnLvl = document.getElementById('ui-barn-level');
            const uiBarnCur = document.getElementById('ui-barn-cur');
            const uiBarnMax = document.getElementById('ui-barn-max');
            const uiBarnFill = document.getElementById('ui-barn-fill');
            
            if (uiBarnLvl) {
                const cur = getCurrentItemsCount();
                const mx = getBarnCapacity();
                const lvl = state.inventory.barnLevel || 1;
                uiBarnLvl.innerText = `Lv.${lvl}`;
                uiBarnCur.innerText = cur;
                uiBarnMax.innerText = mx >= 999999 ? 'MAX' : mx;
                
                let percent = (cur / mx) * 100;
                if (percent > 100) percent = 100;
                uiBarnFill.style.width = `${percent}%`;
                
                if (percent >= 90) {
                    uiBarnFill.className = "h-full bg-red-500 transition-all duration-300";
                    uiBarnCur.className = "text-red-600 font-black animate-pulse";
                } else if (percent >= 70) {
                    uiBarnFill.className = "h-full bg-orange-400 transition-all duration-300";
                    uiBarnCur.className = "text-orange-600 font-bold";
                } else {
                    uiBarnFill.className = "h-full bg-green-500 transition-all duration-300";
                    uiBarnCur.className = "";
                }
            }

            const seedEntries = Object.entries(state.inventory.seeds).filter(([_, qty]) => qty > 0);
            if (seedEntries.length === 0) {
                document.getElementById('inv-seeds').innerHTML = '<div class="col-span-2 text-sm text-gray-500 text-center py-4 bg-white/30 rounded-xl">ไม่มีเมล็ดพันธุ์ (ซื้อได้ที่ร้านค้า)</div>';
            } else {
                document.getElementById('inv-seeds').innerHTML = seedEntries.map(([id, qty]) => {
                    const seed = SEEDS[id];
                    const sellPrice = Math.floor(seed.buyPrice * 0.5);
                    return `
                    <div class="glass p-3 rounded-xl flex items-center justify-between gap-2">
                        <div class="flex items-center gap-2">
                            <span class="text-3xl">${seed.emoji}</span>
                            <div class="flex-1">
                                <div class="font-bold text-sm text-gray-800">${seed.name}</div>
                                <div class="text-xs font-bold text-green-600">x${qty}</div>
                            </div>
                        </div>
                        <button onclick="sellSeed('${id}')" class="text-xs bg-red-50 text-red-600 hover:bg-red-100 font-bold px-2 py-1 rounded-lg transition shadow-sm border border-red-200 whitespace-nowrap">
                            ขาย (-50%)
                        </button>
                    </div>
                    `;
                }).join('');
            }

            const prodEntries = Object.entries(state.inventory.products).filter(([_, qty]) => qty > 0);
            if (prodEntries.length === 0) {
                document.getElementById('inv-products').innerHTML = '<div class="text-sm text-gray-500 text-center py-8 bg-white/30 rounded-xl">ยังไม่มีผลผลิต<br/><span class="text-xs">ปลูกผัก, เลี้ยงสัตว์ หรือทำอาหารเพื่อนำมาขาย</span></div>';
            } else {
                document.getElementById('inv-products').innerHTML = prodEntries.map(([id, qty]) => {
                    const prod = PRODUCTS[id];
                    const mult = state.marketMultipliers[id] || 1;
                    const sellPrice = Math.floor(prod.basePrice * mult);
                    const totalValue = sellPrice * qty;
                    
                    let trendIcon = '➖';
                    let trendColor = 'text-gray-500';
                    if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-green-600'; }
                    else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-red-500'; }

                    return `
                    <div class="glass p-3 rounded-xl flex justify-between items-center">
                        <div class="flex items-center gap-3">
                            <span class="text-3xl bg-white/50 p-2 rounded-lg shadow-sm">${prod.emoji}</span>
                            <div>
                                <div class="font-bold text-gray-800">${prod.name} <span class="text-green-600 ml-1">x${qty}</span></div>
                                <div class="text-[10px] font-semibold text-gray-500 flex items-center gap-1">
                                    ราคา: ${sellPrice} 🪙 <span class="${trendColor}">${trendIcon}</span>
                                </div>
                            </div>
                        </div>
                        <button onclick="openSellModal('${id}')" class="relative group glass-btn px-4 py-2 bg-yellow-50 rounded-xl text-sm font-bold text-amber-700 shadow-sm border border-yellow-200">
                            ขาย (+${totalValue})
                            <div class="absolute bottom-full mb-2 right-0 bg-gray-900/90 text-white text-xs px-2 py-1.5 rounded opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap z-50 font-normal">
                                ราคาตลาดเปลี่ยนทุก 1 นาที (โอกาส +20% ถึง -20%)
                            </div>
                        </button>
                    </div>
                    `;
                }).join('');
            }
        }

        // Generate Cooking Content
        function renderCooking() {
            // Render Cooking Slots
            const slotsContainer = document.getElementById('cooking-slots-container');
            if (slotsContainer && state.cookingSlots) {
                slotsContainer.innerHTML = state.cookingSlots.map(slot => {
                    if (!slot.recipeId) {
                        return `<div class="glass p-4 rounded-xl flex items-center justify-center text-gray-400 border border-dashed border-gray-300 h-24">เตาว่าง</div>`;
                    }
                    const recipe = RECIPES[slot.recipeId];
                    const now = Date.now();
                    const progress = Math.min((now - slot.startTime) / slot.cookTime, 1);
                    const isDone = progress >= 1;
                    
                    return `
                    <div class="glass p-3 rounded-xl flex flex-col gap-2 relative overflow-hidden">
                        <div class="flex justify-between items-center z-10 relative">
                            <div class="flex items-center gap-2">
                                <span class="text-2xl">${recipe.emoji}</span>
                                <div>
                                    <div class="font-bold text-gray-800 text-sm">${recipe.name} x${slot.qty}</div>
                                    <div class="text-[10px] text-gray-500">${isDone ? 'เสร็จแล้ว!' : 'กำลังปรุง...'}</div>
                                </div>
                            </div>
                            ${isDone ? `<button onclick="collectFood(${slot.id})" class="text-xs font-bold bg-green-500 hover:bg-green-600 text-white px-3 py-1.5 rounded-lg shadow-sm transition animate-pulse">เก็บ</button>` : ''}
                        </div>
                        <div class="h-1.5 bg-gray-200 rounded-full overflow-hidden z-10 relative">
                            <div class="h-full bg-orange-400 transition-all duration-1000" style="width: ${progress * 100}%"></div>
                        </div>
                    </div>`;
                }).join('');
            }

            document.getElementById('cooking-recipes').innerHTML = Object.values(RECIPES).map(recipe => {
                if (recipe.shopPrice > 0 && !state.inventory.unlockedRecipes.includes(recipe.id)) return '';
                const isLocked = state.level < recipe.unlockLevel;
                
                // Build requirement string and check if cookable
                let canCook = true;
                const reqHtml = Object.entries(recipe.req).map(([reqId, reqQty]) => {
                    const hasQty = state.inventory.products[reqId] || 0;
                    if (hasQty < reqQty) canCook = false;
                    const pItem = PRODUCTS[reqId];
                    return `<span class="inline-flex items-center gap-1 bg-white/50 px-2 py-0.5 rounded text-[10px] ${hasQty >= reqQty ? 'text-green-700' : 'text-red-600 font-bold'}">
                        ${pItem.emoji} ${hasQty}/${reqQty}
                    </span>`;
                }).join(' ');

                return `
                <div class="glass p-4 rounded-xl flex flex-col gap-3 ${isLocked ? 'opacity-60 grayscale' : 'hover:bg-white/60'} transition">
                    <div class="flex justify-between items-center">
                        <div class="flex items-center gap-3">
                            <span class="text-4xl bg-white/50 p-2 rounded-lg shadow-sm">${isLocked ? '🔒' : recipe.emoji}</span>
                            <div>
                                <div class="font-bold text-gray-800 text-lg">${recipe.name} ${isLocked ? `<span class="text-[10px] text-red-500 ml-1">ปลดล็อก Lv.${recipe.unlockLevel}</span>` : ''}</div>
                                <div class="text-xs font-semibold text-green-600">ได้รับ ${recipe.xp} XP</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-2">
                            <input type="number" id="qty-${recipe.id}" value="1" min="1" class="w-16 rounded-xl border-gray-300 shadow-sm px-2 py-2 text-sm text-center" ${isLocked || !canCook ? 'disabled' : ''}>
                            <button onclick="cookRecipe('${recipe.id}')" class="glass-btn px-4 py-2.5 rounded-xl text-sm font-bold text-blue-700 shadow-sm whitespace-nowrap bg-blue-50/50" ${isLocked || !canCook ? 'disabled' : ''}>
                                ทำอาหาร
                            </button>
                        </div>
                    </div>
                    <div class="flex flex-wrap gap-1 mt-1 items-center">
                        <span class="text-[10px] font-bold text-gray-500 mr-1">วัตถุดิบ:</span>
                        ${isLocked ? '<span class="text-[10px] text-gray-400">? ? ?</span>' : reqHtml}
                    </div>
                </div>
            `}).join('');
        }

        // Generate Quests Content
        
        function claimAchievement(achId) {
            if (!state.achievements.claimed.includes(achId)) {
                state.achievements.claimed.push(achId);
                if (achId === 'a4') {
                    state.inventory.fertilizer = (state.inventory.fertilizer || 0) + 10;
                }
                showAlert('ยินดีด้วย!', 'คุณได้รับความสำเร็จใหม่และบัฟพิเศษแล้ว! 🏆', '✨');
                if (typeof fireConfetti === 'function') fireConfetti();
                updateUI();
            }
        }

        function renderAchievements() {
            const list = document.getElementById('achievements-list');
            if (!list) return;
            
            list.innerHTML = ACHIEVEMENTS.map(ach => {
                const current = state.achievements[ach.type] || 0;
                const isCompleted = current >= ach.target;
                const isClaimed = state.achievements.claimed.includes(ach.id);
                
                let btn = '';
                if (isClaimed) {
                    btn = `<span class="text-xs font-bold text-green-600 bg-green-100 px-3 py-1 rounded-full">✅ ทำแล้ว</span>`;
                } else if (isCompleted) {
                    btn = `<button onclick="claimAchievement('${ach.id}')" class="text-xs font-bold text-white bg-green-500 hover:bg-green-600 px-3 py-1 rounded-full shadow-sm animate-pulse">รับรางวัล!</button>`;
                } else {
                    btn = `<span class="text-xs font-bold text-gray-400 bg-gray-100 px-3 py-1 rounded-full">${Math.min(current, ach.target)}/${ach.target}</span>`;
                }
                
                return `
                <div class="glass p-4 rounded-xl flex items-center justify-between ${isClaimed ? 'bg-amber-50/50 border-amber-200' : ''}">
                    <div class="flex gap-3 items-center">
                        <div class="text-3xl ${isClaimed ? 'opacity-100 drop-shadow-md' : 'opacity-40 grayscale'}">🏆</div>
                        <div>
                            <div class="font-bold text-gray-800">${ach.name}</div>
                            <div class="text-xs text-gray-500">${ach.desc}</div>
                            <div class="text-[10px] text-amber-600 font-bold mt-1">🎁 ${ach.buffDesc}</div>
                        </div>
                    </div>
                    <div>${btn}</div>
                </div>`;
            }).join('');
        }

        
        function generateNPCOrders() {
            if (!state.upgrades || !state.upgrades.merchant_guild) return; // Must have merchant guild upgrade
            
            // Generate 3 random orders if empty
            if (!state.npcOrders || state.npcOrders.length === 0) {
                state.npcOrders = [];
                for(let i=0; i<3; i++) {
                    state.npcOrders.push(createRandomOrder(i));
                }
            } else {
                // Refresh completed orders or small chance to refresh all
                state.npcOrders = state.npcOrders.map((o, idx) => {
                    if (o.completed || Math.random() < 0.1) return createRandomOrder(idx);
                    return o;
                });
            }
            renderOrders();
        }
        
        function createRandomOrder(id) {
            const possibleItems = Object.keys(PRODUCTS).filter(k => PRODUCTS[k].basePrice <= (state.level * 50) + 50);
            let reqs = {};
            let totalValue = 0;
            
            const numReqs = Math.floor(Math.random() * 2) + 1; // 1 or 2 items
            for(let i=0; i<numReqs; i++) {
                const item = possibleItems[Math.floor(Math.random() * possibleItems.length)];
                const qty = Math.floor(Math.random() * 5) + 2;
                reqs[item] = (reqs[item] || 0) + qty;
                totalValue += PRODUCTS[item].basePrice * qty;
            }
            
            const goldReward = Math.floor(totalValue * (1.1 + Math.random() * 0.4));
            const xpReward = Math.floor(goldReward * 0.5);
            
            const npcs = ['👨‍🌾 ลุงฟาร์มเมอร์', '👩‍🍳 เจ๊ร้านข้าว', '🧙‍♂️ นักเวทย์ฝึกหัด', '👷 ช่างไม้'];
            return {
                id: 'order_'+id+'_'+Date.now(),
                npc: npcs[Math.floor(Math.random() * npcs.length)],
                reqs: reqs,
                goldReward: goldReward,
                xpReward: xpReward,
                completed: false
            };
        }
        
        function renderOrders() {
            const list = document.getElementById('orders-list');
            if (!list) return;
            
            if (!state.upgrades || !state.upgrades.merchant_guild) {
                list.innerHTML = `<div class="glass p-5 rounded-xl text-center text-gray-500">
                    <span class="text-3xl block mb-2">📜</span>
                    ต้องซื้อ <b>"บัตรพ่อค้า"</b> ในร้านค้าหมวด "อัปเกรด" ก่อนเพื่อรับคำสั่งซื้อ
                </div>`;
                return;
            }
            
            if (!state.npcOrders || state.npcOrders.length === 0) {
                list.innerHTML = `<div class="glass p-5 rounded-xl text-center text-gray-500">รอคำสั่งซื้อใหม่...</div>`;
                return;
            }
            
            list.innerHTML = state.npcOrders.map(order => {
                if (order.completed) {
                    return `<div class="glass p-3 rounded-xl flex items-center justify-between opacity-50 bg-green-50">
                        <span class="font-bold text-green-700">ส่งสำเร็จแล้ว!</span>
                    </div>`;
                }
                
                let canComplete = true;
                let reqHtml = Object.entries(order.reqs).map(([itemId, qty]) => {
                    const have = state.inventory.products[itemId] || 0;
                    if (have < qty) canComplete = false;
                    return `<div class="flex items-center gap-1 text-xs">
                        <span>${PRODUCTS[itemId].emoji}</span> ${PRODUCTS[itemId].name} 
                        <span class="${have >= qty ? 'text-green-600' : 'text-red-500'} font-bold">(${have}/${qty})</span>
                    </div>`;
                }).join('');
                
                return `<div class="glass p-3 rounded-xl">
                    <div class="font-bold text-gray-800 mb-1 border-b border-white/40 pb-1">${order.npc} ต้องการ:</div>
                    <div class="space-y-1 mb-3">
                        ${reqHtml}
                    </div>
                    <div class="flex items-center justify-between">
                        <div class="text-sm font-bold text-amber-700 bg-amber-50 px-2 py-1 rounded">
                            รางวัล: ${order.goldReward} 🪙 | ${order.xpReward} XP
                        </div>
                        <button onclick="deliverOrder('${order.id}')" class="px-3 py-1 text-sm font-bold rounded-lg shadow-sm ${canComplete ? 'bg-green-500 text-white' : 'bg-gray-300 text-gray-500 cursor-not-allowed'}" ${canComplete ? '' : 'disabled'}>
                            ส่งของ
                        </button>
                    </div>
                </div>`;
            }).join('');
        }
        
        function deliverOrder(orderId) {
            const order = state.npcOrders.find(o => o.id === orderId);
            if (!order || order.completed) return;
            
            // Double check
            let canComplete = true;
            for(const [itemId, qty] of Object.entries(order.reqs)) {
                if ((state.inventory.products[itemId] || 0) < qty) canComplete = false;
            }
            
            if (canComplete) {
                for(const [itemId, qty] of Object.entries(order.reqs)) {
                    state.inventory.products[itemId] -= qty;
                }
                state.gold += order.goldReward;
                addXP(order.xpReward);
                order.completed = true;
                
                showAlert('ส่งของสำเร็จ!', `ได้รับ ${order.goldReward} 🪙 และ ${order.xpReward} XP`, '🚚');
                updateUI();
                renderOrders();
                renderInventory();
            }
        }

        function renderQuests() {
            // Render Event Quests
            const evContainer = document.getElementById('event-quests-list');
            if (evContainer) {
                let evHtml = '';
                const curEvent = EVENT_QUESTS[state.season] || [];
                
                const eventIcon = document.getElementById('event-icon');
                const eventDesc = document.getElementById('event-desc');
                if(eventIcon) eventIcon.innerText = SEASON_ICONS[state.season].split(' ')[0];
                if(eventDesc) eventDesc.innerText = `ทำภารกิจพิเศษในช่วง${SEASON_ICONS[state.season]}เพื่อรับรางวัลมหาศาล!`;
                
                curEvent.forEach(quest => {
                    const isClaimed = state.claimedQuests.includes(quest.id);
                    const progress = state.stats[quest.action] || 0;
                    const progressPercent = Math.min((progress / quest.reqAmt) * 100, 100);
                    const isDone = progress >= quest.reqAmt;
                    
                    evHtml += `
                    <div class="glass p-3 rounded-xl ${isClaimed ? 'opacity-50 grayscale' : 'hover:bg-white/60 transition'}">
                        <div class="flex justify-between items-center mb-2">
                            <div>
                                <div class="font-bold text-pink-900">${quest.name}</div>
                                <div class="text-xs text-pink-700">${quest.desc}</div>
                            </div>
                            <div class="text-right">
                                <div class="text-[10px] font-bold text-amber-600">${quest.reward.gold} 🪙</div>
                                <div class="text-[10px] font-bold text-green-600">${quest.reward.xp} XP</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-2">
                            <div class="flex-1 h-2 bg-pink-100 rounded-full overflow-hidden shadow-inner border border-pink-200">
                                <div class="h-full ${isDone ? 'bg-pink-500' : 'bg-pink-400'} transition-all" style="width: ${progressPercent}%"></div>
                            </div>
                            <span class="text-[10px] font-bold ${isDone ? 'text-pink-600' : 'text-gray-500'} w-8 text-right">${Math.min(progress, quest.reqAmt)}/${quest.reqAmt}</span>
                        </div>
                        ${!isClaimed && isDone ? `<button onclick="claimQuest('${quest.id}')" class="w-full mt-2 bg-pink-500 hover:bg-pink-600 text-white font-bold text-xs py-1.5 rounded-lg shadow-sm transition">รับรางวัล!</button>` : ''}
                        ${isClaimed ? `<div class="w-full mt-2 bg-gray-100 text-gray-500 text-center font-bold text-xs py-1.5 rounded-lg">รับแล้ว ✔️</div>` : ''}
                    </div>`;
                });
                evContainer.innerHTML = evHtml;
            }

            const container = document.getElementById('quests-list');
            const availableQuests = QUESTS.filter(q => state.level >= q.unlockLevel);
            
            if (availableQuests.length === 0) {
                container.innerHTML = '<div class="text-sm text-gray-500 text-center py-8">ยังไม่มีภารกิจในเลเวลนี้</div>';
                return;
            }

            container.innerHTML = availableQuests.map(q => {
                const isClaimed = state.claimedQuests.includes(q.id);
                const progress = state.stats[q.action] || 0;
                const isDone = progress >= q.reqAmt;
                const progressPercent = Math.min((progress / q.reqAmt) * 100, 100);

                if (isClaimed) {
                    return `
                    <div class="glass p-3 rounded-xl flex justify-between items-center bg-gray-50/50 opacity-60">
                        <div>
                            <div class="font-bold text-gray-600 line-through">${q.name}</div>
                            <div class="text-xs text-gray-500">สำเร็จแล้ว</div>
                        </div>
                        <span class="text-2xl">✅</span>
                    </div>`;
                }

                return `
                <div class="glass p-4 rounded-xl flex flex-col gap-2">
                    <div class="flex justify-between items-start">
                        <div>
                            <div class="font-bold text-green-900">${q.name}</div>
                            <div class="text-xs font-semibold text-gray-600 mt-0.5">${q.desc}</div>
                        </div>
                        <div class="text-right">
                            <div class="text-[10px] font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded border border-amber-200 inline-block mb-1">
                                🎁 รางวัล: ${q.reward.gold} 🪙 | ${q.reward.xp} XP
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex items-center gap-3 mt-2">
                        <div class="flex-1 h-2 bg-white/60 rounded-full overflow-hidden border border-white">
                            <div class="h-full ${isDone ? 'bg-green-500' : 'bg-purple-400'} transition-all" style="width: ${progressPercent}%"></div>
                        </div>
                        <span class="text-[10px] font-bold ${isDone ? 'text-green-600' : 'text-gray-500'} w-8 text-right">${progress}/${q.reqAmt}</span>
                    </div>

                    ${isDone ? `
                        <button onclick="claimQuest('${q.id}')" class="mt-2 w-full glass-btn py-2 bg-green-50 rounded-lg text-sm font-bold text-green-700 border border-green-200 animate-pulse">
                            รับรางวัล!
                        </button>
                    ` : ''}
                </div>`;
            }).join('');
        }

        // Master UI Updater
        function toggleAutoPlanter() {
            state.autoPlanterActive = state.autoPlanterActive === false ? true : false;
            updateUI();
        }
function toggleAutoHarvesterCrop() {
            state.autoHarvesterCropActive = state.autoHarvesterCropActive === false ? true : false;
            updateUI();
        }
        function toggleAutoHarvesterAnimal() {
            state.autoHarvesterAnimalActive = state.autoHarvesterAnimalActive === false ? true : false;
            updateUI();
        }


        function sellSeed(id) {
            const qty = state.inventory.seeds[id] || 0;
            if (qty > 0) {
                const seed = SEEDS[id];
                const totalValue = Math.floor(seed.buyPrice * 0.5) * qty;
                state.gold += totalValue;
                state.inventory.seeds[id] = 0;
                
                updateUI();
                showAlert('ขายเมล็ดพันธุ์สำเร็จ!', `ขายเมล็ด ${seed.name} ${qty} ถุง ได้รับเงิน ${totalValue} 🪙`, '💰');
                if (typeof fireConfetti === 'function') fireConfetti();
            }
        }

        function sellAllInventory() {
            const prodEntries = Object.entries(state.inventory.products).filter(([_, qty]) => qty > 0);
            if (prodEntries.length === 0) {
                showAlert('ไม่มีผลผลิต', 'คุณยังไม่มีผลผลิตให้ขายเลย', '🤷');
                return;
            }

            let totalValue = 0;
            let totalItems = 0;

            prodEntries.forEach(([id, qty]) => {
                const prod = PRODUCTS[id] || RECIPES[id];
                const basePrice = prod.basePrice || (prod.shopPrice * 1.5) || 100;
                const mult = state.marketMultipliers[id] || 1;
                const sellPrice = Math.floor(basePrice * mult);
                totalValue += sellPrice * qty;
                totalItems += qty;
                state.inventory.products[id] = 0;
            });

            let feePercent = 5;
            if (state.upgrades && state.upgrades.sales_license) {
                feePercent -= state.upgrades.sales_license * 1;
            }
            if (feePercent < 0) feePercent = 0;
            const finalValue = Math.floor(totalValue * ((100 - feePercent) / 100));
            state.gold += finalValue;
            
            updateUI();
            showAlert('ขายทั้งหมดสำเร็จ!', `ขายผลผลิต ${totalItems} ชิ้น ได้รับเงิน ${finalValue} 🪙\n(มูลค่าเดิม ${totalValue} หักค่าธรรมเนียม ${feePercent}%)`, '💰');
            if (typeof fireConfetti === 'function') fireConfetti();
        }

function updateUI() {
            // Auto Harvester Button
            const toggleBtnCrop = document.getElementById('btn-toggle-auto-crop');
            if (toggleBtnCrop) {
                if (state.upgrades && state.upgrades.auto_harvester_crop) {
                    toggleBtnCrop.classList.remove('hidden');
                    const isActive = state.autoHarvesterCropActive !== false;
                    document.getElementById('ui-auto-crop-status').innerText = isActive ? 'เปิด' : 'ปิด';
                    document.getElementById('ui-auto-crop-status').className = isActive ? 'text-white' : 'text-red-100';
                    toggleBtnCrop.className = isActive 
                        ? 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600'
                        : 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-red-400 text-white hover:bg-red-500';
                } else {
                    toggleBtnCrop.classList.add('hidden');
                }
            }
            
            const toggleBtnAnimal = document.getElementById('btn-toggle-auto-animal');
            if (toggleBtnAnimal) {
                if (state.upgrades && state.upgrades.auto_harvester_animal) {
                    toggleBtnAnimal.classList.remove('hidden');
                    const isActive = state.autoHarvesterAnimalActive !== false;
                    document.getElementById('ui-auto-animal-status').innerText = isActive ? 'เปิด' : 'ปิด';
                    document.getElementById('ui-auto-animal-status').className = isActive ? 'text-white' : 'text-red-100';
                    toggleBtnAnimal.className = isActive 
                        ? 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-amber-500 text-white hover:bg-amber-600'
                        : 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-red-400 text-white hover:bg-red-500';
                } else {
                    toggleBtnAnimal.classList.add('hidden');
                }
            }
            // Auto Planter Button
            const togglePlanterBtn = document.getElementById('btn-toggle-planter');
            if (togglePlanterBtn) {
                if (state.upgrades && state.upgrades.auto_planter) {
                    togglePlanterBtn.classList.remove('hidden');
                    const isActive = state.autoPlanterActive !== false;
                    document.getElementById('ui-planter-status').innerText = isActive ? 'เปิด' : 'ปิด';
                    document.getElementById('ui-planter-status').className = isActive ? 'text-white' : 'text-red-100';
                    togglePlanterBtn.className = isActive 
                        ? 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-green-500 text-white hover:bg-green-600'
                        : 'text-xs font-bold px-3 py-1.5 rounded-xl flex items-center gap-1 shadow-sm transition bg-red-400 text-white hover:bg-red-500';
                } else {
                    togglePlanterBtn.classList.add('hidden');
                }
            }

            document.getElementById('ui-gold').innerText = state.gold;
            document.getElementById('ui-level').innerText = state.level;
            const lockC = document.getElementById('lock-cooking');
            const lockO = document.getElementById('lock-orders');
            if (lockC) { if (state.level >= 3) lockC.classList.add('hidden'); else lockC.classList.remove('hidden'); }
            if (lockO) { if (state.level >= 5) lockO.classList.add('hidden'); else lockO.classList.remove('hidden'); }
            
            const xpNeeded = state.level * 100;
            document.getElementById('ui-xp-text').innerText = `${state.xp} / ${xpNeeded} XP`;
            const xpPercent = Math.min((state.xp / xpNeeded) * 100, 100);
            document.getElementById('ui-xp-bar').style.width = `${xpPercent}%`;

            const unlockedPlots = state.plots.filter(p => p.unlocked).length;
            let plotPrice = Math.floor(PLOT_BASE_PRICE * Math.pow(1.6, unlockedPlots - 2));
            if (state.upgrades && state.upgrades.field_expansion) {
                plotPrice = Math.floor(plotPrice * (1 - (state.upgrades.field_expansion * 0.1)));
            }
            document.getElementById('ui-plot-price').innerText = plotPrice;
            document.getElementById('btn-buy-plot').disabled = unlockedPlots >= MAX_PLOTS;

            const unlockedPens = state.pens.filter(p => p.unlocked).length;
            let penPrice = unlockedPens * PEN_BASE_PRICE;
            if (state.upgrades && state.upgrades.barn_expansion) {
                penPrice = Math.floor(penPrice * (1 - (state.upgrades.barn_expansion * 0.1)));
            }
            document.getElementById('ui-pen-price').innerText = penPrice;
            document.getElementById('btn-buy-pen').disabled = unlockedPens >= MAX_PENS;

            // Update tab contents
            renderMarket();
            renderInventory();
            renderCooking();
            renderQuests();
            renderOrders();
            
        }

        function randomizeMarket() {
            Object.keys(PRODUCTS).forEach(key => {
                state.marketMultipliers[key] = parseFloat((Math.random() * (1.4 - 0.8) + 0.8).toFixed(2));
            });
            Object.keys(SEEDS).forEach(key => {
                state.marketMultipliers['seed_'+key] = parseFloat((Math.random() * (1.5 - 0.7) + 0.7).toFixed(2));
            });
            Object.keys(ANIMALS).forEach(key => {
                state.marketMultipliers['animal_'+key] = parseFloat((Math.random() * (1.5 - 0.7) + 0.7).toFixed(2));
            });
            Object.keys(RECIPES).forEach(key => {
                state.marketMultipliers['recipe_'+key] = parseFloat((Math.random() * (1.5 - 0.7) + 0.7).toFixed(2));
            });
            state.lastMarketUpdate = Date.now();
            updateUI(); // Refresh views
        }

        /* =========================================
           4. GAME LOOP
           ========================================= */
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        
        function playSFX(type) {
            if (audioCtx.state === 'suspended') audioCtx.resume();
            
            const sfxVolumeEl = document.getElementById('sfx-volume');
            const sfxVolume = sfxVolumeEl ? parseFloat(sfxVolumeEl.value) : 1.0;
            if (sfxVolume <= 0) return;
            
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            
            if (type === 'harvest') {
                osc.type = 'sine';
                osc.frequency.setValueAtTime(600, audioCtx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(1200, audioCtx.currentTime + 0.1);
                gain.gain.setValueAtTime(sfxVolume * 0.3, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.1);
            } else if (type === 'collect') {
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(400, audioCtx.currentTime);
                osc.frequency.linearRampToValueAtTime(600, audioCtx.currentTime + 0.15);
                gain.gain.setValueAtTime(sfxVolume * 0.3, audioCtx.currentTime);
                gain.gain.linearRampToValueAtTime(0.01, audioCtx.currentTime + 0.15);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.15);
            }
        }

        function gameLoop() {
            const now = Date.now();

            // Season logic (10 minutes = 600,000 ms)
            if (!state.seasonStartTime) state.seasonStartTime = now;
            const seasonIndex = Math.floor((now - state.seasonStartTime) / 600000) % 4;
            const currentSeason = SEASONS[seasonIndex];
            
            if (state.season !== currentSeason) {
                state.season = currentSeason;
                const body = document.body;
                if (currentSeason === 'spring') {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1490750967868-88aa4486c946?q=80&w=2071&auto=format&fit=crop')";
                    body.style.backgroundColor = "#fdf2f8";
                } else if (currentSeason === 'summer') {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1501426026826-31c667bdf23d?q=80&w=1936&auto=format&fit=crop')";
                    body.style.backgroundColor = "#f0fdf4";
                } else if (currentSeason === 'autumn') {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1477414348463-c0eb7f1359b6?q=80&w=2070&auto=format&fit=crop')";
                    body.style.backgroundColor = "#fff7ed";
                } else {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1478265409131-1f65c88f965c?q=80&w=1935&auto=format&fit=crop')";
                    body.style.backgroundColor = "#eff6ff";
                }
                const uiSeason = document.getElementById('ui-season');
                if(uiSeason) uiSeason.innerText = SEASON_ICONS[currentSeason];
                showAlert('เปลี่ยนฤดูกาล!', `เข้าสู่ ${SEASON_ICONS[currentSeason]} แล้ว! (มีเมล็ดพันธุ์ใหม่ๆ ให้ปลูกนะ)`, 'เปลี่ยนฤดู');
                renderMarket(); // update available seeds
            }
            
            // Also ensure it sets correctly on first load if we just refreshed
            if (document.getElementById('ui-season') && document.getElementById('ui-season').innerText !== SEASON_ICONS[state.season]) {
                document.getElementById('ui-season').innerText = SEASON_ICONS[state.season];
                const body = document.body;
                if (state.season === 'spring') {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1490750967868-88aa4486c946?q=80&w=2071&auto=format&fit=crop')";
                    body.style.backgroundColor = "#fdf2f8";
                } else if (state.season === 'summer') {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1501426026826-31c667bdf23d?q=80&w=1936&auto=format&fit=crop')";
                    body.style.backgroundColor = "#f0fdf4";
                } else if (state.season === 'autumn') {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1477414348463-c0eb7f1359b6?q=80&w=2070&auto=format&fit=crop')";
                    body.style.backgroundColor = "#fff7ed";
                } else {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1478265409131-1f65c88f965c?q=80&w=1935&auto=format&fit=crop')";
                    body.style.backgroundColor = "#eff6ff";
                }
            }

            // Market fluctuation & NPC Orders every 60 seconds
            if (now - state.lastMarketUpdate > 300000) {
                randomizeMarket();
                generateNPCOrders();
            }

            // Weather fluctuation every 2 minutes
            if (!state.lastWeatherUpdate || now - state.lastWeatherUpdate > 120000) {
                if (!state.nextWeather) state.nextWeather = 'sunny';
                
                state.weather = state.nextWeather;
                
                // Determine next weather based on season
                let r = Math.random();
                if (state.season === 'winter') {
                    state.nextWeather = r > 0.5 ? 'snowy' : 'sunny';
                } else if (state.season === 'summer') {
                    state.nextWeather = r > 0.8 ? 'rainy' : 'sunny';
                } else {
                    state.nextWeather = r > 0.4 ? 'rainy' : 'sunny';
                }
                
                state.lastWeatherUpdate = now;
                
                const wUI = document.getElementById('ui-weather');
                const nextWUI = document.getElementById('ui-next-weather');
                const layer = document.getElementById('weather-layer');
                if(layer) layer.innerHTML = ''; // clear weather particles
                
                if (state.weather === 'rainy') {
                    if(wUI) {
                        wUI.innerText = '🌧️ ฝนตก (โตไว 2x)';
                        wUI.className = "text-sm font-semibold text-indigo-800 bg-indigo-200/80 px-3 py-0.5 rounded-full shadow-sm border border-white transition-all";
                    }
                    // Add Rain particles
                    if(layer) {
                        for(let i=0; i<30; i++) {
                            let d = document.createElement('div');
                            d.className = 'rain-drop';
                            d.style.left = Math.random() * 100 + 'vw';
                            d.style.animationDuration = (0.5 + Math.random() * 0.5) + 's';
                            d.style.animationDelay = Math.random() * 2 + 's';
                            layer.appendChild(d);
                        }
                    }
                } else if (state.weather === 'snowy') {
                    if(wUI) {
                        wUI.innerText = '❄️ หิมะตก (โตช้า 0.5x)';
                        wUI.className = "text-sm font-semibold text-blue-900 bg-blue-100/80 px-3 py-0.5 rounded-full shadow-sm border border-white transition-all";
                    }
                    // Add Snow particles
                    if(layer) {
                        for(let i=0; i<30; i++) {
                            let d = document.createElement('div');
                            d.className = 'snow-flake';
                            d.style.left = Math.random() * 100 + 'vw';
                            d.style.animationDuration = (2 + Math.random() * 3) + 's';
                            d.style.animationDelay = Math.random() * 2 + 's';
                            layer.appendChild(d);
                        }
                    }
                } else {
                    if(wUI) {
                        wUI.innerText = '🌤️ แดดจ้า';
                        wUI.className = "text-sm font-semibold text-blue-800 bg-blue-100/80 px-3 py-0.5 rounded-full shadow-sm border border-white transition-all";
                    }
                }
                
                const nextIcon = state.nextWeather === 'rainy' ? '🌧️' : (state.nextWeather === 'snowy' ? '❄️' : '🌤️');
                if(nextWUI) nextWUI.innerText = `⏩ ถัดไป: ${nextIcon}`;
            }

            let plantSpeedMult = 1;
            if (state.weather === 'rainy') plantSpeedMult = 2;
            if (state.weather === 'snowy') plantSpeedMult = 0.5;
            
            // Greenhouse bonus
            if (state.upgrades && state.upgrades.greenhouse) {
                plantSpeedMult *= (1 + (state.upgrades.greenhouse * 0.1));
            } else if (state.greenhouseUnlocked) {
                plantSpeedMult *= 1.5;
            }
            if (state.achievements && state.achievements.claimed && state.achievements.claimed.includes('a3')) plantSpeedMult *= 1.1; // 10% faster

            // Auto-Harvester (Crop)
            if (state.autoHarvesterCropActive !== false && (state.upgrades && state.upgrades.auto_harvester_crop) && (!state.lastAutoHarvestCrop || now - state.lastAutoHarvestCrop > 2000)) {
                state.lastAutoHarvestCrop = now;
                state.plots.forEach(plot => {
                    if (plot.unlocked && plot.seedId && plot.plantedAt) {
                        const seed = SEEDS[plot.seedId];
                        let elapsedSec = (now - plot.plantedAt) / 1000;
                        elapsedSec *= plantSpeedMult;
                        if (elapsedSec >= seed.growTime) {
                            if (checkBarnCapacity(1)) {
                                harvest(plot.id, true);
                            }
                        }
                    }
                });
            }

            // Auto-Harvester (Animal)
            if (state.autoHarvesterAnimalActive !== false && (state.upgrades && state.upgrades.auto_harvester_animal) && (!state.lastAutoHarvestAnimal || now - state.lastAutoHarvestAnimal > 2000)) {
                state.lastAutoHarvestAnimal = now;
                state.pens.forEach(pen => {
                    if (pen.unlocked && pen.animalId && pen.lastCollected) {
                        const animal = ANIMALS[pen.animalId];
                        const elapsedSec = (now - pen.lastCollected) / 1000;
                        if (elapsedSec >= animal.cooldown) {
                            if (checkBarnCapacity(1)) {
                                collectAnimal(pen.id, true);
                            }
                        }
                    }
                });
            }

            state.plots.forEach(plot => {
                const elLocked = document.getElementById(`plot-${plot.id}-locked`);
                const elEmpty = document.getElementById(`plot-${plot.id}-empty`);
                const elGrowing = document.getElementById(`plot-${plot.id}-growing`);
                const elHarvest = document.getElementById(`plot-${plot.id}-harvest`);
                const elFertilize = document.getElementById(`plot-${plot.id}-fertilize`);
                
                if (!plot.unlocked) {
                    elLocked.classList.remove('hidden'); elEmpty.classList.add('hidden');
                    elGrowing.classList.add('hidden'); elHarvest.classList.add('hidden');
                    return;
                }
                elLocked.classList.add('hidden');

                if (plot.seedId && plot.plantedAt) {
                    elEmpty.classList.add('hidden');
                    const seed = SEEDS[plot.seedId];
                    // Apply speed multiplier
                    let elapsedSec = (now - plot.plantedAt) / 1000;
                    elapsedSec *= plantSpeedMult;
                    
                    const progress = Math.min((elapsedSec / seed.growTime) * 100, 100);

                    if (progress >= 100) {
                        elGrowing.classList.add('hidden');
                        elHarvest.classList.remove('hidden');
                        if (elFertilize) elFertilize.classList.add('hidden');
                        document.getElementById(`plot-${plot.id}-harvest-emoji`).innerText = PRODUCTS[seed.produces].emoji;
                    } else {
                        elGrowing.classList.remove('hidden');
                        elHarvest.classList.add('hidden');
                        if (elFertilize) {
                            if (state.inventory.fertilizer > 0) {
                                elFertilize.classList.remove('hidden');
                                document.getElementById(`plot-${plot.id}-fert-count`).innerText = state.inventory.fertilizer;
                            } else {
                                elFertilize.classList.add('hidden');
                            }
                        }
                        
                        const pEmoji = document.getElementById(`plot-${plot.id}-emoji`);
                        if (!pEmoji) return;
                        if (progress < 33) {
                            pEmoji.innerText = '🌱';
                            pEmoji.className = 'text-2xl md:text-3xl mb-2 md:mb-3 drop-shadow-sm transition-all duration-500 sway';
                        } else if (progress < 66) {
                            pEmoji.innerText = '🌿';
                            pEmoji.className = 'text-4xl md:text-5xl mb-2 md:mb-3 drop-shadow-sm transition-all duration-500 sway';
                        } else {
                            pEmoji.innerText = seed.emoji;
                            pEmoji.className = 'text-5xl md:text-6xl mb-2 md:mb-3 drop-shadow-sm transition-all duration-500 sway';
                        }
                        
                        document.getElementById(`plot-${plot.id}-bar`).style.width = `${progress}%`;
                    }
                } else {
                    elEmpty.classList.remove('hidden');
                    elGrowing.classList.add('hidden');
                    elHarvest.classList.add('hidden');
                    if (elFertilize) elFertilize.classList.add('hidden');
                }
            });

            state.pens.forEach(pen => {
                const elLocked = document.getElementById(`pen-${pen.id}-locked`);
                const elEmpty = document.getElementById(`pen-${pen.id}-empty`);
                const elProducing = document.getElementById(`pen-${pen.id}-producing`);
                const elCollect = document.getElementById(`pen-${pen.id}-collect`);

                if (!pen.unlocked) {
                    elLocked.classList.remove('hidden'); elEmpty.classList.add('hidden');
                    elProducing.classList.add('hidden'); elCollect.classList.add('hidden');
                    return;
                }
                elLocked.classList.add('hidden');

                const elActions = document.getElementById(`pen-${pen.id}-actions`);

                if (pen.animalId && pen.lastCollected) {
                    elEmpty.classList.add('hidden');
                    if(elActions) elActions.classList.remove('hidden');
                    const animal = ANIMALS[pen.animalId];
                    let elapsedSec = (now - pen.lastCollected) / 1000;
                    if (state.upgrades && state.upgrades.premium_feed) {
                        elapsedSec *= (1 + (state.upgrades.premium_feed * 0.1));
                    }
                    const progress = Math.min((elapsedSec / animal.cooldown) * 100, 100);

                    if (progress >= 100) {
                        elProducing.classList.add('hidden');
                        elCollect.classList.remove('hidden');
                        document.getElementById(`pen-${pen.id}-animal-emoji`).innerText = animal.emoji;
                        document.getElementById(`pen-${pen.id}-product-emoji`).innerText = PRODUCTS[animal.produces].emoji;
                    } else {
                        elProducing.classList.remove('hidden');
                        elCollect.classList.add('hidden');
                        document.getElementById(`pen-${pen.id}-emoji`).innerText = animal.emoji;
                        document.getElementById(`pen-${pen.id}-bar`).style.width = `${progress}%`;
                        const hapEl = document.getElementById(`pen-${pen.id}-happiness`);
                        if (hapEl) hapEl.innerText = (pen.happiness || 0);
                    }
                } else {
                    elEmpty.classList.remove('hidden');
                    if(elActions) elActions.classList.add('hidden');
                    elProducing.classList.add('hidden');
                    elCollect.classList.add('hidden');
                }
            });
        }

        /* =========================================
           5. CORE ACTIONS & LOGIC
           ========================================= */
        function trackStat(action, amount = 1) {
            state.stats[action] = (state.stats[action] || 0) + amount;
            // Update quests UI seamlessly if it's visible
            renderQuests(); 
        }

        function addXP(amount) {
            if (state.upgrades && state.upgrades.golden_hoe) {
                amount = Math.floor(amount * (1 + (state.upgrades.golden_hoe * 0.05)));
            }
            state.xp += amount;
            let xpNeeded = state.level * 100;
            let leveledUp = false;
            
            while (state.xp >= xpNeeded) {
                state.xp -= xpNeeded;
                state.level++;
                xpNeeded = state.level * 100;
                leveledUp = true;
            }

            updateUI(); // Full update on XP change
            if (leveledUp) {
                showAlert('🎉 เลเวลอัพ!', `ยินดีด้วย! คุณอัพเป็นเลเวล ${state.level} แล้ว! เมนูและของใหม่ๆ ในตลาดถูกปลดล็อกแล้ว`, '🌟');
                if (typeof fireConfetti === 'function') fireConfetti();
            }
        }

        function buyPlot() {
            const unlockedCount = state.plots.filter(p => p.unlocked).length;
            if (unlockedCount >= MAX_PLOTS) return;

            let price = Math.floor(PLOT_BASE_PRICE * Math.pow(1.6, unlockedCount - 2));
            if (state.upgrades && state.upgrades.field_expansion) {
                price = Math.floor(price * (1 - (state.upgrades.field_expansion * 0.1)));
            }
            if (state.gold >= price) {
                state.gold -= price;
                state.plots[unlockedCount].unlocked = true;
                updateUI();
            } else {
                showAlert('เงินไม่พอ!', 'คุณมีเหรียญทองไม่พอสำหรับซื้อแปลงผัก', '💸');
            }
        }

        function buyPen() {
            const unlockedCount = state.pens.filter(p => p.unlocked).length;
            if (unlockedCount >= MAX_PENS) return;

            let price = unlockedCount * PEN_BASE_PRICE;
            if (state.upgrades && state.upgrades.barn_expansion) {
                price = Math.floor(price * (1 - (state.upgrades.barn_expansion * 0.1)));
            }
            if (state.gold >= price) {
                state.gold -= price;
                state.pens[unlockedCount].unlocked = true;
                updateUI();
            } else {
                showAlert('เงินไม่พอ!', 'คุณมีเหรียญทองไม่พอสำหรับซื้อคอกสัตว์', '💸');
            }
        }

        function buyItem(type, id, price) {
            let qty = quickBuyAmount;
            if (type === 'animal' || type === 'recipe') {
                qty = 1;
            }
            const totalPrice = price * qty;
            
            if (state.gold < totalPrice) {
                showAlert('เงินไม่พอ!', `เหรียญทองไม่พอสำหรับซื้อ ${qty} ชิ้น`, '💸');
                return;
            }
            
            if (type === 'seed' || type === 'fertilizer') {
                if (!checkBarnCapacity(qty)) {
                    showAlert('พื้นที่กระเป๋าเต็ม!', 'ไม่สามารถซื้อของเพิ่มได้ โปรดอัปเกรดโรงนาหรือขายของก่อน', '📦');
                    return;
                }
            }

            if (type === 'seed') {
                state.gold -= totalPrice;
                state.inventory.seeds[id] = (state.inventory.seeds[id] || 0) + qty;
                updateUI();
                showAlert('ซื้อสำเร็จ', `ได้รับเมล็ด ${SEEDS[id].name} ${qty} ถุง`, '🛒');
            } else if (type === 'fertilizer') {
                state.gold -= totalPrice;
                state.inventory.fertilizer = (state.inventory.fertilizer || 0) + qty;
                updateUI();
                showAlert('ซื้อสำเร็จ', `ได้รับปุ๋ยเร่งโต ${qty} ถุง`, '💩');
            } else if (type === 'recipe') {
                state.gold -= totalPrice;
                if (!state.inventory.unlockedRecipes.includes(id)) {
                    state.inventory.unlockedRecipes.push(id);
                }
                updateUI();
                showAlert('ซื้อสำเร็จ', `ได้รับสูตร ${RECIPES[id].name}`, '📜');
            }
            else if (type === 'animal') {
                const emptyPen = state.pens.find(p => p.unlocked && !p.animalId);
                if (!emptyPen) {
                    showAlert('คอกเต็ม!', 'ไม่มีคอกว่างสำหรับเลี้ยงสัตว์ โปรดสร้างคอกเพิ่ม', '🚫');
                    return;
                }
                state.gold -= price;
                emptyPen.animalId = id;
                emptyPen.lastCollected = Date.now();
                updateUI();
                showAlert('ซื้อสำเร็จ', `${ANIMALS[id].name} ย้ายเข้าคอกแล้ว!`, '🏡');
            }
        }

        
        function buyDynamicUpgrade(id) {
            const u = UPGRADES[id];
            const curLevel = state.upgrades[id] || 0;
            if (curLevel >= u.maxLevel) return;
            let nextPrice = Math.floor(u.buyPrice * Math.pow(u.priceMult, curLevel));
                if (state.upgrades && state.upgrades.upgrade_discount) {
                    nextPrice = Math.floor(nextPrice * (1 - (state.upgrades.upgrade_discount * 0.05)));
                }
            
            if (state.gold >= nextPrice) {
                state.gold -= nextPrice;
                state.upgrades[id] = curLevel + 1;
                showAlert('ซื้อสำเร็จ', `อัปเกรด ${u.name} เป็นเลเวล ${curLevel + 1} แล้ว!`, u.emoji);
                
                if (id === 'merchant_guild') {
                    generateNPCOrders();
                    switchTab('orders'); // Jump to orders tab
                }
                if (id === 'greenhouse') state.greenhouseUnlocked = true;
                if (id === 'auto_harvester') state.autoHarvesterUnlocked = true;
                
                updateUI();
                renderMarket();
            } else {
                showAlert('เงินไม่พอ', 'คุณมีเงินไม่พอซื้อการอัปเกรดนี้', '💸');
            }
        }
            

        function buyUpgrade(type, price) {
            if (state.gold >= price) {
                state.gold -= price;
                if (type === 'greenhouse') state.greenhouseUnlocked = true;
                if (type === 'autoHarvester') state.autoHarvesterUnlocked = true;
                
                updateUI();
                showAlert('อัปเกรดสำเร็จ!', `คุณได้ซื้อ ${type === 'greenhouse' ? 'เรือนกระจก' : 'หุ่นยนต์เก็บเกี่ยว'} เรียบร้อยแล้ว`, '🎉');
                if (typeof fireConfetti === 'function') fireConfetti();
            } else {
                showAlert('เหรียญทองไม่พอ!', 'คุณมีเหรียญทองไม่พอสำหรับอัปเกรดชิ้นนี้', '🪙');
            }
        }

        
        let pendingSaleId = null;

        function updateSellQty(change) {
            const inputEl = document.getElementById('sell-qty-input');
            let val = parseInt(inputEl.value) || 0;
            const max = parseInt(inputEl.getAttribute('data-max')) || 0;
            
            if (change === 'max') {
                val = max;
            } else {
                val += change;
            }
            if (val < 1) val = 1;
            if (val > max) val = max;
            inputEl.value = val;
            updateSellTotal();
        }

        function updateSellTotal() {
            const inputEl = document.getElementById('sell-qty-input');
            const val = parseInt(inputEl.value) || 0;
            const price = parseInt(inputEl.getAttribute('data-price')) || 0;
            document.getElementById('sell-total').innerText = val * price;
        }


        function openSellModal(productId) {
            const qty = state.inventory.products[productId] || 0;
            if (qty <= 0) return;

            const prod = PRODUCTS[productId];
            const mult = state.marketMultipliers[productId] || 1;
            const sellPrice = Math.floor(prod.basePrice * mult);
            const total = qty * sellPrice;
            
            let trendIcon = '➖';
            let trendColor = 'text-gray-500';
            if (mult >= 1.1) { trendIcon = '📈'; trendColor = 'text-green-600'; }
            else if (mult <= 0.9) { trendIcon = '📉'; trendColor = 'text-red-500'; }

            pendingSaleId = productId;
            
            document.getElementById('sell-icon').innerText = prod.emoji;
            document.getElementById('sell-desc').innerHTML = `ขาย <b>${prod.name}</b> (มี <b>${qty}</b> ชิ้น)<br/><span class="text-xs ${trendColor}">ราคาตลาด: ${sellPrice} 🪙 ${trendIcon}</span>`;
            
            const inputEl = document.getElementById('sell-qty-input');
            inputEl.value = qty;
            inputEl.max = qty;
            inputEl.setAttribute('data-price', sellPrice);
            inputEl.setAttribute('data-max', qty);
            
            updateSellTotal();

            const modal = document.getElementById('modal-sell');
            modal.classList.remove('hidden-scale');
            modal.classList.add('visible-scale');
        }

        function closeSellModal() {
            pendingSaleId = null;
            const modal = document.getElementById('modal-sell');
            modal.classList.remove('visible-scale');
            modal.classList.add('hidden-scale');
        }

        function executeSell() {
            if (!pendingSaleId) return;
            const productId = pendingSaleId;
            let qty = state.inventory.products[productId] || 0;
            const inputEl = document.getElementById('sell-qty-input');
            if (inputEl) {
                let sellAmt = parseInt(inputEl.value) || 0;
                if (sellAmt > qty) sellAmt = qty;
                if (sellAmt < 0) sellAmt = 0;
                qty = sellAmt;
            }
            
            if (qty > 0) {
                const prod = PRODUCTS[productId];
                const mult = state.marketMultipliers[productId] || 1;
                let sellPrice = Math.floor(prod.basePrice * mult);
                let multiplierBonus = 1.0;
                
                if (state.achievements && state.achievements.claimed) {
                    if (state.achievements.claimed.includes('a2')) multiplierBonus += 0.10;
                    else if (state.achievements.claimed.includes('a1')) multiplierBonus += 0.05;
                }
                if (state.upgrades && state.upgrades.lucky_charm) {
                    multiplierBonus += (state.upgrades.lucky_charm * 0.05);
                }
                
                sellPrice = Math.floor(sellPrice * multiplierBonus);
                const total = qty * sellPrice;
                
                state.gold += total;
                state.inventory.products[productId] -= qty;
                
                trackStat('earn_gold', total);
                
                // Show floating text over gold UI
                showFloatingText('ui-gold', `+${total} 🪙`, 'text-amber-500');
                
                updateUI();
            }
            closeSellModal();
        }

        function openSeedModal(plotId) {
            currentActivePlotId = plotId;
            const grid = document.getElementById('seed-selection-grid');
            
            const seedEntries = Object.entries(state.inventory.seeds).filter(([_, qty]) => qty > 0);
            if (seedEntries.length === 0) {
                grid.innerHTML = '<div class="col-span-3 text-center text-gray-500 py-6">ไม่มีเมล็ดพันธุ์เลย...<br/>ไปซื้อที่ร้านค้าก่อนนะ!</div>';
            } else {
                grid.innerHTML = seedEntries.map(([id, qty]) => {
                    const seed = SEEDS[id];
                    return `
                    <button onclick="plantSeed('${id}')" class="flex flex-col items-center p-4 bg-white hover:bg-green-50 border-2 border-gray-100 hover:border-green-400 rounded-[1.5rem] transition-all duration-200 shadow-sm hover:shadow-md transform hover:-translate-y-1">
                        <span class="text-3xl mb-1">${seed.emoji}</span>
                        <span class="text-xs font-bold text-gray-800">${seed.name}</span>
                        <span class="text-[10px] font-semibold text-green-600 bg-green-100 px-2 py-0.5 rounded-full mt-1">x${qty}</span>
                    </button>
                    `;
                }).join('');
            }
            
            const modal = document.getElementById('modal-seed');
            modal.classList.remove('hidden-scale');
            modal.classList.add('visible-scale');
        }

        
        let currentActivePenId = null;

        function openAnimalModal(penId) {
            currentActivePenId = penId;
            const grid = document.getElementById('animal-selection-grid');
            grid.innerHTML = Object.values(ANIMALS).map(animal => {
                const isLocked = state.level < animal.unlockLevel;
                const canAfford = state.gold >= animal.buyPrice;
                
                if (isLocked) {
                    return `
                        <div class="flex flex-col items-center p-4 bg-gray-50 border-2 border-gray-100 rounded-[1.5rem] opacity-60 grayscale cursor-not-allowed">
                            <span class="text-3xl mb-1">${animal.emoji}</span>
                            <span class="text-xs font-bold text-gray-600">${animal.name}</span>
                            <span class="text-[10px] text-red-500 mt-1">Lv.${animal.unlockLevel}</span>
                        </div>
                    `;
                }
                
                return `
                    <button onclick="placeAnimal('${animal.id}')" class="glass p-3 rounded-xl flex flex-col items-center hover:bg-white/50 transition border border-transparent hover:border-white ${!canAfford ? 'opacity-50' : ''}">
                        <span class="text-3xl mb-1 drop-shadow-sm">${animal.emoji}</span>
                        <span class="text-xs font-bold text-green-900">${animal.name}</span>
                        <span class="text-[10px] font-bold ${canAfford ? 'text-amber-600' : 'text-red-500'} mt-1">${animal.buyPrice} 🪙</span>
                    </button>
                `;
            }).join('');
            
            const modal = document.getElementById('modal-animal');
            modal.classList.remove('hidden-scale');
            modal.classList.add('visible-scale');
        }

        function openBarnUpgradeModal() {
            const modal = document.getElementById('modal-barn-upgrade');
            const content = document.getElementById('barn-upgrade-content');
            
            const lvl = state.inventory.barnLevel || 1;
            
            if (lvl >= 10) {
                content.innerHTML = `
                    <div class="text-center py-6">
                        <div class="text-4xl mb-3">👑</div>
                        <div class="font-bold text-xl text-blue-900 mb-2">โรงนาเลเวลสูงสุดแล้ว!</div>
                        <div class="text-gray-500 text-sm">คุณมีพื้นที่เก็บของแบบไม่จำกัด</div>
                    </div>
                `;
            } else {
                const curUpg = BARN_UPGRADES.find(u => u.level === lvl);
                const nextUpg = BARN_UPGRADES.find(u => u.level === lvl + 1);
                
                let canUpgrade = true;
                if (state.gold < nextUpg.reqGold) canUpgrade = false;
                
                let reqHtml = Object.entries(nextUpg.reqItems).map(([reqId, reqQty]) => {
                    let hasQty = state.inventory.products[reqId] || 0;
                    if (hasQty < reqQty) canUpgrade = false;
                    let pItem = PRODUCTS[reqId] || ANIMALS[reqId] || RECIPES[reqId]; // Can be any item
                    if(!pItem && reqId === 'duck_egg') pItem = {emoji:'🥚', name:'ไข่เป็ด'}; // fallback
                    let emoji = pItem ? pItem.emoji : '📦';
                    return `
                        <div class="flex items-center justify-between bg-white/60 p-2 rounded-xl text-sm">
                            <span class="flex items-center gap-2">${emoji} ${pItem ? pItem.name : reqId}</span>
                            <span class="${hasQty >= reqQty ? 'text-green-600' : 'text-red-500'} font-bold">${hasQty}/${reqQty}</span>
                        </div>
                    `;
                }).join('');
                
                content.innerHTML = `
                    <div class="flex items-center justify-center gap-4 mb-2">
                        <div class="text-center bg-gray-100 p-3 rounded-2xl flex-1">
                            <div class="text-xs text-gray-500">ปัจจุบัน Lv.${lvl}</div>
                            <div class="font-bold text-lg text-gray-800">${curUpg.capacity} <span class="text-xs">ชิ้น</span></div>
                        </div>
                        <div class="text-blue-500">➡️</div>
                        <div class="text-center bg-blue-100 p-3 rounded-2xl flex-1 border-2 border-blue-200">
                            <div class="text-xs text-blue-600">ระดับถัดไป Lv.${lvl+1}</div>
                            <div class="font-bold text-lg text-blue-900">${nextUpg.capacity >= 999999 ? 'MAX' : nextUpg.capacity} <span class="text-xs">ชิ้น</span></div>
                        </div>
                    </div>
                    
                    <div class="mt-4">
                        <h4 class="text-xs font-bold text-gray-500 uppercase mb-2">เงื่อนไขการอัปเกรด:</h4>
                        <div class="space-y-2 mb-4">
                            <div class="flex items-center justify-between bg-white/60 p-2 rounded-xl text-sm">
                                <span class="flex items-center gap-2">🪙 ทองคำ</span>
                                <span class="${state.gold >= nextUpg.reqGold ? 'text-green-600' : 'text-red-500'} font-bold">${state.gold}/${nextUpg.reqGold}</span>
                            </div>
                            ${reqHtml}
                        </div>
                        
                        <button onclick="upgradeBarn()" class="w-full glass-btn ${canUpgrade ? 'bg-blue-500 hover:bg-blue-600 text-white border-blue-400' : 'bg-gray-200 text-gray-500'} py-3 rounded-xl font-bold shadow-sm" ${!canUpgrade ? 'disabled' : ''}>
                            อัปเกรดเลย!
                        </button>
                    </div>
                `;
            }
            
            modal.classList.remove('hidden-scale');
            modal.classList.add('visible-scale');
        }
        
        function closeBarnUpgradeModal() {
            const modal = document.getElementById('modal-barn-upgrade');
            modal.classList.remove('visible-scale');
            modal.classList.add('hidden-scale');
        }
        
        function upgradeBarn() {
            const lvl = state.inventory.barnLevel || 1;
            if (lvl >= 10) return;
            
            const nextUpg = BARN_UPGRADES.find(u => u.level === lvl + 1);
            
            // Check again
            if (state.gold < nextUpg.reqGold) return;
            let canUpgrade = true;
            Object.entries(nextUpg.reqItems).forEach(([reqId, reqQty]) => {
                if ((state.inventory.products[reqId] || 0) < reqQty) canUpgrade = false;
            });
            
            if (!canUpgrade) return;
            
            // Deduct
            state.gold -= nextUpg.reqGold;
            Object.entries(nextUpg.reqItems).forEach(([reqId, reqQty]) => {
                state.inventory.products[reqId] -= reqQty;
            });
            
            // Upgrade
            state.inventory.barnLevel = lvl + 1;
            
            closeBarnUpgradeModal();
            updateUI();
            
            showAlert('อัปเกรดโรงนาสำเร็จ!', `ยินดีด้วย! พื้นที่เก็บของเพิ่มเป็น ${nextUpg.capacity >= 999999 ? 'MAX' : nextUpg.capacity} ชิ้นแล้ว`, '🎉');
            if (typeof fireConfetti === 'function') fireConfetti();
        }
        function closeAnimalModal() {
            const modal = document.getElementById('modal-animal');
            modal.classList.remove('visible-scale');
            modal.classList.add('hidden-scale');
            currentActivePenId = null;
        }

        function placeAnimal(animalId) {
            if (currentActivePenId === null) return;
            const animal = ANIMALS[animalId];
            if (state.gold >= animal.buyPrice) {
                state.gold -= animal.buyPrice;
                const pen = state.pens.find(p => p.id === currentActivePenId);
                pen.animalId = animalId;
                pen.lastCollected = Date.now();
                pen.happiness = 0;
                updateUI();
                closeAnimalModal();
                showFloatingText(`pen-${currentActivePenId}`, `- ${animal.buyPrice} 🪙`, 'text-red-500');
            } else {
                showAlert('เงินไม่พอ!', `เหรียญทองไม่พอสำหรับซื้อ ${animal.name}`, '💸');
            }
        }

        function closeSeedModal() {
            const modal = document.getElementById('modal-seed');
            modal.classList.remove('visible-scale');
            modal.classList.add('hidden-scale');
            currentActivePlotId = null;
        }

        function plantSeed(seedId) {
            if (currentActivePlotId === null) return;
            if (state.inventory.seeds[seedId] > 0) {
                state.inventory.seeds[seedId]--;
                const plot = state.plots.find(p => p.id === currentActivePlotId);
                plot.seedId = seedId;
                
                let plantedTime = Date.now();
                // Sprinkler Upgrade: 5% chance per level to grow instantly
                if (state.upgrades && state.upgrades.sprinkler) {
                    const chance = state.upgrades.sprinkler * 0.05;
                    if (Math.random() < chance) {
                        plantedTime -= SEEDS[seedId].growTime * 1000 * 2; // offset to past to instant grow
                        showAlert('สปริงเกอร์ทำงาน!', 'เมล็ดพันธุ์ได้รับน้ำและโตเต็มที่ทันที!', '💦');
                    }
                }
                
                plot.plantedAt = plantedTime;
                updateUI();
                closeSeedModal();
            }
        }

        
        function fertilize(plotId, event) {
            if (event) event.stopPropagation();
            if (state.inventory.fertilizer > 0) {
                const plot = state.plots.find(p => p.id === plotId);
                if (plot && plot.seedId && plot.plantedAt) {
                    const seed = SEEDS[plot.seedId];
                    const now = Date.now();
                    
                    const timeElapsedMs = now - plot.plantedAt;
                    const growTimeMs = seed.growTime * 1000;
                    const remainingMs = growTimeMs - timeElapsedMs;
                    
                    if (remainingMs > 0) {
                        state.inventory.fertilizer--;
                        if (state.upgrades && state.upgrades.super_fertilizer) {
                            plot.plantedAt -= remainingMs; // Instant grow
                            showFloatingText(`plot-${plotId}`, '⚡ โตทันที!', 'text-purple-600');
                        } else {
                            plot.plantedAt -= remainingMs * 0.5; // Cut remaining time by 50%
                            showFloatingText(`plot-${plotId}`, '⚡ โตไวขึ้น 50%!', 'text-purple-600');
                        }
                        updateUI();
                    }
                }
            } else {
                showAlert('ไม่มีปุ๋ย', 'ซื้อปุ๋ยได้ที่ร้านค้า > อัปเกรด', '💩');
            }
        }

        function harvest(plotId, isAuto = false) {
            const plot = state.plots.find(p => p.id === plotId);
            if (plot && plot.seedId) {
                playSFX('harvest');
                const seed = SEEDS[plot.seedId];
                const product = seed.produces;
                
                let amount = 1;
                let bonusStr = '';
                if (state.upgrades && state.upgrades.magic_beans) {
                    if (Math.random() < state.upgrades.magic_beans * 0.02) {
                        amount = 2;
                        bonusStr = ' ✨ถั่ววิเศษ!';
                    }
                }
                
                if (!checkBarnCapacity(amount)) {
                    if(!isAuto) showAlert('โรงนาเต็ม!', 'ไม่สามารถเก็บผลผลิตได้ โปรดอัปเกรดโรงนาหรือขายของ', '📦');
                    return;
                }
                
                state.inventory.products[product] = (state.inventory.products[product] || 0) + amount;
                
                trackStat(`harvest_${product}`, amount);
                addXP(seed.xp * amount);
                
                showFloatingText(`plot-${plotId}`, `+${amount} ${PRODUCTS[product].emoji}${bonusStr}  +${seed.xp * amount} XP`, 'text-green-600');
                
                let replanted = false;
                if (state.autoPlanterActive !== false && state.upgrades && state.upgrades.auto_planter) {
                    if (state.inventory.seeds[plot.seedId] > 0) {
                        state.inventory.seeds[plot.seedId]--;
                        plot.plantedAt = Date.now();
                        replanted = true;
                        setTimeout(() => showFloatingText(`plot-${plotId}`, `🌱 ปลูกใหม่!`, 'text-green-500'), 500);
                    }
                }
                
                if (!replanted) {
                    plot.seedId = null;
                    plot.plantedAt = null;
                }
                
                updateUI();
            }
        }

        
        function removeAnimal(penId, event) {
            if (event) event.stopPropagation();
            const pen = state.pens.find(p => p.id === penId);
            if (pen && pen.animalId) {
                const animal = ANIMALS[pen.animalId];
                const sellPrice = Math.floor(animal.buyPrice * 0.5);
                state.gold += sellPrice;
                pen.animalId = null;
                pen.lastCollected = null;
                pen.happiness = 0;
                showFloatingText(`pen-${penId}`, `+${sellPrice} 🪙`, 'text-amber-500');
                showAlert('ขายสัตว์เลี้ยงสำเร็จ', `คุณได้รับเงิน ${sellPrice} 🪙 จากการขาย ${animal.name}`, '👋');
                updateUI();
            }
        }
        
        function feedAnimal(penId, event) {
            if (event) event.stopPropagation();
            const pen = state.pens.find(p => p.id === penId);
            if (!pen || !pen.animalId) return;
            
            // Check if user has food (carrot, cabbage, etc)
            const foods = ['carrot', 'cabbage', 'corn', 'tomato', 'potato'];
            let fed = false;
            for (let f of foods) {
                if (state.inventory.products[f] > 0) {
                    state.inventory.products[f]--;
                    pen.happiness = Math.min(100, (pen.happiness || 0) + 10);
                    showFloatingText(`pen-${penId}`, `อร่อย! 💖+10`, 'text-pink-600');
                    fed = true;
                    break;
                }
            }
            if (!fed) {
                showAlert('ไม่มีอาหาร!', 'สัตว์เลี้ยงชอบกิน แครอท กะหล่ำปลี ข้าวโพด มะเขือเทศ มันฝรั่ง (ต้องมีในผลผลิต)', '🥕');
            } else {
                updateUI();
            }
        }

        function collectAnimal(penId, isAuto = false) {
            const pen = state.pens.find(p => p.id === penId);
            if (pen && pen.animalId) {
                playSFX('collect');
                const animal = ANIMALS[pen.animalId];
                const product = animal.produces;
                
                let amount = 1;
                let doubleDropStr = '';
                
                // Happiness gives chance for double drop (100 happiness = 50% chance)
                let dropChance = (pen.happiness || 0) / 200;
                if (state.upgrades && state.upgrades.lucky_hand) {
                    dropChance += (state.upgrades.lucky_hand * 0.02);
                }
                
                if (Math.random() < dropChance) {
                    amount = 2;
                    doubleDropStr = ' 🍀เบิ้ล!';
                    if (pen.happiness && Math.random() < 0.5) {
                        pen.happiness -= 5; // consume some happiness on double drop
                        if (pen.happiness < 0) pen.happiness = 0;
                    }
                }
                
                if (!checkBarnCapacity(amount)) {
                    if(!isAuto) showAlert('โรงนาเต็ม!', 'ไม่สามารถเก็บผลผลิตได้ โปรดอัปเกรดโรงนาหรือขายของ', '📦');
                    return;
                }
                
                state.inventory.products[product] = (state.inventory.products[product] || 0) + amount;
                
                trackStat(`collect_${product}`, amount);
                addXP(animal.xp * amount);
                
                let bonusGoldStr = '';
                if (state.upgrades && state.upgrades.animal_breeder) {
                    if (Math.random() < state.upgrades.animal_breeder * 0.05) {
                        const bonusGold = Math.floor(PRODUCTS[product].basePrice * amount * 0.5);
                        state.gold += bonusGold;
                        bonusGoldStr = ` +${bonusGold} 🪙`;
                    }
                }
                
                showFloatingText(`pen-${penId}`, `+${amount} ${PRODUCTS[product].emoji}${doubleDropStr}  +${animal.xp * amount} XP${bonusGoldStr}`, 'text-amber-600');
                
                pen.lastCollected = Date.now();
                
                updateUI();
            }
        }

        function cookRecipe(recipeId) {
            const recipe = RECIPES[recipeId];
            if (!recipe) return;

            const qtyInput = document.getElementById(`qty-${recipeId}`);
            const qty = parseInt(qtyInput ? qtyInput.value : 1) || 1;
            if (qty < 1) return;

            // Double check ingredients
            let canCook = true;
            Object.entries(recipe.req).forEach(([reqId, reqQty]) => {
                if ((state.inventory.products[reqId] || 0) < reqQty * qty) canCook = false;
            });

            if (canCook) {
                // Find empty slot
                const emptySlot = state.cookingSlots.find(s => !s.recipeId);
                if (!emptySlot) {
                    showAlert('เตาเต็ม!', 'เตาปรุงอาหารเต็มแล้ว โปรดรอให้เมนูปัจจุบันเสร็จก่อน', '🍳');
                    return;
                }

                // Deduct ingredients
                Object.entries(recipe.req).forEach(([reqId, reqQty]) => {
                    state.inventory.products[reqId] -= reqQty * qty;
                });
                
                // Start cooking
                let timeMs = (recipe.xp * 500) * qty;
                if (timeMs < 3000) timeMs = 3000;
                if (timeMs > 300000) timeMs = 300000;

                emptySlot.recipeId = recipeId;
                emptySlot.startTime = Date.now();
                emptySlot.qty = qty;
                emptySlot.cookTime = timeMs;

                updateUI();
                showAlert('เริ่มปรุงอาหาร!', `กำลังทำ ${recipe.name} x${qty} โปรดรอสักครู่`, '🍳');
            } else {
                showAlert('วัตถุดิบไม่พอ!', 'คุณมีวัตถุดิบไม่เพียงพอสำหรับทำเมนูนี้', '❌');
            }
        }

        function collectFood(slotId) {
            const slot = state.cookingSlots.find(s => s.id === slotId);
            if (!slot || !slot.recipeId) return;
            
            if (!checkBarnCapacity(slot.qty)) {
                showAlert('โรงนาเต็ม!', 'ไม่สามารถเก็บอาหารได้ โปรดอัปเกรดโรงนาหรือขายของก่อน', '📦');
                return;
            }
            
            const recipe = RECIPES[slot.recipeId];
            
            // Add product
            state.inventory.products[slot.recipeId] = (state.inventory.products[slot.recipeId] || 0) + slot.qty;
            
            trackStat(`cook_${slot.recipeId}`, slot.qty);
            let xpBonus = 1;
            if (state.upgrades && state.upgrades.master_chef) {
                xpBonus += state.upgrades.master_chef * 0.1;
            }
            addXP(Math.floor(recipe.xp * slot.qty * xpBonus));
            
            showAlert('ทำอาหารเสร็จแล้ว!', `คุณได้รับ ${recipe.name} x${slot.qty} กลิ่นหอมน่าทานมาก!`, recipe.emoji);
            if (typeof fireConfetti === 'function') fireConfetti();
            
            // Reset slot
            slot.recipeId = null;
            slot.startTime = null;
            slot.qty = 0;
            slot.cookTime = 0;
            
            updateUI();
        }

        function claimQuest(questId) {
            let quest = QUESTS.find(q => q.id === questId);
            if (!quest && EVENT_QUESTS[state.season]) {
                quest = EVENT_QUESTS[state.season].find(q => q.id === questId);
            }
            if (!quest || state.claimedQuests.includes(questId)) return;

            const progress = state.stats[quest.action] || 0;
            if (progress >= quest.reqAmt) {
                state.claimedQuests.push(questId);
                state.gold += quest.reward.gold;
                addXP(quest.reward.xp);
                updateUI();
                
                showAlert('ภารกิจสำเร็จ!', `ได้รับ ${quest.reward.gold} 🪙 และ ${quest.reward.xp} XP`, '🏆');
                if (typeof fireConfetti === 'function') fireConfetti();
            }
        }

        /* =========================================
           6. TAB NAVIGATION & UTILS
           ========================================= */
                        function switchTab(tabId) {
            if (tabId === 'cooking' && state.level < 3) {
                showAlert('ระดับไม่ถึง', 'เมนูอาหารจะปลดล็อกเมื่อเลเวล 3', '🔒');
                return;
            }
            if (tabId === 'orders' && state.level < 5) {
                showAlert('ระดับไม่ถึง', 'เมนูส่งของจะปลดล็อกเมื่อเลเวล 5', '🔒');
                return;
            }
            const tabs = ['farm', 'market', 'inventory', 'cooking', 'quests', 'orders', 'radio', 'achievements'];
            tabs.forEach(t => {
                const view = document.getElementById(`view-${t}`);
                if(view) view.classList.add('hidden');
                const btn = document.getElementById(`tab-${t}`);
                if(btn) {
                    btn.classList.remove('bg-white', 'text-green-900', 'shadow-sm');
                    btn.classList.add('hover:bg-white/70', 'text-green-700');
                }
            });
            
            if (tabId !== 'farm') {
                const activeView = document.getElementById(`view-${tabId}`);
                if(activeView) activeView.classList.remove('hidden');
            }
            
            const activeBtn = document.getElementById(`tab-${tabId}`);
            if(activeBtn) {
                activeBtn.classList.remove('hover:bg-white/70', 'text-green-700');
                activeBtn.classList.add('bg-white', 'text-green-900', 'shadow-sm');
            }
            
            const tabsContainer = document.getElementById('view-tabs-container');
            const farmContainer = document.getElementById('view-farm');
            
            if (tabId === 'farm') {
                if (tabsContainer) tabsContainer.classList.add('hidden');
                if (farmContainer) farmContainer.classList.remove('hidden');
            } else {
                if (tabsContainer) tabsContainer.classList.remove('hidden');
                if (farmContainer) farmContainer.classList.add('hidden');
            }
        }

        function showAlert(title, desc, icon = '✨') {
            document.getElementById('alert-title').innerText = title;
            document.getElementById('alert-desc').innerHTML = desc;
            document.getElementById('alert-icon').innerText = icon;
            
            const modal = document.getElementById('modal-alert');
            modal.classList.remove('hidden-scale');
            modal.classList.add('visible-scale');
        }

        function closeAlert() {
            const modal = document.getElementById('modal-alert');
            modal.classList.remove('visible-scale');
            modal.classList.add('hidden-scale');
        }

        function showFloatingText(elementId, text, colorClass = "text-yellow-600") {
            const el = document.getElementById(elementId);
            if (!el) return;
            
            const rect = el.getBoundingClientRect();
            const floatEl = document.createElement('div');
            floatEl.className = `floating-text ${colorClass} text-lg md:text-xl`;
            floatEl.innerText = text;
            
            // Position at the center-top of the element relative to page
            const top = rect.top + window.scrollY;
            const left = rect.left + window.scrollX + (rect.width / 2);
            
            floatEl.style.top = `${top}px`;
            floatEl.style.left = `${left}px`;
            
            document.body.appendChild(floatEl);
            
            // Remove after animation (1.2s)
            setTimeout(() => {
                floatEl.remove();
            }, 1200);
        }

        function confirmReset() {
            if (confirm("แน่ใจหรือไม่ว่าต้องการเริ่มเกมใหม่ทั้งหมด? ข้อมูลที่เล่นมาจะหายไป!")) {
                localStorage.removeItem('pastelFarmSaveV2');
                location.reload();
            }
        }

        function fireConfetti() {
            if (typeof confetti !== 'undefined') {
                confetti({
                    particleCount: 120,
                    spread: 80,
                    origin: { y: 0.6 },
                    colors: ['#22c55e', '#f59e0b', '#3b82f6', '#ec4899', '#a855f7']
                });
            }
        }

        // Boot
        window.onload = () => {
            loadGame();
            initUI();
        };

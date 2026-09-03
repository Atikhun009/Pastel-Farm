import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the UPGRADES block
old_upgrades_start = "const UPGRADES = {"
old_upgrades_end = "gnome_statue: { id: 'gnome_statue', name: 'รูปปั้นโนม'"

old_block = content[content.find(old_upgrades_start) : content.find(old_upgrades_end)]

new_block = """const UPGRADES = {
            auto_planter: { id: 'auto_planter', name: 'หุ่นยนต์ปลูกผัก', emoji: '🌱', desc: 'ปลูกเมล็ดพันธุ์เดิมอัตโนมัติ (ถ้ามี)', buyPrice: 4000, maxLevel: 1, priceMult: 1, type: 'feature' },
            master_chef: { id: 'master_chef', name: 'มาสเตอร์เชฟ', emoji: '👨‍🍳', desc: 'ทำอาหารได้ XP เพิ่ม 0.5% ต่อเลเวล (สูงสุด 50%)', buyPrice: 1500, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            sales_license: { id: 'sales_license', name: 'ใบอนุญาตการค้า', emoji: '🎫', desc: 'ค่าธรรมเนียมขายทั้งหมดลดลง 0.5% ต่อเลเวล (สูงสุด 50%)', buyPrice: 2000, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            bulk_buyer: { id: 'bulk_buyer', name: 'เหมาจ่าย', emoji: '🤝', desc: 'ซื้อสัตว์เลี้ยงถูกลง 0.5% ต่อเลเวล (สูงสุด 50%)', buyPrice: 1800, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            lucky_hand: { id: 'lucky_hand', name: 'มือทองคำ', emoji: '🧤', desc: 'โอกาส 0.5% ต่อเลเวล ที่สัตว์จะให้ผลผลิต x2 (สูงสุด 50%)', buyPrice: 3000, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            upgrade_discount: { id: 'upgrade_discount', name: 'บัตรส่วนลดอัปเกรด', emoji: '🏷️', desc: 'ซื้ออัปเกรดถูกลง 0.5% ต่อเลเวล (สูงสุด 50%)', buyPrice: 1000, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            greenhouse: { id: 'greenhouse', name: 'เรือนกระจก', emoji: '🌱', desc: 'พืชโตเร็วขึ้น 0.5% ต่อเลเวล (สูงสุด 50%)', buyPrice: 500, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            auto_harvester_crop: { id: 'auto_harvester_crop', name: 'เครื่องเกี่ยวข้าวออโต้', emoji: '🚜', desc: 'เก็บเกี่ยวพืชอัตโนมัติเมื่อโตเต็มที่', buyPrice: 6000, maxLevel: 1, priceMult: 1, type: 'feature' },
            auto_harvester_animal: { id: 'auto_harvester_animal', name: 'เครื่องรีดนมออโต้', emoji: '🐄', desc: 'เก็บผลผลิตสัตว์อัตโนมัติ', buyPrice: 6000, maxLevel: 1, priceMult: 1, type: 'feature' },
            sprinkler: { id: 'sprinkler', name: 'สปริงเกอร์น้ำ', emoji: '💦', desc: 'โอกาส 0.5% ต่อเลเวล ที่พืชจะโตทันทีเมื่อปลูก (สูงสุด 50%)', buyPrice: 800, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            golden_hoe: { id: 'golden_hoe', name: 'จอบทองคำ', emoji: '⛏️', desc: 'ได้รับ XP เพิ่ม 0.5% ต่อเลเวล (สูงสุด 50%)', buyPrice: 1000, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            premium_feed: { id: 'premium_feed', name: 'อาหารสัตว์เกรด A', emoji: '🌾', desc: 'สัตว์ผลิตเร็วขึ้น 0.5% ต่อเลเวล (สูงสุด 50%)', buyPrice: 1500, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            lucky_charm: { id: 'lucky_charm', name: 'เครื่องรางนำโชค', emoji: '🍀', desc: 'เพิ่มราคาขายในตลาด 0.5% ต่อเลเวล (สูงสุด 50%)', buyPrice: 2000, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            weather_radar: { id: 'weather_radar', name: 'เรดาร์สภาพอากาศ', emoji: '📡', desc: 'พยากรณ์อากาศล่วงหน้า', buyPrice: 300, maxLevel: 1, priceMult: 1, type: 'feature' },
            speedy_boots: { id: 'speedy_boots', name: 'รองเท้าวิเศษ', emoji: '👢', desc: 'ได้ของออฟไลน์เยอะขึ้น 0.5% ต่อเลเวล (สูงสุด 50%)', buyPrice: 1200, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            magic_beans: { id: 'magic_beans', name: 'เมล็ดถั่ววิเศษ', emoji: '✨', desc: 'โอกาส 0.5% ต่อเลเวล ที่จะเก็บเกี่ยวพืชได้ x2 (สูงสุด 50%)', buyPrice: 2500, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            animal_breeder: { id: 'animal_breeder', name: 'เคล็ดลับเพาะพันธุ์สัตว์', emoji: '📖', desc: 'เมื่อเก็บเกี่ยวสัตว์ โอกาสได้เงินโบนัส 0.5% ต่อเลเวล (สูงสุด 50%)', buyPrice: 1800, maxLevel: 100, priceMult: 1.15, type: 'passive' },
            --"""

content = content.replace(old_block, new_block.replace('--', ''))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

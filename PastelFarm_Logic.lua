-- ==========================================
-- Pastel Farm - Core Game Logic (Lua Version)
-- ==========================================
-- โค้ดส่วนนี้คือระบบหลักของเกม (Game Logic) ที่ถูกถอดมาจากไฟล์ HTML/JS
-- สามารถนำไปใช้กับ Game Engine ที่รองรับ Lua เช่น Roblox, Love2D, หรือ FiveM ได้
-- โดยต้องเขียนระบบกราฟิก (UI) มาเชื่อมต่อกับตัวแปรเหล่านี้อีกที

local PastelFarm = {
    -- สเตตัสหลักของผู้เล่น
    state = {
        level = 1,
        xp = 0,
        coins = 500,       -- เงินเริ่มต้น
        diamonds = 0,      -- เพชร
        season = "Spring", -- ฤดูกาล
        time = "06:00"     -- เวลาในเกม
    },
    
    -- ช่องเก็บของ (คีย์คือชื่อไอเทม, ค่าคือจำนวน)
    inventory = {
        carrot_seed = 5,
        cabbage_seed = 3
    },
    
    -- แปลงผัก
    plots = {},
    
    -- คอกสัตว์
    animals = {}
}

-- ==========================================
-- ฐานข้อมูลเกม (Config Data)
-- ==========================================
PastelFarm.config = {
    seeds = {
        carrot_seed = { cost = 10, growTime = 5, yield = "carrot" },
        cabbage_seed = { cost = 15, growTime = 10, yield = "cabbage" }
    },
    crops = {
        carrot = { sellPrice = 20 },
        cabbage = { sellPrice = 35 }
    },
    levels = {
        [1] = { xpRequired = 100 },
        [2] = { xpRequired = 250 },
        [3] = { xpRequired = 500 },
        [4] = { xpRequired = 1000 }
    }
}

-- สร้างแปลงปลูกผักเริ่มต้น 6 แปลง
for i = 1, 6 do
    table.insert(PastelFarm.plots, {
        id = i,
        isPlanted = false,
        plantType = nil,
        growthTimeLeft = 0,
        isReady = false
    })
end

-- ==========================================
-- ระบบช่องเก็บของ (Inventory System)
-- ==========================================
function PastelFarm.addItem(itemName, amount)
    amount = amount or 1
    PastelFarm.inventory[itemName] = (PastelFarm.inventory[itemName] or 0) + amount
end

function PastelFarm.removeItem(itemName, amount)
    amount = amount or 1
    if PastelFarm.inventory[itemName] and PastelFarm.inventory[itemName] >= amount then
        PastelFarm.inventory[itemName] = PastelFarm.inventory[itemName] - amount
        return true -- หักไอเทมสำเร็จ
    end
    return false -- ไอเทมไม่พอ
end

-- ==========================================
-- ระบบเลเวล (Leveling System)
-- ==========================================
function PastelFarm.addXP(amount)
    PastelFarm.state.xp = PastelFarm.state.xp + amount
    local currentLevelData = PastelFarm.config.levels[PastelFarm.state.level]
    
    if currentLevelData and PastelFarm.state.xp >= currentLevelData.xpRequired then
        PastelFarm.state.level = PastelFarm.state.level + 1
        PastelFarm.state.xp = PastelFarm.state.xp - currentLevelData.xpRequired
        print("🎉 Level Up! You are now level " .. PastelFarm.state.level)
        -- รับรางวัลเลเวลอัปตรงนี้ได้
    end
end

-- ==========================================
-- ระบบเศรษฐกิจ (Economy System)
-- ==========================================
function PastelFarm.buySeed(seedName, quantity)
    quantity = quantity or 1
    local seedInfo = PastelFarm.config.seeds[seedName]
    if not seedInfo then return false, "ไม่มีเมล็ดพันธุ์นี้" end
    
    local totalCost = seedInfo.cost * quantity
    if PastelFarm.state.coins >= totalCost then
        PastelFarm.state.coins = PastelFarm.state.coins - totalCost
        PastelFarm.addItem(seedName, quantity)
        return true, "ซื้อสำเร็จ"
    else
        return false, "เงินไม่พอ"
    end
end

function PastelFarm.sellCrop(cropName, quantity)
    quantity = quantity or 1
    local cropInfo = PastelFarm.config.crops[cropName]
    if not cropInfo then return false, "ขายผลผลิตนี้ไม่ได้" end

    if PastelFarm.removeItem(cropName, quantity) then
        local totalEarned = cropInfo.sellPrice * quantity
        PastelFarm.state.coins = PastelFarm.state.coins + totalEarned
        return true, "ขายสำเร็จ ได้เงิน: " .. totalEarned
    else
        return false, "ผลผลิตไม่พอขาย"
    end
end

-- ==========================================
-- ระบบทำฟาร์ม (Farming System)
-- ==========================================
function PastelFarm.plantSeed(plotId, seedName)
    local plot = PastelFarm.plots[plotId]
    if not plot then return false, "ไม่มีแปลงนี้" end
    if plot.isPlanted then return false, "แปลงนี้มีพืชอยู่แล้ว" end
    
    local seedInfo = PastelFarm.config.seeds[seedName]
    if not seedInfo then return false, "ไม่มีข้อมูลเมล็ดพันธุ์" end

    if PastelFarm.removeItem(seedName, 1) then
        plot.isPlanted = true
        plot.plantType = seedName
        plot.growthTimeLeft = seedInfo.growTime
        plot.isReady = false
        return true, "ปลูกสำเร็จ"
    else
        return false, "ไม่มีเมล็ดพันธุ์นี้ในช่องเก็บของ"
    end
end

function PastelFarm.harvest(plotId)
    local plot = PastelFarm.plots[plotId]
    if not plot then return false, "ไม่มีแปลงนี้" end
    if not plot.isPlanted then return false, "ไม่มีพืชให้เก็บ" end
    if not plot.isReady then return false, "พืชยังไม่โตเต็มที่" end

    local seedInfo = PastelFarm.config.seeds[plot.plantType]
    PastelFarm.addItem(seedInfo.yield, 1)
    PastelFarm.addXP(15) -- ได้ XP จากการเก็บเกี่ยว
    
    -- รีเซ็ตแปลงปลูก
    plot.isPlanted = false
    plot.plantType = nil
    plot.isReady = false
    plot.growthTimeLeft = 0

    return true, "เก็บเกี่ยวสำเร็จ"
end

-- ==========================================
-- ระบบอัปเดตเวลา (Game Loop)
-- ==========================================
-- ฟังก์ชันนี้ต้องถูกเรียกใช้งานทุกๆ เฟรม หรือทุกๆ วินาทีใน Game Engine
-- dt = delta time (เวลาที่ผ่านไปใน 1 เฟรม)
function PastelFarm.update(dt)
    -- อัปเดตเวลาเติบโตของพืช
    for _, plot in ipairs(PastelFarm.plots) do
        if plot.isPlanted and not plot.isReady then
            plot.growthTimeLeft = plot.growthTimeLeft - dt
            if plot.growthTimeLeft <= 0 then
                plot.isReady = true
                plot.growthTimeLeft = 0
            end
        end
    end
end

return PastelFarm

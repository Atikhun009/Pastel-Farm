import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Guide Tab Button
old_tab_calendar = """                        <button id="tab-rebirth" onclick="switchTab('rebirth')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-purple-700 hover:bg-white/70 transition flex-1 hidden">
                            🔥 จุติ (Rebirth)
                        </button>
                        
                        <div id="ui-calendar" class="px-4 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-white/80 shadow-sm border border-blue-200 text-blue-800 flex-none flex items-center justify-center whitespace-nowrap">"""

new_tab_calendar = """                        <button id="tab-rebirth" onclick="switchTab('rebirth')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-purple-700 hover:bg-white/70 transition flex-1 hidden">
                            🔥 จุติ (Rebirth)
                        </button>
                        <button id="tab-guide" onclick="switchTab('guide')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-orange-700 hover:bg-white/70 transition flex-1">
                            📖 คู่มือ
                        </button>
                        
                        <div id="ui-calendar" class="px-4 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-white/80 shadow-sm border border-blue-200 text-blue-800 flex-none flex items-center justify-center whitespace-nowrap">"""

content = content.replace(old_tab_calendar, new_tab_calendar)

# 2. Add Guide View
guide_view = """
                    <!-- Guide Content -->
                    <div id="view-guide" class="flex-1 overflow-y-auto pr-2 space-y-6 hidden">
                        <div class="glass-panel p-6 rounded-[2rem]">
                            <h2 class="text-2xl font-bold text-orange-900 mb-6 flex items-center gap-2">
                                <span class="text-3xl">📖</span> คู่มือสอนเล่น Pastel Farm
                            </h2>
                            
                            <div class="space-y-6">
                                <!-- Section 1 -->
                                <div class="bg-white/70 p-4 rounded-xl shadow-sm border border-orange-100">
                                    <h3 class="text-lg font-bold text-green-800 mb-2 flex items-center gap-2">🌱 การปลูกพืช</h3>
                                    <ul class="text-sm text-gray-700 space-y-2 list-disc list-inside">
                                        <li>ซื้อ <b>เมล็ดพันธุ์</b> ได้ที่ <span class="text-green-700 font-bold">🛒 ร้านค้า</span></li>
                                        <li>คลิกที่ <span class="text-green-700 font-bold">แปลงว่าง</span> เพื่อเลือกเมล็ดที่จะปลูก</li>
                                        <li>คลิก <span class="text-blue-500 font-bold">รดน้ำ 💧</span> หรือ <span class="text-amber-600 font-bold">ใส่ปุ๋ย 💩</span> เพื่อลดระยะเวลาการเติบโต</li>
                                        <li>เมื่อพืชโตเต็มที่ กดคลิกเพื่อ <b>เก็บเกี่ยว</b> ผลผลิตจะเข้า <span class="text-green-700 font-bold">🎒 กระเป๋า</span> ทันที</li>
                                    </ul>
                                </div>
                                
                                <!-- Section 2 -->
                                <div class="bg-white/70 p-4 rounded-xl shadow-sm border border-orange-100">
                                    <h3 class="text-lg font-bold text-amber-800 mb-2 flex items-center gap-2">🐄 การเลี้ยงสัตว์</h3>
                                    <ul class="text-sm text-gray-700 space-y-2 list-disc list-inside">
                                        <li>ซื้อ <b>สัตว์เลี้ยง</b> ที่ <span class="text-green-700 font-bold">🛒 ร้านค้า</span> หมวดสัตว์</li>
                                        <li>สัตว์จะใช้เวลาในการผลิตไอเทม (เช่น ไข่ นม) เมื่อแถบเวลาเต็ม ให้กด <span class="text-green-600 font-bold">เก็บ 📦</span></li>
                                        <li>ทุกครั้งที่เก็บ มีโอกาสได้รับ <b>ผลผลิต x2</b> ขึ้นอยู่กับความสุขของสัตว์ ยิ่งมีระดับความสุขมาก ยิ่งมีโอกาสเบิ้ลเยอะ!</li>
                                    </ul>
                                </div>
                                
                                <!-- Section 3 -->
                                <div class="bg-white/70 p-4 rounded-xl shadow-sm border border-orange-100">
                                    <h3 class="text-lg font-bold text-blue-800 mb-2 flex items-center gap-2">📦 โรงนา & การขายของ</h3>
                                    <ul class="text-sm text-gray-700 space-y-2 list-disc list-inside">
                                        <li>ของทุกชิ้นที่คุณเก็บเกี่ยวจะใช้ <b>พื้นที่โรงนา</b></li>
                                        <li>หากโรงนาเต็ม คุณจะไม่สามารถเก็บเกี่ยวหรือทำอาหารได้!</li>
                                        <li>คุณสามารถ <span class="text-amber-600 font-bold">ขายผลผลิต</span> ที่แท็บกระเป๋า เพื่อรับเงินและเพิ่มพื้นที่ว่าง</li>
                                        <li>สามารถอัปเกรดความจุโรงนาได้ที่แท็บกระเป๋า (ต้องใช้เงินและของที่กำหนด) แบบ <b>ทยอยส่งของ</b> ได้</li>
                                    </ul>
                                </div>
                                
                                <!-- Section 4 -->
                                <div class="bg-white/70 p-4 rounded-xl shadow-sm border border-orange-100">
                                    <h3 class="text-lg font-bold text-pink-800 mb-2 flex items-center gap-2">🍳 การทำอาหาร & ส่งของ (ภารกิจ)</h3>
                                    <ul class="text-sm text-gray-700 space-y-2 list-disc list-inside">
                                        <li>ผลผลิตสดๆ สามารถนำไป <b>ปรุงอาหาร</b> ได้ที่แท็บอาหาร เพื่อรับ <span class="text-amber-600 font-bold">เงิน</span> และ <span class="text-blue-500 font-bold">XP</span> จำนวนมหาศาล!</li>
                                        <li>มี <b>NPC</b> เข้ามาสั่งซื้อของที่แท็บ <span class="text-green-700 font-bold">📋 ส่งของ</span> หากคุณส่งได้ครบตามที่สั่งจะได้รางวัลพิเศษ</li>
                                        <li>แท็บ <span class="text-green-700 font-bold">📜 ภารกิจ</span> จะมีภารกิจประจำวันให้คุณทำ เพื่อรับทองและเพชร</li>
                                    </ul>
                                </div>
                                
                                <!-- Section 5 -->
                                <div class="bg-white/70 p-4 rounded-xl shadow-sm border border-orange-100">
                                    <h3 class="text-lg font-bold text-purple-800 mb-2 flex items-center gap-2">⚡ ระบบจุติ (Rebirth) & เพชร</h3>
                                    <ul class="text-sm text-gray-700 space-y-2 list-disc list-inside">
                                        <li>เมื่อ <span class="text-purple-600 font-bold">เลเวล 500</span> แท็บจุติจะเปิดขึ้น</li>
                                        <li>หากกดจุติ ทุกอย่างจะถูกรีเซ็ต (ยกเว้นเพชร) แต่คุณจะได้รับโบนัส <span class="text-purple-600 font-bold">เงิน/XP ถาวร +100%</span> และเพชรฟรี</li>
                                        <li>นำ <b>เพชร</b> ไปซื้อบัฟเร่งเวลาได้ที่ <span class="text-blue-600 font-bold">💎 ร้านเพชร</span></li>
                                    </ul>
                                </div>

                            </div>
                        </div>
                    </div>
"""

old_diamond_view = """                    <!-- Diamond Shop Content -->"""
content = content.replace(old_diamond_view, guide_view + "\n" + old_diamond_view)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

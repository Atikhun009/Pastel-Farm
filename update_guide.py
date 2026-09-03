import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_section = """                                <!-- Section 5 -->
                                <div class="bg-white/70 p-4 rounded-xl shadow-sm border border-orange-100">
                                    <h3 class="text-lg font-bold text-purple-800 mb-2 flex items-center gap-2">⚡ ระบบจุติ (Rebirth) & เพชร</h3>
                                    <ul class="text-sm text-gray-700 space-y-2 list-disc list-inside">
                                        <li>เมื่อ <span class="text-purple-600 font-bold">เลเวล 500</span> แท็บจุติจะเปิดขึ้น</li>
                                        <li>หากกดจุติ ทุกอย่างจะถูกรีเซ็ต (ยกเว้นเพชร) แต่คุณจะได้รับโบนัส <span class="text-purple-600 font-bold">เงิน/XP ถาวร +100%</span> และเพชรฟรี</li>
                                        <li>นำ <b>เพชร</b> ไปซื้อบัฟเร่งเวลาได้ที่ <span class="text-blue-600 font-bold">💎 ร้านเพชร</span></li>
                                    </ul>
                                </div>

                            </div>"""

new_section = """                                <!-- Section 5 -->
                                <div class="bg-white/70 p-4 rounded-xl shadow-sm border border-orange-100">
                                    <h3 class="text-lg font-bold text-purple-800 mb-2 flex items-center gap-2">⚡ ระบบจุติ (Rebirth) & เพชร</h3>
                                    <ul class="text-sm text-gray-700 space-y-2 list-disc list-inside">
                                        <li>เมื่อ <span class="text-purple-600 font-bold">เลเวล 500</span> แท็บจุติจะเปิดขึ้น</li>
                                        <li>หากกดจุติ ทุกอย่างจะถูกรีเซ็ต (ยกเว้นเพชร) แต่คุณจะได้รับโบนัส <span class="text-purple-600 font-bold">เงิน/XP ถาวร +100%</span> และเพชรฟรี</li>
                                        <li>นำ <b>เพชร</b> ไปซื้อบัฟเร่งเวลาได้ที่ <span class="text-blue-600 font-bold">💎 ร้านเพชร</span></li>
                                    </ul>
                                </div>
                                
                                <!-- Update Log -->
                                <div class="bg-blue-50 p-4 rounded-xl shadow-sm border border-blue-200">
                                    <h3 class="text-lg font-bold text-blue-900 mb-3 flex items-center gap-2">📢 บันทึกการอัปเดต (Patch Notes)</h3>
                                    
                                    <div class="space-y-4">
                                        <div class="bg-white p-3 rounded-lg border border-blue-100">
                                            <div class="flex items-center gap-2 mb-1">
                                                <span class="bg-blue-500 text-white text-xs font-bold px-2 py-0.5 rounded">v1.2.0</span>
                                                <span class="text-sm font-bold text-gray-800">ระบบของขวัญและคู่มือ</span>
                                            </div>
                                            <ul class="text-xs text-gray-600 space-y-1 list-disc list-inside">
                                                <li>เพิ่มแท็บ <span class="text-orange-600 font-bold">คู่มือ</span> สำหรับอธิบายระบบต่างๆ</li>
                                                <li>เพิ่มระบบ <span class="text-purple-600 font-bold">โค้ดของขวัญ</span> ให้ผู้เล่นสามารถสร้างโค้ดส่งไอเทม เงิน หรือเพชรให้เพื่อนได้ (โค้ดอายุ 2 นาที)</li>
                                                <li>แยกช่องกรอกโค้ดผู้พัฒนา และ โค้ดรับของขวัญจากเพื่อน ออกจากกันอย่างชัดเจน</li>
                                                <li>แก้ไขบั๊กการแสดงเวลานับถอยหลังของบัฟเร่งความเร็ว</li>
                                            </ul>
                                        </div>
                                        
                                        <div class="bg-white p-3 rounded-lg border border-gray-200 opacity-80">
                                            <div class="flex items-center gap-2 mb-1">
                                                <span class="bg-gray-500 text-white text-xs font-bold px-2 py-0.5 rounded">v1.1.0</span>
                                                <span class="text-sm font-bold text-gray-800">ขยายระบบทำฟาร์ม</span>
                                            </div>
                                            <ul class="text-xs text-gray-600 space-y-1 list-disc list-inside">
                                                <li>เพิ่มระบบร้านค้าแยกหมวดหมู่ (พืช, สัตว์, อัปเกรด, ตำราอาหาร)</li>
                                                <li>เพิ่มแท็บภารกิจ, ทำอาหาร และออเดอร์ส่งของจาก NPC</li>
                                                <li>เพิ่มบัฟพิเศษ (พืชโตไว, เงินคูณสอง)</li>
                                            </ul>
                                        </div>
                                        
                                        <div class="bg-white p-3 rounded-lg border border-gray-200 opacity-80">
                                            <div class="flex items-center gap-2 mb-1">
                                                <span class="bg-gray-500 text-white text-xs font-bold px-2 py-0.5 rounded">v1.0.0</span>
                                                <span class="text-sm font-bold text-gray-800">เปิดตัวเกม</span>
                                            </div>
                                            <ul class="text-xs text-gray-600 space-y-1 list-disc list-inside">
                                                <li>ระบบปลูกพืช เลี้ยงสัตว์เบื้องต้น</li>
                                                <li>ระบบความสุขสัตว์เลี้ยงและฤดูกาล</li>
                                                <li>UI กระจกสไตล์พาสเทล</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>

                            </div>"""

if old_section in content:
    content = content.replace(old_section, new_section)
    print("Patch notes added successfully")
else:
    print("Could not find section to replace")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


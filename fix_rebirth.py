import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add rebirth tab
old_tab_diamond = """                        <button id="tab-diamond" onclick="switchTab('diamond')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-blue-700 hover:bg-white/70 transition flex-1">
                            💎 ร้านเพชร
                        </button>"""

new_tab_diamond = """                        <button id="tab-diamond" onclick="switchTab('diamond')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-blue-700 hover:bg-white/70 transition flex-1">
                            💎 ร้านเพชร
                        </button>
                        <button id="tab-rebirth" onclick="switchTab('rebirth')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-purple-700 hover:bg-white/70 transition flex-1 hidden">
                            🔥 จุติ (Rebirth)
                        </button>"""

content = content.replace(old_tab_diamond, new_tab_diamond)

# 2. Add Rebirth View HTML
old_diamond_view = """                    <!-- Diamond Shop Content -->"""

rebirth_view = """                    <!-- Rebirth Content -->
                    <div id="view-rebirth" class="flex-1 overflow-y-auto pr-2 space-y-4 hidden text-center">
                        <div class="bg-gradient-to-br from-purple-900 to-indigo-900 rounded-[2rem] p-8 text-white shadow-xl relative overflow-hidden">
                            <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/stardust.png')] opacity-30 mix-blend-overlay"></div>
                            <div class="relative z-10">
                                <h2 class="text-4xl font-black mb-2 text-transparent bg-clip-text bg-gradient-to-r from-purple-300 to-pink-300 drop-shadow-sm">🔥 จุติ (Rebirth)</h2>
                                <p class="text-purple-200 mb-6 font-medium">เริ่มต้นใหม่เพื่อก้าวข้ามขีดจำกัด!</p>
                                
                                <div class="bg-black/30 p-6 rounded-2xl inline-block mb-6 backdrop-blur-sm border border-purple-500/30">
                                    <div class="text-xs text-purple-300 font-bold mb-1 uppercase tracking-wider">รอบจุติปัจจุบันของคุณ</div>
                                    <div class="text-5xl font-black text-white" id="ui-rebirth-count">0</div>
                                </div>
                                
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8 text-left">
                                    <div class="bg-white/10 p-4 rounded-xl border border-white/10">
                                        <h3 class="font-bold text-lg text-pink-300 mb-2">⚠️ สิ่งที่จะถูกรีเซ็ต</h3>
                                        <ul class="text-sm text-purple-100 space-y-1 list-disc list-inside">
                                            <li>เลเวล และ XP</li>
                                            <li>เหรียญทองทั้งหมด</li>
                                            <li>ไอเทมในกระเป๋า และโรงนา</li>
                                            <li>สัตว์เลี้ยง และพืชผัก</li>
                                            <li>การอัปเกรดทั้งหมด</li>
                                        </ul>
                                    </div>
                                    <div class="bg-white/10 p-4 rounded-xl border border-white/10">
                                        <h3 class="font-bold text-lg text-green-300 mb-2">🎁 สิ่งที่จะได้รับ</h3>
                                        <ul class="text-sm text-purple-100 space-y-1 list-disc list-inside">
                                            <li><span class="font-bold text-white">+100%</span> โบนัสเงินและ XP ถาวร!</li>
                                            <li>ได้รับ <span class="font-bold text-white">500 💎 เพชร</span> ทันที</li>
                                            <li>เพชรเดิมที่มีอยู่<span class="font-bold text-green-300">จะไม่หายไป</span></li>
                                        </ul>
                                    </div>
                                </div>
                                
                                <div id="rebirth-req-msg" class="text-red-300 font-bold mb-4 hidden">คุณต้องมีเลเวล 500 ขึ้นไปจึงจะจุติได้</div>
                                
                                <button id="btn-perform-rebirth" onclick="performRebirth()" class="px-8 py-4 bg-gradient-to-r from-pink-500 to-purple-500 hover:from-pink-400 hover:to-purple-400 text-white font-black text-xl rounded-2xl shadow-lg transition-transform hover:scale-105 active:scale-95 flex items-center justify-center gap-3 mx-auto w-full max-w-sm border-2 border-pink-300">
                                    <span class="text-2xl">⚡</span> กดเพื่อจุติเลย!
                                </button>
                            </div>
                        </div>
                    </div>
"""
content = content.replace(old_diamond_view, rebirth_view + "\n" + old_diamond_view)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

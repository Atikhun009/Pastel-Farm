import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

view_diamond_html = """
                    <!-- Diamond Shop Content -->
                    <div id="view-diamond" class="flex-1 overflow-y-auto pr-2 space-y-4 hidden">
                        <div class="bg-blue-50/80 rounded-xl p-3 mb-4 text-xs font-semibold text-blue-800 border border-blue-200 flex gap-2">
                            <span class="text-base">💎</span> ร้านค้าพิเศษ! ใช้เพชรเพื่อซื้อบัฟเสริมต่างๆ เพชรหาได้จากการอัพเลเวล และการส่งของตามออเดอร์
                        </div>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                            <div class="bg-white/80 p-4 rounded-2xl shadow-sm border-2 border-blue-100 flex flex-col justify-between hover:scale-[1.02] transition-transform">
                                <div>
                                    <h3 class="font-bold text-lg text-blue-900 mb-1">💰 คูณสองเงินรายได้</h3>
                                    <p class="text-xs text-gray-600">ได้รับเงิน x2 จากการขายทุกช่องทาง เป็นเวลา 2 นาที</p>
                                </div>
                                <button onclick="buyDiamondBuff('gold_x2', 20)" class="mt-4 px-4 py-2 bg-gradient-to-r from-blue-400 to-blue-500 text-white font-bold rounded-xl shadow-md hover:from-blue-500 hover:to-blue-600 transition-all flex items-center justify-center gap-2">
                                    ซื้อ 20 <span class="text-lg">💎</span>
                                </button>
                            </div>

                            <div class="bg-white/80 p-4 rounded-2xl shadow-sm border-2 border-blue-100 flex flex-col justify-between hover:scale-[1.02] transition-transform">
                                <div>
                                    <h3 class="font-bold text-lg text-blue-900 mb-1">🌱 พืชโตไว x2</h3>
                                    <p class="text-xs text-gray-600">พืชโตเร็วขึ้น 2 เท่า เป็นเวลา 2 นาที (ทับซ้อนบัฟอื่นได้)</p>
                                </div>
                                <button onclick="buyDiamondBuff('crop_speed_x2', 15)" class="mt-4 px-4 py-2 bg-gradient-to-r from-blue-400 to-blue-500 text-white font-bold rounded-xl shadow-md hover:from-blue-500 hover:to-blue-600 transition-all flex items-center justify-center gap-2">
                                    ซื้อ 15 <span class="text-lg">💎</span>
                                </button>
                            </div>

                            <div class="bg-white/80 p-4 rounded-2xl shadow-sm border-2 border-blue-100 flex flex-col justify-between hover:scale-[1.02] transition-transform">
                                <div>
                                    <h3 class="font-bold text-lg text-blue-900 mb-1">🐾 สัตว์ผลิตไว x2</h3>
                                    <p class="text-xs text-gray-600">สัตว์ผลิตผลผลิตเร็วขึ้น 2 เท่า เป็นเวลา 2 นาที</p>
                                </div>
                                <button onclick="buyDiamondBuff('animal_speed_x2', 15)" class="mt-4 px-4 py-2 bg-gradient-to-r from-blue-400 to-blue-500 text-white font-bold rounded-xl shadow-md hover:from-blue-500 hover:to-blue-600 transition-all flex items-center justify-center gap-2">
                                    ซื้อ 15 <span class="text-lg">💎</span>
                                </button>
                            </div>

                            <div class="bg-white/80 p-4 rounded-2xl shadow-sm border-2 border-blue-100 flex flex-col justify-between hover:scale-[1.02] transition-transform">
                                <div>
                                    <h3 class="font-bold text-lg text-blue-900 mb-1">🍀 โอกาสเบิ้ล 100%</h3>
                                    <p class="text-xs text-gray-600">สุ่มได้ผลผลิต 2 ชิ้นแบบ 100% (ทั้งพืชและสัตว์) เป็นเวลา 2 นาที</p>
                                </div>
                                <button onclick="buyDiamondBuff('double_drop', 30)" class="mt-4 px-4 py-2 bg-gradient-to-r from-blue-400 to-blue-500 text-white font-bold rounded-xl shadow-md hover:from-blue-500 hover:to-blue-600 transition-all flex items-center justify-center gap-2">
                                    ซื้อ 30 <span class="text-lg">💎</span>
                                </button>
                            </div>
                            
                            <div class="bg-white/80 p-4 rounded-2xl shadow-sm border-2 border-blue-100 flex flex-col justify-between hover:scale-[1.02] transition-transform">
                                <div>
                                    <h3 class="font-bold text-lg text-blue-900 mb-1">🪙 แลกเงิน</h3>
                                    <p class="text-xs text-gray-600">ใช้เพชรแลกเงินจำนวนตามเลเวลของคุณ (รับ ${state.level * 1000} 🪙)</p>
                                </div>
                                <button onclick="buyDiamondBuff('gold_instant', 5)" class="mt-4 px-4 py-2 bg-gradient-to-r from-amber-400 to-amber-500 text-white font-bold rounded-xl shadow-md hover:from-amber-500 hover:to-amber-600 transition-all flex items-center justify-center gap-2">
                                    ซื้อ 5 <span class="text-lg">💎</span>
                                </button>
                            </div>
                        </div>
                    </div>
"""

content = content.replace("<!-- Market Content -->", view_diamond_html + "\n                    <!-- Market Content -->")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

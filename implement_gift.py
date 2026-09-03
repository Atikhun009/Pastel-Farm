import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_html = """                    <div id="view-redeem" class="flex-1 overflow-y-auto pr-2 space-y-6 hidden">
                        <div class="bg-blue-50/80 rounded-xl p-3 mb-4 text-xs font-semibold text-blue-800 border border-blue-200">
                            🎟️ กรอกโค้ดลับเพื่อรับของรางวัลพิเศษ!
                        </div>
                        <div class="glass p-4 rounded-2xl">
                            <input type="text" id="redeem-code-input" placeholder="ใส่โค้ดที่นี่ (เช่น PASTELFARM2025)" class="w-full mb-3 px-4 py-2 rounded-xl bg-white/50 border border-white/50 focus:outline-none focus:ring-2 focus:ring-green-400 font-bold text-center text-gray-700 uppercase">
                            <button onclick="redeemCode()" class="w-full bg-green-500 hover:bg-green-600 text-white font-bold py-3 rounded-xl shadow-md transition transform hover:scale-105">
                                รับรางวัล
                            </button>
                        </div>
                    </div>"""

new_html = """                    <!-- Redeem & Gift Content -->
                    <div id="view-redeem" class="flex-1 overflow-y-auto pr-2 space-y-6 hidden">
                        <!-- Redeem Code -->
                        <div class="glass-panel p-5 rounded-[2rem]">
                            <h2 class="text-xl font-bold text-green-900 flex items-center gap-2 mb-4">
                                <span class="text-2xl">🎟️</span> กรอกโค้ดรับของ
                            </h2>
                            <p class="text-xs text-gray-500 mb-4">รับของรางวัลพิเศษจากผู้พัฒนา หรือโค้ดของขวัญจากเพื่อน!</p>
                            <input type="text" id="redeem-code-input" placeholder="ใส่โค้ดที่นี่" class="w-full mb-3 px-4 py-3 rounded-xl bg-white/70 border border-white/50 focus:outline-none focus:ring-2 focus:ring-green-400 font-bold text-center text-gray-700">
                            <button onclick="redeemCode()" class="w-full bg-green-500 hover:bg-green-600 text-white font-bold py-3 rounded-xl shadow-md transition transform hover:scale-105">
                                รับรางวัล
                            </button>
                        </div>
                        
                        <!-- Create Gift Code -->
                        <div class="glass-panel p-5 rounded-[2rem] border-2 border-purple-200 bg-purple-50/30">
                            <h2 class="text-xl font-bold text-purple-900 flex items-center gap-2 mb-4">
                                <span class="text-2xl">🎁</span> สร้างโค้ดส่งของให้เพื่อน
                            </h2>
                            <p class="text-xs text-purple-700 mb-4 font-semibold">เลือกของที่คุณมี เพื่อสร้างโค้ดให้เพื่อนไปกรอกรับ (โค้ดหมดอายุใน 2 นาที)</p>
                            
                            <div class="space-y-3 mb-4">
                                <div>
                                    <label class="text-xs font-bold text-gray-500 mb-1 block">เลือกไอเทมที่จะส่ง:</label>
                                    <select id="gift-item-select" class="w-full px-4 py-2 rounded-xl bg-white/70 border border-white/50 focus:outline-none focus:ring-2 focus:ring-purple-400 font-bold text-gray-700">
                                        <!-- Populated via JS -->
                                    </select>
                                </div>
                                <div>
                                    <label class="text-xs font-bold text-gray-500 mb-1 block">จำนวน (ที่ส่งได้):</label>
                                    <input type="number" id="gift-qty-input" min="1" value="1" class="w-full px-4 py-2 rounded-xl bg-white/70 border border-white/50 focus:outline-none focus:ring-2 focus:ring-purple-400 font-bold text-gray-700">
                                </div>
                            </div>
                            
                            <button onclick="generateGiftCode()" class="w-full bg-purple-500 hover:bg-purple-600 text-white font-bold py-3 rounded-xl shadow-md transition transform hover:scale-105 mb-4">
                                สร้างโค้ดของขวัญ
                            </button>
                            
                            <!-- Result Box -->
                            <div id="gift-result-box" class="hidden bg-white p-4 rounded-xl border border-purple-200 text-center">
                                <div class="text-xs font-bold text-gray-500 mb-2">ก๊อปปี้โค้ดด้านล่างให้เพื่อน (อายุ 2 นาที)</div>
                                <div class="flex gap-2">
                                    <input type="text" id="gift-code-output" readonly class="flex-1 bg-gray-100 rounded-lg px-2 py-1 text-sm font-mono text-gray-600">
                                    <button onclick="copyGiftCode()" class="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded-lg text-xs font-bold transition">ก๊อปปี้</button>
                                </div>
                            </div>
                        </div>
                    </div>"""

if old_html in content:
    content = content.replace(old_html, new_html)
    print("Replaced Redeem HTML")
else:
    print("Could not find old_html to replace")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


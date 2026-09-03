import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Navigation Button
nav_old = """                        <button id="tab-achievements" onclick="switchTab('achievements')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🏆 ความสำเร็จ
                        </button>"""
nav_new = """                        <button id="tab-achievements" onclick="switchTab('achievements')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🏆 ความสำเร็จ
                        </button>
                        <button id="tab-redeem" onclick="switchTab('redeem')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🎟️ โค้ด
                        </button>"""
content = content.replace(nav_old, nav_new)

# 2. Add Redeem View
view_orders_regex = r'(<div id="view-orders" class="flex-1 overflow-y-auto pr-2 space-y-6 hidden">.*?</div>\n                        </div>\n                    </div>)'
view_redeem = """
                    <div id="view-redeem" class="flex-1 overflow-y-auto pr-2 space-y-6 hidden">
                        <div class="bg-blue-50/80 rounded-xl p-3 mb-4 text-xs font-semibold text-blue-800 border border-blue-200">
                            🎟️ กรอกโค้ดลับเพื่อรับของรางวัลพิเศษ!
                        </div>
                        <div class="glass p-4 rounded-2xl">
                            <input type="text" id="redeem-code-input" placeholder="ใส่โค้ดที่นี่..." class="w-full mb-3 px-4 py-2 rounded-xl bg-white/50 border border-white/50 focus:outline-none focus:ring-2 focus:ring-green-400 font-bold text-center text-gray-700 uppercase">
                            <button onclick="redeemCode()" class="w-full bg-green-500 hover:bg-green-600 text-white font-bold py-3 rounded-xl shadow-md transition transform hover:scale-105">
                                รับรางวัล
                            </button>
                        </div>
                    </div>
"""
# I need a more reliable replacement for the view insertion.

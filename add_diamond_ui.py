import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add diamond counter
header_old = """                <div class="flex items-center gap-3 bg-gradient-to-r from-yellow-100 to-amber-100 px-6 py-3 rounded-2xl border border-yellow-200 shadow-sm">
                    <span class="text-2xl drop-shadow-sm">🪙</span>
                    <span id="ui-gold" class="text-2xl font-bold text-amber-700">300</span>
                    <span id="ui-gold-buff" class="text-xs font-bold text-red-600 bg-red-100 px-1 rounded hidden animate-pulse">x1.5</span>
                </div>
            </div>
        </header>"""

header_new = """                <div class="flex flex-col gap-2">
                    <div class="flex items-center gap-3 bg-gradient-to-r from-yellow-100 to-amber-100 px-6 py-2 rounded-2xl border border-yellow-200 shadow-sm w-full">
                        <span class="text-2xl drop-shadow-sm">🪙</span>
                        <span id="ui-gold" class="text-xl font-bold text-amber-700">300</span>
                        <span id="ui-gold-buff" class="text-xs font-bold text-red-600 bg-red-100 px-1 rounded hidden animate-pulse">x2</span>
                    </div>
                    <div class="flex items-center gap-3 bg-gradient-to-r from-blue-50 to-cyan-100 px-6 py-2 rounded-2xl border border-blue-200 shadow-sm w-full">
                        <span class="text-2xl drop-shadow-sm">💎</span>
                        <span id="ui-diamond" class="text-xl font-bold text-blue-700">0</span>
                    </div>
                </div>
            </div>
        </header>"""

content = content.replace(header_old, header_new)

# Add tab for diamond shop
tab_old = """                        <button id="tab-redeem" onclick="switchTab('redeem')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🎟️ โค้ด
                        </button>"""

tab_new = """                        <button id="tab-redeem" onclick="switchTab('redeem')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🎟️ โค้ด
                        </button>
                        <button id="tab-diamond" onclick="switchTab('diamond')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-blue-700 hover:bg-white/70 transition flex-1">
                            💎 ร้านเพชร
                        </button>"""

content = content.replace(tab_old, tab_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_inv_ui = """                        <div>
                            <div class="flex justify-between items-center mb-3">
                                <h3 class="text-sm font-bold text-green-900/60 uppercase tracking-wider flex items-center gap-1">
                                    <span>🧺</span> ผลผลิต
                                </h3>
                                <button onclick="sellAllInventory()" class="text-xs bg-red-50 text-red-600 hover:bg-red-100 font-bold px-3 py-1.5 rounded-lg transition shadow-sm border border-red-200">
                                    ⚡ ขายทั้งหมด (-5%)
                                </button>
                            </div>"""

new_inv_ui = """                        <div>
                            <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-3 gap-2">
                                <h3 class="text-sm font-bold text-green-900/60 uppercase tracking-wider flex items-center gap-1">
                                    <span>🧺</span> ผลผลิต
                                </h3>
                                
                                <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-2 w-full md:w-auto">
                                    <div class="flex items-center gap-2 bg-white/50 px-3 py-1.5 rounded-xl border border-white shadow-sm flex-1 sm:flex-none justify-between">
                                        <div class="text-xs font-bold text-gray-600">โรงนา <span id="ui-barn-level" class="text-green-700 bg-green-100 px-1.5 rounded">Lv.1</span></div>
                                        <div class="flex items-center gap-2">
                                            <div class="w-20 md:w-24 h-2 bg-gray-200 rounded-full overflow-hidden">
                                                <div id="ui-barn-fill" class="h-full bg-green-500 transition-all duration-300" style="width: 0%"></div>
                                            </div>
                                            <div class="text-[10px] font-bold text-gray-700 w-12 text-right"><span id="ui-barn-cur">0</span>/<span id="ui-barn-max">100</span></div>
                                        </div>
                                    </div>
                                    <button onclick="openBarnUpgradeModal()" class="text-xs bg-blue-500 text-white hover:bg-blue-600 font-bold px-3 py-1.5 rounded-xl transition shadow-sm flex-none text-center">
                                        ⬆️ อัปเกรด
                                    </button>
                                    <button onclick="sellAllInventory()" class="text-xs bg-red-50 text-red-600 hover:bg-red-100 font-bold px-3 py-1.5 rounded-xl transition shadow-sm border border-red-200 flex-none text-center">
                                        ⚡ ขายหมด (-5%)
                                    </button>
                                </div>
                            </div>"""

content = content.replace(old_inv_ui, new_inv_ui)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

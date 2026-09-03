import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

header_gold_old = """<span id="ui-gold" class="text-2xl font-bold text-amber-700">300</span>"""
header_gold_new = """<span id="ui-gold" class="text-2xl font-bold text-amber-700">300</span>
                    <span id="ui-gold-buff" class="text-xs font-bold text-red-600 bg-red-100 px-1 rounded hidden animate-pulse">x1.5</span>"""
content = content.replace(header_gold_old, header_gold_new)

header_xp_old = """<span id="ui-level" class="font-black text-amber-700">1</span>"""
header_xp_new = """<span id="ui-level" class="font-black text-amber-700">1</span>
                                <span id="ui-crop-buff" class="text-xs font-bold text-green-600 bg-green-100 px-1 rounded hidden animate-pulse">พืชx2</span>"""
content = content.replace(header_xp_old, header_xp_new)

update_ui_old = """document.getElementById('ui-gold').innerText = state.gold;"""
update_ui_new = """document.getElementById('ui-gold').innerText = state.gold;
            const uiGoldBuff = document.getElementById('ui-gold-buff');
            if (uiGoldBuff) {
                if (state.activeBuffs && state.activeBuffs.goldMultEnd && Date.now() < state.activeBuffs.goldMultEnd) {
                    uiGoldBuff.classList.remove('hidden');
                } else {
                    uiGoldBuff.classList.add('hidden');
                }
            }
            const uiCropBuff = document.getElementById('ui-crop-buff');
            if (uiCropBuff) {
                if (state.activeBuffs && state.activeBuffs.cropSpeedEnd && Date.now() < state.activeBuffs.cropSpeedEnd) {
                    uiCropBuff.classList.remove('hidden');
                } else {
                    uiCropBuff.classList.add('hidden');
                }
            }"""
content = content.replace(update_ui_old, update_ui_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

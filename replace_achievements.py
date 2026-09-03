import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

achievements_tab_old = """                        <button id="tab-achievements" onclick="switchTab('achievements')" class="px-4 py-2.5 rounded-xl text-sm font-bold text-green-700 hover:bg-white/70 transition flex-1">
                            🏆 ความสำเร็จ
                        </button>"""

calendar_new = """                        <div id="ui-calendar" class="px-4 py-2.5 rounded-xl text-sm font-bold bg-white/80 shadow-sm border border-blue-200 text-blue-800 flex-1 flex items-center justify-center whitespace-nowrap min-w-[200px]">
                            ปี 1 ฤดูใบไม้ผลิ วันที่ 1 | 6:00 AM
                        </div>"""

content = content.replace(achievements_tab_old, calendar_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

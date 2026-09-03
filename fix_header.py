import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add ui-calendar to the header
header_old = """            <!-- Level & Name -->
            <div class="flex items-center gap-4 bg-white/60 p-2 pr-4 rounded-2xl border border-white shadow-sm w-full md:w-auto">"""
header_new = """            <!-- Level & Name -->
            <div class="flex flex-col items-start gap-1 bg-white/60 p-2 pr-4 rounded-2xl border border-white shadow-sm w-full md:w-auto">
                <div class="text-xs font-bold text-gray-700 bg-white/80 px-2 py-0.5 rounded-full shadow-sm" id="ui-calendar">ปี 1 ฤดูใบไม้ผลิ วันที่ 1 | 6:00 AM</div>
                <div class="flex items-center gap-4">"""
content = content.replace(header_old, header_new)

# Add closing div for the added flex-col wrapper
header_close_old = """                    </div>
                </div>
            </div>
            
            <!-- Gold & Music -->"""
header_close_new = """                    </div>
                </div>
                </div>
            </div>
            
            <!-- Gold & Music -->"""
content = content.replace(header_close_old, header_close_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

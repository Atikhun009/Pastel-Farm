import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_cal = """<div id="ui-calendar" class="px-3 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-white/80 shadow-sm border border-blue-200 text-blue-800 flex-1 flex items-center justify-center min-w-0 text-center break-words leading-tight">"""
new_cal = """<div id="ui-calendar" class="px-4 py-2.5 rounded-xl text-xs sm:text-sm font-bold bg-white/80 shadow-sm border border-blue-200 text-blue-800 flex-none flex items-center justify-center whitespace-nowrap">"""

content = content.replace(old_cal, new_cal)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

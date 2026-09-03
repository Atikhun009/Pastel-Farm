import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the backdrop darker/blurrier
content = content.replace("bg-green-900/20 backdrop-blur-sm", "bg-green-900/40 backdrop-blur-md")

# Upgrade Modal containers
old_alert = r"class=\"glass-panel p-8 rounded-\[2rem\] max-w-sm w-full mx-4 shadow-2xl text-center border-2 border-white\""
new_alert = r"class=\"bg-gradient-to-b from-white to-green-50/95 backdrop-blur-xl p-8 rounded-[2.5rem] max-w-sm w-full mx-4 shadow-[0_20px_60px_-15px_rgba(0,0,0,0.3)] shadow-green-900/20 border-[3px] border-white/70 text-center transform transition-transform\""
content = re.sub(old_alert, new_alert, content)

old_sell = r"class=\"glass-panel p-6 md:p-8 rounded-\[2rem\] max-w-sm w-full mx-4 shadow-2xl border-2 border-white text-center\""
new_sell = r"class=\"bg-gradient-to-b from-white to-green-50/95 backdrop-blur-xl p-6 md:p-8 rounded-[2.5rem] max-w-sm w-full mx-4 shadow-[0_20px_60px_-15px_rgba(0,0,0,0.3)] shadow-green-900/20 border-[3px] border-white/70 text-center\""
content = re.sub(old_sell, new_sell, content)

old_seed = r"class=\"glass-panel p-6 md:p-8 rounded-\[2rem\] max-w-md w-full mx-4 shadow-2xl border-2 border-white\""
new_seed = r"class=\"bg-gradient-to-b from-white to-green-50/95 backdrop-blur-xl p-6 md:p-8 rounded-[2.5rem] max-w-md w-full mx-4 shadow-[0_20px_60px_-15px_rgba(0,0,0,0.3)] shadow-green-900/20 border-[3px] border-white/70\""
content = re.sub(old_seed, new_seed, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


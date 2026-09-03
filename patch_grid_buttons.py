import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_seed_btn = r"class=\"flex flex-col items-center p-3 bg-gray-50 hover:bg-green-50 border border-gray-200 hover:border-green-300 rounded-2xl transition shadow-sm\""
new_seed_btn = r"class=\"flex flex-col items-center p-4 bg-white hover:bg-green-50 border-2 border-gray-100 hover:border-green-400 rounded-[1.5rem] transition-all duration-200 shadow-sm hover:shadow-md transform hover:-translate-y-1\""
content = re.sub(old_seed_btn, new_seed_btn, content)

old_animal_btn = r"class=\"glass p-3 rounded-xl flex flex-col items-center hover:bg-white\/60 transition cursor-pointer\""
new_animal_btn = r"class=\"flex flex-col items-center p-4 bg-white hover:bg-green-50 border-2 border-gray-100 hover:border-green-400 rounded-[1.5rem] transition-all duration-200 shadow-sm hover:shadow-md transform hover:-translate-y-1 cursor-pointer\""
content = re.sub(old_animal_btn, new_animal_btn, content)

old_animal_btn_disabled = r"class=\"glass p-3 rounded-xl flex flex-col items-center opacity-60 grayscale cursor-not-allowed\""
new_animal_btn_disabled = r"class=\"flex flex-col items-center p-4 bg-gray-50 border-2 border-gray-100 rounded-[1.5rem] opacity-60 grayscale cursor-not-allowed\""
content = re.sub(old_animal_btn_disabled, new_animal_btn_disabled, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_cooking_html = """                <section class="glass-panel p-5 md:p-6 rounded-[2rem]">
                    <div class="flex justify-between items-center mb-5">
                        <h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
                            <span class="text-2xl">🍳</span> ห้องครัว
                        </h2>
                    </div>
                    
                    <div id="cooking-recipes" class="grid grid-cols-1 md:grid-cols-2 gap-4">"""

new_cooking_html = """                <section class="glass-panel p-5 md:p-6 rounded-[2rem]">
                    <div class="flex justify-between items-center mb-5">
                        <h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
                            <span class="text-2xl">🍳</span> ห้องครัว
                        </h2>
                    </div>
                    
                    <!-- Cooking Slots -->
                    <div id="cooking-slots-container" class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6"></div>
                    
                    <h3 class="text-lg font-bold text-gray-700 mb-3 border-b pb-2">สมุดสูตรอาหาร</h3>
                    <div id="cooking-recipes" class="grid grid-cols-1 md:grid-cols-2 gap-4">"""

content = content.replace(old_cooking_html, new_cooking_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

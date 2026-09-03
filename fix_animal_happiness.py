import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Animal happiness bar
old_producing = """                    <div id="pen-${pen.id}-producing" class="w-full flex flex-col items-center hidden">
                        <span id="pen-${pen.id}-emoji" class="text-4xl md:text-5xl mb-2 md:mb-3 drop-shadow-sm sway animate-pulse">🐔</span>
                        <div class="w-full h-2 bg-white/60 rounded-full overflow-hidden shadow-inner border border-white">
                            <div id="pen-${pen.id}-bar" class="h-full bg-gradient-to-r from-amber-400 to-orange-400 progress-bar-fill" style="width: 0%"></div>
                        </div>
                    </div>"""

new_producing = """                    <div id="pen-${pen.id}-producing" class="w-full flex flex-col items-center hidden relative">
                        <div class="absolute -top-2 -right-2 bg-white/80 rounded-full px-1.5 py-0.5 text-[10px] font-bold text-pink-500 shadow-sm flex items-center gap-1 border border-pink-100 z-20">
                            💖 <span id="pen-${pen.id}-happiness">0</span>
                        </div>
                        <span id="pen-${pen.id}-emoji" class="text-4xl md:text-5xl mb-2 md:mb-3 drop-shadow-sm sway animate-pulse">🐔</span>
                        <div class="w-full h-2 bg-white/60 rounded-full overflow-hidden shadow-inner border border-white mb-1">
                            <div id="pen-${pen.id}-bar" class="h-full bg-gradient-to-r from-amber-400 to-orange-400 progress-bar-fill" style="width: 0%"></div>
                        </div>
                    </div>"""

content = content.replace(old_producing, new_producing)

# Update happiness in gameloop (updateUI handles it? Let's check updateUI)
# Actually, updateUI doesn't renderPensDOM entirely, it just sets attributes.
old_pen_update = """                        document.getElementById(`pen-${pen.id}-emoji`).innerText = animal.emoji;
                        document.getElementById(`pen-${pen.id}-bar`).style.width = `${progress}%`;
                    }"""
new_pen_update = """                        document.getElementById(`pen-${pen.id}-emoji`).innerText = animal.emoji;
                        document.getElementById(`pen-${pen.id}-bar`).style.width = `${progress}%`;
                        const hapEl = document.getElementById(`pen-${pen.id}-happiness`);
                        if (hapEl) hapEl.innerText = (pen.happiness || 0);
                    }"""
content = content.replace(old_pen_update, new_pen_update)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

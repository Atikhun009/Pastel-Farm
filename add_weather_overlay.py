import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update renderPlotsDOM to include weather icon overlay
old_renderPlotsDOM = """                    <button id="plot-${plot.id}-fertilize" onclick="fertilize(${plot.id}, event)" class="absolute top-1 right-1 bg-purple-50 hover:bg-purple-100 border border-purple-200 p-1.5 rounded-full text-xs shadow-sm z-30 hidden" title="ใช้ปุ๋ยเร่งโต">
                        💩 <span class="text-[10px] font-bold text-purple-800" id="plot-${plot.id}-fert-count"></span>
                    </button>
                </div>
            `).join('');"""

new_renderPlotsDOM = """                    <button id="plot-${plot.id}-fertilize" onclick="fertilize(${plot.id}, event)" class="absolute top-1 right-1 bg-purple-50 hover:bg-purple-100 border border-purple-200 p-1.5 rounded-full text-xs shadow-sm z-30 hidden" title="ใช้ปุ๋ยเร่งโต">
                        💩 <span class="text-[10px] font-bold text-purple-800" id="plot-${plot.id}-fert-count"></span>
                    </button>
                    <div id="plot-${plot.id}-weather" class="absolute top-1 left-1 p-1.5 rounded-full text-[10px] shadow-sm z-30 hidden transition-all"></div>
                </div>
            `).join('');"""

if old_renderPlotsDOM in content:
    content = content.replace(old_renderPlotsDOM, new_renderPlotsDOM)
    print("renderPlotsDOM updated")

# 2. Update updateUI to show/hide the weather overlay
old_updateUI_loop = """                        if (elFertilize) {
                            if (state.inventory.fertilizer > 0) {
                                elFertilize.classList.remove('hidden');
                                document.getElementById(`plot-${plot.id}-fert-count`).innerText = state.inventory.fertilizer;
                            } else {
                                elFertilize.classList.add('hidden');
                            }
                        }
                        
                        const pEmoji = document.getElementById(`plot-${plot.id}-emoji`);"""

new_updateUI_loop = """                        if (elFertilize) {
                            if (state.inventory.fertilizer > 0) {
                                elFertilize.classList.remove('hidden');
                                document.getElementById(`plot-${plot.id}-fert-count`).innerText = state.inventory.fertilizer;
                            } else {
                                elFertilize.classList.add('hidden');
                            }
                        }
                        
                        const wOverlay = document.getElementById(`plot-${plot.id}-weather`);
                        if (wOverlay) {
                            if (state.weather === 'rainy') {
                                wOverlay.classList.remove('hidden');
                                wOverlay.innerText = '🌧️';
                                wOverlay.className = 'absolute top-1 left-1 p-1 rounded-full text-[10px] shadow-sm z-30 transition-all bg-indigo-100/90 border border-indigo-200 animate-pulse';
                                wOverlay.title = 'ฝนตก (โตไว 2x)';
                            } else if (state.weather === 'snowy') {
                                wOverlay.classList.remove('hidden');
                                wOverlay.innerText = '❄️';
                                wOverlay.className = 'absolute top-1 left-1 p-1 rounded-full text-[10px] shadow-sm z-30 transition-all bg-blue-100/90 border border-blue-200';
                                wOverlay.title = 'หิมะตก (โตช้า 0.5x)';
                            } else {
                                wOverlay.classList.add('hidden');
                            }
                        }
                        
                        const pEmoji = document.getElementById(`plot-${plot.id}-emoji`);"""

if old_updateUI_loop in content:
    content = content.replace(old_updateUI_loop, new_updateUI_loop)
    print("updateUI loop updated")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

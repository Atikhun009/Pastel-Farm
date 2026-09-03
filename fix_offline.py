import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_offline = """                            const earnKeys = Object.keys(offlineEarnings);
                            if (earnKeys.length > 0) {
                                const earnStr = earnKeys.map(k => `${PRODUCTS[k].emoji} ${PRODUCTS[k].name} x${offlineEarnings[k]}`).join(', ');
                                offlineMsgs.push(`<div class="text-left text-sm mb-2 text-gray-700"><b>💤 ขณะที่คุณไม่อยู่:</b><br/>สัตว์เลี้ยงผลิต ${earnStr}<br/>ได้รับ <span class="text-green-600 font-bold">${offlineXP} XP</span></div>`);
                                state.xp += offlineXP;
                            }"""

new_offline = """                            const earnKeys = Object.keys(offlineEarnings);
                            if (earnKeys.length > 0) {
                                let totalAdded = 0;
                                earnKeys.forEach(k => totalAdded += offlineEarnings[k]);
                                
                                const curItems = getCurrentItemsCount();
                                const maxCap = getBarnCapacity();
                                
                                if (curItems + totalAdded > maxCap) {
                                    // limit it
                                    const availableSpace = Math.max(0, maxCap - curItems);
                                    let spaceLeft = availableSpace;
                                    earnKeys.forEach(k => {
                                        if (spaceLeft > 0) {
                                            const addAmt = Math.min(offlineEarnings[k], spaceLeft);
                                            // subtract what we can't add from the inventory since it was already added above in loop
                                            state.inventory.products[k] -= (offlineEarnings[k] - addAmt);
                                            offlineEarnings[k] = addAmt;
                                            spaceLeft -= addAmt;
                                        } else {
                                            state.inventory.products[k] -= offlineEarnings[k];
                                            offlineEarnings[k] = 0;
                                        }
                                    });
                                    offlineMsgs.push(`<div class="text-left text-sm mb-2 text-red-600 bg-red-50 p-2 rounded-lg border border-red-200"><b>⚠️ โรงนาเต็ม!</b><br/>สัตว์เลี้ยงผลิตของได้ไม่เต็มที่เนื่องจากพื้นที่ไม่พอ</div>`);
                                }
                                
                                const finalKeys = earnKeys.filter(k => offlineEarnings[k] > 0);
                                if (finalKeys.length > 0) {
                                    const earnStr = finalKeys.map(k => `${PRODUCTS[k].emoji} ${PRODUCTS[k].name} x${offlineEarnings[k]}`).join(', ');
                                    offlineMsgs.push(`<div class="text-left text-sm mb-2 text-gray-700"><b>💤 ขณะที่คุณไม่อยู่:</b><br/>สัตว์เลี้ยงผลิต ${earnStr}<br/>ได้รับ <span class="text-green-600 font-bold">${offlineXP} XP</span></div>`);
                                    state.xp += offlineXP;
                                }
                            }"""

content = content.replace(old_offline, new_offline)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

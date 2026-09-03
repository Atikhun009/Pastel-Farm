import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add toast container
toast_html = '    <div id="toast-container" class="fixed bottom-20 right-4 z-50 flex flex-col gap-2 pointer-events-none"></div>\n</body>'
content = content.replace('</body>', toast_html)

# 2. Add showToast function
show_toast_func = """        function showToast(title, desc, icon = '✨') {
            const container = document.getElementById('toast-container');
            if (!container) return;
            const toast = document.createElement('div');
            toast.className = 'glass p-3 rounded-xl shadow-lg flex items-center gap-3 bg-white/90 border-l-4 border-green-400 transition-all duration-300 transform translate-x-full';
            toast.innerHTML = `
                <div class="text-2xl">${icon}</div>
                <div>
                    <div class="font-bold text-gray-800 text-sm">${title}</div>
                    <div class="text-[10px] text-gray-500">${desc}</div>
                </div>
            `;
            container.appendChild(toast);
            
            // Animate in
            requestAnimationFrame(() => {
                toast.classList.remove('translate-x-full');
            });
            
            // Remove after 3 seconds
            setTimeout(() => {
                toast.classList.add('opacity-0', 'translate-x-full');
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        }

        function showAlert(title, desc, icon = '✨') {"""
content = content.replace("        function showAlert(title, desc, icon = '✨') {", show_toast_func)

# 3. Replace sprinkler alert with showToast
content = content.replace("showAlert('สปริงเกอร์ทำงาน!', 'เมล็ดพันธุ์ได้รับน้ำและโตเต็มที่ทันที!', '💦');", "showToast('สปริงเกอร์ทำงาน!', 'เมล็ดพันธุ์โตเต็มที่ทันที!', '💦');")

# Also auto_harvest etc. if any uses showAlert. Wait, does auto_harvest use it? Let's check `autoHarvest()` or others.
# I will check after saving this.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


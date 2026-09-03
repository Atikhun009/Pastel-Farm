import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_glass_btn = """        .glass-btn {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(255, 255, 255, 0.9);
            transition: all 0.2s ease;
        }
        .glass-btn:hover:not(:disabled) {
            background: rgba(255, 255, 255, 1);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }"""

new_glass_btn = """        .glass-btn {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(255, 255, 255, 0.9);
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        .glass-btn:hover:not(:disabled) {
            background: rgba(255, 255, 255, 1);
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.08);
        }
        .glass-btn:active:not(:disabled) {
            transform: translateY(1px) scale(0.98);
        }
        button {
            transition: all 0.2s ease;
        }
        button:active:not(:disabled) {
            transform: scale(0.95);
        }"""

content = content.replace(old_glass_btn, new_glass_btn)

old_scale = """        .hidden-scale {
            opacity: 0;
            transform: scale(0.95);
            pointer-events: none;
        }
        .visible-scale {
            opacity: 1;
            transform: scale(1);
            pointer-events: auto;
        }"""

new_scale = """        .hidden-scale {
            opacity: 0;
            transform: scale(0.9) translateY(20px);
            pointer-events: none;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        .visible-scale {
            opacity: 1;
            transform: scale(1) translateY(0);
            pointer-events: auto;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        
        /* Smooth tab transition */
        .tab-content {
            animation: fadeInTab 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        @keyframes fadeInTab {
            from { opacity: 0; transform: translateY(10px) scale(0.98); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }"""

content = content.replace(old_scale, new_scale)

# add tab-content class to views
content = content.replace('id="view-farm" class="space-y-6"', 'id="view-farm" class="space-y-6 tab-content"')
content = content.replace('id="view-market" class="space-y-6 hidden"', 'id="view-market" class="space-y-6 hidden tab-content"')
content = content.replace('id="view-inventory" class="space-y-6 hidden"', 'id="view-inventory" class="space-y-6 hidden tab-content"')
content = content.replace('id="view-cooking" class="space-y-6 hidden"', 'id="view-cooking" class="space-y-6 hidden tab-content"')
content = content.replace('id="view-quests" class="space-y-6 hidden"', 'id="view-quests" class="space-y-6 hidden tab-content"')
content = content.replace('id="view-orders" class="space-y-6 hidden"', 'id="view-orders" class="space-y-6 hidden tab-content"')
content = content.replace('id="view-achievements" class="space-y-6 hidden"', 'id="view-achievements" class="space-y-6 hidden tab-content"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

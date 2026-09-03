import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_alert = """        function showAlert(title, desc, icon = '✨') {
            document.getElementById('alert-title').innerText = title;
            document.getElementById('alert-desc').innerText = desc;
            document.getElementById('alert-icon').innerText = icon;"""

new_alert = """        function showAlert(title, desc, icon = '✨') {
            document.getElementById('alert-title').innerText = title;
            document.getElementById('alert-desc').innerHTML = desc;
            document.getElementById('alert-icon').innerText = icon;"""

content = content.replace(old_alert, new_alert)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

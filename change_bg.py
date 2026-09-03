import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Current default background classes in the HTML head (if any) or body tag
old_body = r'<body class="min-h-screen font-sans text-gray-800 p-2 md:p-6 pb-24 md:pb-6 overflow-x-hidden selection:bg-green-200[^"]*">'
new_body = r'<body class="min-h-screen font-sans text-gray-800 p-2 md:p-6 pb-24 md:pb-6 overflow-x-hidden selection:bg-green-200 bg-cover bg-center bg-fixed transition-all duration-1000" id="game-body">'
content = re.sub(old_body, new_body, content)


# In the script, find where it changes colors and change it to set background images
old_season_change = r"document\.body\.className = `min-h-screen font-sans text-gray-800 p-2 md:p-6 pb-24 md:pb-6 overflow-x-hidden selection:bg-green-200 transition-colors duration-1000 \$\{currentSeason === 'spring' \? 'bg-pink-50' : currentSeason === 'summer' \? 'bg-green-50' : currentSeason === 'autumn' \? 'bg-orange-50' : 'bg-blue-50'\}`;"
new_season_change = r"""const body = document.getElementById('game-body');
                if (currentSeason === 'spring') {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1490750967868-88aa4486c946?q=80&w=2071&auto=format&fit=crop')";
                    body.style.backgroundColor = "#fdf2f8";
                } else if (currentSeason === 'summer') {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1501426026826-31c667bdf23d?q=80&w=1936&auto=format&fit=crop')";
                    body.style.backgroundColor = "#f0fdf4";
                } else if (currentSeason === 'autumn') {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1477414348463-c0eb7f1359b6?q=80&w=2070&auto=format&fit=crop')";
                    body.style.backgroundColor = "#fff7ed";
                } else {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1478265409131-1f65c88f965c?q=80&w=1935&auto=format&fit=crop')";
                    body.style.backgroundColor = "#eff6ff";
                }"""
content = re.sub(old_season_change, new_season_change, content)

old_initial_change = r"document\.body\.className = `min-h-screen font-sans text-gray-800 p-2 md:p-6 pb-24 md:pb-6 overflow-x-hidden selection:bg-green-200 transition-colors duration-1000 \$\{state\.season === 'spring' \? 'bg-pink-50' : state\.season === 'summer' \? 'bg-green-50' : state\.season === 'autumn' \? 'bg-orange-50' : 'bg-blue-50'\}`;"
new_initial_change = r"""const body = document.getElementById('game-body');
                if (state.season === 'spring') {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1490750967868-88aa4486c946?q=80&w=2071&auto=format&fit=crop')";
                    body.style.backgroundColor = "#fdf2f8";
                } else if (state.season === 'summer') {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1501426026826-31c667bdf23d?q=80&w=1936&auto=format&fit=crop')";
                    body.style.backgroundColor = "#f0fdf4";
                } else if (state.season === 'autumn') {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1477414348463-c0eb7f1359b6?q=80&w=2070&auto=format&fit=crop')";
                    body.style.backgroundColor = "#fff7ed";
                } else {
                    body.style.backgroundImage = "url('https://images.unsplash.com/photo-1478265409131-1f65c88f965c?q=80&w=1935&auto=format&fit=crop')";
                    body.style.backgroundColor = "#eff6ff";
                }"""
content = re.sub(old_initial_change, new_initial_change, content)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

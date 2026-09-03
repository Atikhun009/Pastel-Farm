import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace multiple toggleAutoPlanter functions
pattern = r"([ \t]*function toggleAutoPlanter\(\) \{\s*state.autoPlanterActive = state.autoPlanterActive === false \? true : false;\s*updateUI\(\);\s*\})+\s*"
replacement = r"        function toggleAutoPlanter() {\n            state.autoPlanterActive = state.autoPlanterActive === false ? true : false;\n            updateUI();\n        }\n"
content = re.sub(pattern, replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

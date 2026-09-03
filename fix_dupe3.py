import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def dedup(text):
    chunk = "        function toggleAutoPlanter() {\n            state.autoPlanterActive = state.autoPlanterActive === false ? true : false;\n            updateUI();\n        }\n"
    while content.count(chunk) > 1:
        text = text.replace(chunk + chunk, chunk)
    return text

content = content.replace("        function toggleAutoPlanter() {\n            state.autoPlanterActive = state.autoPlanterActive === false ? true : false;\n            updateUI();\n        }\n        function toggleAutoPlanter() {\n            state.autoPlanterActive = state.autoPlanterActive === false ? true : false;\n            updateUI();\n        }", "        function toggleAutoPlanter() {\n            state.autoPlanterActive = state.autoPlanterActive === false ? true : false;\n            updateUI();\n        }")

# Just to be safe, brute force it
content = re.sub(r"(function toggleAutoPlanter\(\) \{[^\}]+\}\s*){2,}", r"function toggleAutoPlanter() {\n            state.autoPlanterActive = state.autoPlanterActive === false ? true : false;\n            updateUI();\n        }\n", content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

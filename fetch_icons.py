import urllib.request
import json
import re
import os

icons = [
    'python', 'fastapi', 'svelte', 'typescript', 'javascript',
    'nodedotjs', 'postgresql', 'mongodb', 'docker', 'githubactions',
    'googlecloud', 'linkedin', 'youtube', 'instagram', 'github'
]

results = {}
for ic in icons:
    url = f"https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/{ic}.svg"
    try:
        content = urllib.request.urlopen(url).read().decode('utf-8')
        m = re.search(r'd="([^"]+)"', content)
        if m:
            results[ic] = m.group(1)
            print(f"{ic}: OK")
        else:
            print(f"{ic}: no path found")
    except Exception as e:
        print(f"{ic}: failed {e}")

os.makedirs('assets', exist_ok=True)
with open('assets/icons.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
print("Icons fetched successfully.")

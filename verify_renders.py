import os
import subprocess
import time
from PIL import Image

os.makedirs('verification_renders', exist_ok=True)
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

svg_files = [
    ('hero', 'assets/hero.svg', 850, 420),
    ('about-life', 'assets/about-life.svg', 850, 410),
    ('stack', 'assets/stack.svg', 850, 510),
    ('id-dashboard', 'assets/id-dashboard.svg', 850, 560),
    ('connect', 'assets/connect.svg', 850, 370)
]

timestamps = [0, 2, 5, 9, 13]

print("Starting verification rendering...")

for name, filepath, width, height in svg_files:
    # 1. Test at each timestamp: 0, 2, 5, 9, 13s
    for t in timestamps:
        # Create an HTML wrapper that sets animation-delay: -{t}s on all animated elements
        html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{
      margin: 0;
      padding: 0;
      background: #030712;
      display: flex;
      justify-content: center;
      align-items: center;
      width: {width}px;
      height: {height}px;
      overflow: hidden;
    }}
    /* Offset animation time by {t} seconds */
    svg * {{
      animation-delay: -{t}s !important;
    }}
  </style>
</head>
<body>
  {open(filepath, 'r', encoding='utf-8').read()}
</body>
</html>
"""
        html_path = os.path.abspath(f'verification_renders/temp_{name}_{t}s.html')
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        out_img = os.path.abspath(f'verification_renders/{name}_{t}s.png')
        url = 'file:///' + html_path.replace('\\', '/')
        res = subprocess.run([
            chrome,
            '--headless=new',
            '--disable-gpu',
            f'--screenshot={out_img}',
            f'--window-size={width},{height}',
            url
        ], capture_output=True, text=True)

        if os.path.exists(out_img):
            im = Image.open(out_img)
            print(f"[{name}] {t}s render: OK ({im.size})")
        else:
            print(f"[{name}] {t}s render: FAILED! {res.stderr}")

    # 2. Test with animation removed (static fallback / reduced motion)
    no_anim_html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{
      margin: 0;
      padding: 0;
      background: #030712;
      width: {width}px;
      height: {height}px;
      overflow: hidden;
    }}
    svg *, svg *::before, svg *::after {{
      animation: none !important;
      transition: none !important;
    }}
  </style>
</head>
<body>
  {open(filepath, 'r', encoding='utf-8').read()}
</body>
</html>
"""
    no_anim_path = os.path.abspath(f'verification_renders/temp_{name}_no_anim.html')
    with open(no_anim_path, 'w', encoding='utf-8') as f:
        f.write(no_anim_html)

    out_no_anim = os.path.abspath(f'verification_renders/{name}_no_anim.png')
    url_no_anim = 'file:///' + no_anim_path.replace('\\', '/')
    subprocess.run([
        chrome,
        '--headless=new',
        '--disable-gpu',
        f'--screenshot={out_no_anim}',
        f'--window-size={width},{height}',
        url_no_anim
    ], capture_output=True, text=True)
    if os.path.exists(out_no_anim):
        print(f"[{name}] no_anim render: OK")

    # 3. Test as <img> element (simulating GitHub's renderer)
    img_tag_html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{
      margin: 0;
      padding: 0;
      background: #030712;
      width: {width}px;
      height: {height}px;
      overflow: hidden;
    }}
    img {{
      display: block;
      width: {width}px;
      height: {height}px;
    }}
  </style>
</head>
<body>
  <img src="file:///{os.path.abspath(filepath).replace('\\', '/')}" width="{width}" height="{height}" />
</body>
</html>
"""
    img_tag_path = os.path.abspath(f'verification_renders/temp_{name}_img_tag.html')
    with open(img_tag_path, 'w', encoding='utf-8') as f:
        f.write(img_tag_html)

    out_img_tag = os.path.abspath(f'verification_renders/{name}_img_tag.png')
    url_img_tag = 'file:///' + img_tag_path.replace('\\', '/')
    subprocess.run([
        chrome,
        '--headless=new',
        '--disable-gpu',
        f'--screenshot={out_img_tag}',
        f'--window-size={width},{height}',
        url_img_tag
    ], capture_output=True, text=True)
    if os.path.exists(out_img_tag):
        print(f"[{name}] img_tag render: OK")

print("\nVerification renders finished.")

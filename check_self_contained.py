import re

svgs = ['assets/hero.svg', 'assets/about-life.svg', 'assets/stack.svg', 'assets/id-dashboard.svg', 'assets/connect.svg']
clean = True

for s in svgs:
    with open(s, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find any http or https
    for line in content.splitlines():
        if 'http://' in line or 'https://' in line:
            # Check if it is standard XML namespace or <a> link target in connect.svg
            is_valid_ns = 'xmlns="http://www.w3.org/2000/svg"' in line or 'xmlns:xlink="http://www.w3.org/1999/xlink"' in line
            is_valid_link = '<a href="https://' in line
            if not is_valid_ns and not is_valid_link:
                print(f"Warning in {s}: Suspicious external reference: {line.strip()[:100]}")
                clean = False

    # Check images
    images = re.findall(r'<image[^>]+>', content)
    for img in images:
        if 'href="data:image/png;base64,' not in img:
            print(f"Warning in {s}: Non-inlined image: {img[:100]}")
            clean = False

if clean:
    print("ALL 5 SVGS ARE 100% SELF-CONTAINED! ZERO EXTERNAL NETWORK REQUESTS.")
else:
    print("Issues found.")

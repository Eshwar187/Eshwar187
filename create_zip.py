import zipfile
import os

zip_name = 'profile-readme.zip'
files_to_zip = [
    'README.md',
    'preview.html',
    'assets/hero.svg',
    'assets/about-life.svg',
    'assets/stack.svg',
    'assets/id-dashboard.svg',
    'assets/connect.svg',
    'assets/id.png',
    'assets/right_pointing.png',
    'assets/fonts/LICENSE-FONTS.txt'
]

with zipfile.ZipFile(zip_name, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for f in files_to_zip:
        if os.path.exists(f):
            z.write(f, arcname=f)
            print(f"Added to zip: {f} ({os.path.getsize(f)} bytes)")
        else:
            print(f"Warning: {f} not found!")

print(f"\n{zip_name} created successfully! Total size: {os.path.getsize(zip_name)} bytes.")

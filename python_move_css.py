import os
import shutil

# Define current and target paths
current_css_path = os.path.join('app', 'static', 'img', 'css', 'style.css')
target_css_dir = os.path.join('app', 'static', 'css')
target_css_path = os.path.join(target_css_dir, 'style.css')

# Make sure target directory exists
os.makedirs(target_css_dir, exist_ok=True)

# Move the file
if os.path.exists(current_css_path):
    shutil.move(current_css_path, target_css_path)
    print(f"Moved 'style.css' to {target_css_path}")
else:
    print(f"File not found at {current_css_path}")

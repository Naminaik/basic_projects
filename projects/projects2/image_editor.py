from PIL import Image,ImageEnhance, ImageFilter
import os

path = "C:\\Users\\nami\\Pictures\\Saved Pictures"
path_out = "C:\\Users\\nami\\Pictures\\Saved Pictures"

for filename in os.listdir(path):
    file_path = f"{path}/{filename}"
    try:
        # Only process image files (skip system files like desktop.ini)
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")):
            img = Image.open(file_path)
            edit = img.filter(ImageFilter.SMOOTH).convert("L").rotate(-180)
            clean_name = os.path.splitext(filename)[0]
            edit.save(f"{path_out}/{clean_name}_edited.jpg")
        else:
            print(f"Skipping non-image file: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        
from PIL import Image
import os

DATASET_PATH = "dataset"

def clean_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        try:
            with Image.open(file_path) as img:
                img.verify()  # verify image
        except:
            print(f"❌ Removing bad file: {file_path}")
            os.remove(file_path)

for class_name in os.listdir(DATASET_PATH):
    class_path = os.path.join(DATASET_PATH, class_name)
    clean_folder(class_path)

print("✅ Dataset cleaned successfully")
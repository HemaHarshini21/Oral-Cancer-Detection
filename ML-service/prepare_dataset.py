import os
import shutil

SOURCE = "raw_dataset"
TARGET = "dataset"

os.makedirs(f"{TARGET}/cancer", exist_ok=True)
os.makedirs(f"{TARGET}/normal", exist_ok=True)

for root, dirs, files in os.walk(SOURCE):
    for file in files:
        if file.endswith((".jpg", ".png", ".jpeg")):

            src = os.path.join(root, file)

            if "cancer" in root.lower() or "malignant" in root.lower():
                dst = os.path.join(TARGET, "cancer", file)
            else:
                dst = os.path.join(TARGET, "normal", file)

            try:
                shutil.copy(src, dst)
            except:
                pass

print("✅ Dataset ready")
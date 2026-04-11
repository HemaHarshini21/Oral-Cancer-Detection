import os

source = "raw_dataset"

classes = ["cancer", "normal"]

for cls in classes:
    path = os.path.join(source, cls)
    
    print("Checking:", path)

    if not os.path.exists(path):
        print("❌ Folder NOT FOUND")
    else:
        images = os.listdir(path)
        print("✅ Images found:", len(images))
import json
import os
import random
import shutil

# Define directories
train_dir = 'train'
val_dir = 'val'
dirs = [train_dir, val_dir]

# Ensure each directory exists and has the necessary subdirectories
for d in dirs:
    os.makedirs(os.path.join(d, 'images'), exist_ok=True)
    os.makedirs(os.path.join(d, 'labels'), exist_ok=True)

# Load JSON data
with open('final_merged_yolo.json', 'r') as file:
    data = json.load(file)

# List of specific source folders to search for images
source_folders = [
    'forged_checks/data',        # data subfolder of forged_checks
    'forged_signatures/data',    # data subfolder of forged_signatures
    'signature_data/images'      # images subfolder of signature_data
]

# Process each image entry
for entry in data:
    file_name = entry['file_name']
    bbox_yolo = entry['bbox_yolo']

    # Format YOLO label string
    yolo_label = f"0 {bbox_yolo[0]} {bbox_yolo[1]} {bbox_yolo[2]} {bbox_yolo[3]}"

    # Randomly choose train or validation
    target_dir = train_dir if random.random() < 0.8 else val_dir

    # Search for the image in all specified source folders
    image_found = False
    for folder in source_folders:
        image_source_path = os.path.join(folder, file_name)
        if os.path.exists(image_source_path):
            image_found = True
            break

    # If the image is found, copy it to the target "images" directory
    if image_found:
        image_target_path = os.path.join(target_dir, 'images', file_name)
        shutil.copy(image_source_path, image_target_path)

        # Write label to the target "labels" directory
        label_file_name = file_name.replace('.jpg', '.txt')
        label_path = os.path.join(target_dir, 'labels', label_file_name)
        with open(label_path, 'w') as label_file:
            label_file.write(yolo_label)
    else:
        print(f"Image {file_name} not found in any specified source folder.")

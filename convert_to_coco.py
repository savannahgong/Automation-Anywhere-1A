import json

with open("final_merged.json", "r") as f:
    input_data = json.load(f)

# COCO format structure
coco_data = {
    "images": [],
    "annotations": [],
    "categories": [
        {
            "id": 1,
            "name": "signature",
            "supercategory": "document"
        }
    ]
}

# Track unique file names and IDs
image_id_map = {}
annotation_id = 1

# Process each entry in the input data
for item in input_data:
    file_name = item["file_name"]
    
    # Assign a unique ID to each image based on file name
    if file_name not in image_id_map:
        image_id = len(image_id_map) + 1
        image_id_map[file_name] = image_id
        
        # Add image info to "images" section
        coco_data["images"].append({
            "id": image_id,
            "file_name": file_name,
            "width": item["width"],
            "height": item["height"]
        })
    else:
        image_id = image_id_map[file_name]

    # Convert bbox to COCO format: [x, y, width, height]
    x_min, y_min, x_max, y_max = item["bbox"]
    width = x_max - x_min
    height = y_max - y_min

    # Add annotation info to "annotations" section
    coco_data["annotations"].append({
        "id": annotation_id,
        "image_id": image_id,
        "category_id": 1,
        "bbox": [x_min, y_min, width, height],
        "area": width * height,
        "iscrowd": 0
    })
    
    annotation_id += 1

# Save the output in COCO format
with open("coco_format.json", "w") as f:
    json.dump(coco_data, f, indent=4)

print("Conversion complete. COCO format saved to 'coco_format.json'.")

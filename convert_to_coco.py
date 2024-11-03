import json
from sklearn.model_selection import train_test_split

# Load data from coco_format.json
with open("coco_format.json", "r") as f:
    coco_data = json.load(f)

# Initialize COCO structures for train and validation sets
coco_train = {
    "images": [],
    "annotations": [],
    "categories": coco_data["categories"]
}

coco_val = {
    "images": [],
    "annotations": [],
    "categories": coco_data["categories"]
}

# Map images and annotations for easy splitting
image_id_map = {img["id"]: img for img in coco_data["images"]}
annotations_map = {}

for ann in coco_data["annotations"]:
    image_id = ann["image_id"]
    if image_id not in annotations_map:
        annotations_map[image_id] = []
    annotations_map[image_id].append(ann)

# Split images into train and validation sets (80-20 split)
image_ids = list(image_id_map.keys())
train_ids, val_ids = train_test_split(image_ids, test_size=0.2, random_state=42)

# Assign images and annotations to train and validation COCO structures
for image_id in train_ids:
    coco_train["images"].append(image_id_map[image_id])
    if image_id in annotations_map:
        coco_train["annotations"].extend(annotations_map[image_id])

for image_id in val_ids:
    coco_val["images"].append(image_id_map[image_id])
    if image_id in annotations_map:
        coco_val["annotations"].extend(annotations_map[image_id])

# Save the output files in COCO format
with open("coco_train.json", "w") as f:
    json.dump(coco_train, f, indent=4)

with open("coco_val.json", "w") as f:
    json.dump(coco_val, f, indent=4)

print("Dataset split complete. COCO format files saved as 'coco_train.json' and 'coco_val.json'.")




# import json

# with open("final_merged.json", "r") as f:
#     input_data = json.load(f)

# # COCO format structure
# coco_data = {
#     "images": [],
#     "annotations": [],
#     "categories": [
#         {
#             "id": 1,
#             "name": "signature",
#             "supercategory": "document"
#         }
#     ]
# }

# # Track unique file names and IDs
# image_id_map = {}
# annotation_id = 1

# # Process each entry in the input data
# for item in input_data:
#     file_name = item["file_name"]
    
#     # Assign a unique ID to each image based on file name
#     if file_name not in image_id_map:
#         image_id = len(image_id_map) + 1
#         image_id_map[file_name] = image_id
        
#         # Add image info to "images" section
#         coco_data["images"].append({
#             "id": image_id,
#             "file_name": file_name,
#             "width": item["width"],
#             "height": item["height"]
#         })
#     else:
#         image_id = image_id_map[file_name]

#     # Convert bbox to COCO format: [x, y, width, height]
#     x_min, y_min, x_max, y_max = item["bbox"]
#     width = x_max - x_min
#     height = y_max - y_min

#     # Add annotation info to "annotations" section
#     coco_data["annotations"].append({
#         "id": annotation_id,
#         "image_id": image_id,
#         "category_id": 1,
#         "bbox": [x_min, y_min, width, height],
#         "area": width * height,
#         "iscrowd": 0
#     })
    
#     annotation_id += 1

# # Save the output in COCO format
# with open("coco_format.json", "w") as f:
#     json.dump(coco_data, f, indent=4)

# print("Conversion complete. COCO format saved to 'coco_format.json'.")

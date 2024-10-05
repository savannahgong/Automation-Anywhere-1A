

import json

# Load the two labels.json files
with open('forged_checks/labels.json') as f1, open('forged_signatures/labels.json') as f2:
    forged_checks_data = json.load(f1)
    forged_signatures_data = json.load(f2)

# Create a category mapping based on the current categories in forged_checks
category_mapping = {category['name']: category['id'] for category in forged_checks_data['categories']}

# Start with the next available category id
next_category_id = max(category_mapping.values()) + 1 if category_mapping else 1

# Merge categories from forged_signatures into forged_checks if not present
for category in forged_signatures_data['categories']:
    if category['name'] not in category_mapping:
        # Add new category and assign the next available category id
        category['id'] = next_category_id
        category_mapping[category['name']] = next_category_id
        forged_checks_data['categories'].append(category)
        next_category_id += 1

# Merge images
images = forged_checks_data['images']
image_offset = len(images)  # To handle unique image IDs
for img in forged_signatures_data['images']:
    img['id'] += image_offset  # Adjust image ID
    images.append(img)

# Merge annotations from forged_signatures
if 'annotations' in forged_signatures_data:
    annotations = forged_signatures_data['annotations']
    for ann in annotations:
        ann['image_id'] += image_offset  # Adjust image ID
        # Update category_id based on the new category mapping
        ann['category_id'] = category_mapping['signature']  # Assuming all annotations are for 'signature'
        if 'annotations' not in forged_checks_data:
            forged_checks_data['annotations'] = []
        forged_checks_data['annotations'].append(ann)

# Create the combined JSON data
combined_data = {
    "info": forged_checks_data['info'],
    "licenses": forged_checks_data['licenses'],
    "categories": forged_checks_data['categories'],
    "images": forged_checks_data['images'],
}

# If annotations exist, include them
if 'annotations' in forged_checks_data:
    combined_data['annotations'] = forged_checks_data['annotations']

# Write to a new combined_labels.json file
with open('combined_labels.json', 'w') as outfile:
    json.dump(combined_data, outfile, indent=4)

print("JSON files successfully merged into combined_labels.json")

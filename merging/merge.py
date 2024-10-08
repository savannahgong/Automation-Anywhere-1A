# Outputs merged_signatures.json

import json

# File paths
combined_forged_signatures_path = 'combined_forged_signatures.json'
updated_combined_signatures_path = 'updated_combined_signatures.json'
output_json_path = 'merged_signatures.json'

# Load the JSON data from both files
with open(combined_forged_signatures_path, 'r') as f:
    forged_data = json.load(f)

with open(updated_combined_signatures_path, 'r') as f:
    updated_data = json.load(f)

# Create a dictionary to hold the merged data
merged_data = {}

# Process the forged signatures data (retain original bbox format)
for entry in forged_data:
    file_name = entry['file_name']
    width = entry['width']
    height = entry['height']
    bbox = entry['bbox']  # Retain bbox as is

    if file_name not in merged_data:
        merged_data[file_name] = {
            'file_name': file_name,
            'width': width,
            'height': height,
            'bboxes': []  # Create bboxes key to store all bounding boxes
        }
    merged_data[file_name]['bboxes'].append(bbox)

# Process the updated signatures data (merge bbox information)
for entry in updated_data:
    file_name = entry['file_name']
    width = entry['width']
    height = entry['height']
    bboxes = entry['bboxes']  # Assume bboxes is already in a list format

    if file_name not in merged_data:
        merged_data[file_name] = {
            'file_name': file_name,
            'width': width,
            'height': height,
            'bboxes': bboxes  # Directly add all bboxes from updated data
        }
    else:
        # Append bounding boxes if the file_name already exists
        merged_data[file_name]['bboxes'].extend(bboxes)

# Convert the merged data back to a list
merged_list = list(merged_data.values())

# Save the merged data to a new JSON file
with open(output_json_path, 'w') as f:
    json.dump(merged_list, f, indent=4)

print(f"Merged data has been written to {output_json_path}")

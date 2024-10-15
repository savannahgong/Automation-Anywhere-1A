import json

# Load the JSON data
with open('merging/combined_forged_signatures.json', 'r') as f:
    data = json.load(f)

# Update the bbox values
for item in data:
    xmin, ymin, xmin_offset, ymin_offset = item['bbox']
    item['bbox'][2] = xmin + xmin_offset  # Update xmin_offset
    item['bbox'][3] = ymin + ymin_offset  # Update ymin_offset

# Save the modified JSON data back to the file
with open('combined_forged_signatures_modified.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Bounding box values have been updated and saved to 'combined_forged_signatures_modified.json'.")

# combined labels.json in forged_checks and forged signatures into combined_forged_signatures.json
# outputs combined_forged_signatures.json

import json

# Load both labels.json files
with open('forged_checks/labels.json', 'r') as file1:
    checks_data = json.load(file1)

with open('forged_signatures/labels.json', 'r') as file2:
    signatures_data = json.load(file2)

# Function to extract relevant information when category_id is 1 (signature)
def extract_signature_data(data):
    filtered_data = []
    for annotation in data['annotations']:
        if annotation['category_id'] == 1:
            image_info = next((img for img in data['images'] if img['id'] == annotation['image_id']), None)
            if image_info:
                filtered_data.append({
                    'file_name': image_info['file_name'],
                    'width': image_info['width'],
                    'height': image_info['height'],
                    'bbox': annotation['bbox']
                })
    return filtered_data

# Extract data from both files
combined_data = extract_signature_data(checks_data) + extract_signature_data(signatures_data)

# Write the combined data to a new JSON file
with open('combined_forged_signatures.json', 'w') as outfile:
    json.dump(combined_data, outfile, indent=4)

print("Data successfully combined and written to 'combined_signatures.json'.")

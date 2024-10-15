# import json

# # Load the JSON data
# with open('merging/updated_combined_signatures.json', 'r') as f:
#     data = json.load(f)

# # Create a new list to store the separated bbox entries
# separated_data = []

# # Loop through each file entry in the data
# for item in data:
#     file_name = item['file_name']
#     width = item['width']
#     height = item['height']
    
#     # For each bbox, create a new entry and append to the new list
#     for bbox in item['bboxes']:
#         new_entry = {
#             "file_name": file_name,
#             "width": width,
#             "height": height,
#             "bbox": bbox  # Add bbox data directly
#         }
#         separated_data.append(new_entry)

# # Save the modified JSON data to a new file
# with open('separated_combined_signatures.json', 'w') as f:
#     json.dump(separated_data, f, indent=4)

# print("Bboxes have been separated and saved to 'separated_combined_signatures.json'.")
import json

# Load the JSON data
with open('merging/updated_combined_signatures.json', 'r') as f:
    data = json.load(f)

# Create a new list to store the separated bbox entries
separated_data = []

# Loop through each file entry in the data
for item in data:
    file_name = item['file_name']
    width = item['width']
    height = item['height']
    
    # For each bbox, create a new entry and append to the new list
    for bbox in item['bboxes']:
        # Convert bbox from dictionary to list format [xmin, ymin, xmax, ymax]
        bbox_list = [bbox['xmin'], bbox['ymin'], bbox['xmax'], bbox['ymax']]
        
        new_entry = {
            "file_name": file_name,
            "width": width,
            "height": height,
            "bbox": bbox_list  # Store bbox as a list
        }
        separated_data.append(new_entry)

# Save the modified JSON data to a new file
with open('separated_combined_signatures.json', 'w') as f:
    json.dump(separated_data, f, indent=4)

print("Bboxes have been separated and converted to list format, saved to 'separated_combined_signatures.json'.")

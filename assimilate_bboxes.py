import json

# Load the JSON file
with open('combined_data.json', 'r') as file:
    data = json.load(file)

# Function to convert bbox to bndbox-like format
def convert_bbox_to_bndbox(bbox):
    xmin = bbox[0]
    ymin = bbox[1]
    xmax = xmin + bbox[2]  # xmax = xmin + width
    ymax = ymin + bbox[3]  # ymax = ymin + height
    return {
        "xmin": xmin,
        "xmax": xmax,
        "ymin": ymin,
        "ymax": ymax
    }

# Function to recursively process the JSON file and convert bbox fields
def process_json(data):
    if isinstance(data, dict):
        # If bbox is present, convert it to bndbox format
        if "bbox" in data:
            data["bndbox"] = convert_bbox_to_bndbox(data["bbox"])
            del data["bbox"]  # Optionally remove the original bbox if not needed
        # Recursively process inner dictionaries
        for key, value in data.items():
            process_json(value)
    elif isinstance(data, list):
        # Recursively process each item in a list
        for item in data:
            process_json(item)

# Process the JSON data
process_json(data)

# Save the modified JSON back to a file
with open('updated_bboxes_combined_data.json', 'w') as file:
    json.dump(data, file, indent=4)

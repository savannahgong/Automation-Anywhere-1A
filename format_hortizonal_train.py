import json

# Path to the JSON file
json_file_path = 'coco_train.json'

# Files with expected dimensions (Expected width, Expected height)
expected_dimensions = {
    "chicago_20.pdf_12.jpg": (2200, 1700),
    "chicago_33.pdf_17.jpg": (2200, 1700),
    "chicago_40.pdf_51.jpg": (2200, 1698),
    "chicago_40.pdf_52.jpg": (2200, 1698),
    "chicago_40.pdf_59.jpg": (2200, 1698),
    "chicago_41.pdf_43.jpg": (2214, 1695),
    "chicago_41.pdf_45.jpg": (2209, 1695),
    "chicago_41.pdf_46.jpg": (2212, 1695),
    "chicago_41.pdf_47.jpg": (2209, 1695),
    "chicago_41.pdf_48.jpg": (2209, 1695),
    "chicago_55.pdf_15.jpg": (2200, 1700),
    "chicago_55.pdf_16.jpg": (2200, 1700),
}

# Load the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Update the dimensions for specific files
for image in data['images']:
    file_name = image['file_name']
    if file_name in expected_dimensions:
        expected_width, expected_height = expected_dimensions[file_name]
        # Update width and height if they don't match expected values
        if (image['width'], image['height']) != (expected_width, expected_height):
            print(f"Updating dimensions for {file_name}: Expected ({expected_width}, {expected_height}), Actual ({image['width']}, {image['height']})")
            image['width'], image['height'] = expected_width, expected_height

# Save the updated JSON back to file
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("JSON file has been updated with the correct dimensions.")

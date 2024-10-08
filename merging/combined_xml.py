# converts the .xml annotations into .json
# outputs updated_combined_signatures.json

import os
import xml.etree.ElementTree as ET
import json

# Define paths
annotations_folder = 'signature_data/annotations'
output_json = 'updated_combined_signatures.json'

# Function to parse an XML file and extract relevant data
def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    filename = root.find('filename').text
    width = int(root.find('size/width').text)
    height = int(root.find('size/height').text)
    
    # List to store bounding boxes
    bounding_boxes = []

    # Iterate over all 'object' elements (for multiple signatures)
    for obj in root.findall('object'):
        category_name = obj.find('name').text
        if category_name == 'signature':
            bndbox = obj.find('bndbox')
            bbox = {
                'xmin': int(bndbox.find('xmin').text),
                'xmax': int(bndbox.find('xmax').text),
                'ymin': int(bndbox.find('ymin').text),
                'ymax': int(bndbox.find('ymax').text)
            }
            bounding_boxes.append(bbox)

    # Return the parsed information if any bounding boxes are found
    if bounding_boxes:
        return {
            'file_name': filename.replace('.xml', '.jpg'),
            'width': width,
            'height': height,
            'bboxes': bounding_boxes  # Store all bounding boxes for the file
        }
    return None

# List to store all signature data
signatures_data = []

# Iterate through all XML files in the annotations folder
for xml_file in os.listdir(annotations_folder):
    if xml_file.endswith('.xml'):
        xml_path = os.path.join(annotations_folder, xml_file)
        signature_info = parse_xml(xml_path)
        if signature_info:
            signatures_data.append(signature_info)

# Save combined data to a JSON file
with open(output_json, 'w') as f:
    json.dump(signatures_data, f, indent=4)

print(f"Data has been written to {output_json}")

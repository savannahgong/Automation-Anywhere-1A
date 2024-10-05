import os
import xml.etree.ElementTree as ET
import json

signature_data_images_folder = 'signature_data/images'
signature_data_annotations_folder = 'signature_data/annotations'
forged_signatures_json = 'combined_labels.json'

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    data = {
        'filename': root.find('filename').text,
        'path': root.find('path').text,
        'size': {
            'width': int(root.find('size/width').text),
            'height': int(root.find('size/height').text),
            'depth': int(root.find('size/depth').text),
        },
        'objects': []
    }
    
    for obj in root.findall('object'):
        obj_data = {
            'name': obj.find('name').text,
            'bndbox': {
                'xmin': int(obj.find('bndbox/xmin').text),
                'xmax': int(obj.find('bndbox/xmax').text),
                'ymin': int(obj.find('bndbox/ymin').text),
                'ymax': int(obj.find('bndbox/ymax').text),
            }
        }
        data['objects'].append(obj_data)
    
    return data

signature_data = []
for xml_file in os.listdir(signature_data_annotations_folder):
    if xml_file.endswith('.xml'):
        xml_path = os.path.join(signature_data_annotations_folder, xml_file)
        parsed_xml = parse_xml(xml_path)
        signature_data.append(parsed_xml)

with open(forged_signatures_json, 'r') as f:
    forged_signatures_data = json.load(f)

combined_data = {
    "signature_data": signature_data,
    "forged_signatures": forged_signatures_data
}

output_json = 'combined_data.json'
with open(output_json, 'w') as f:
    json.dump(combined_data, f, indent=4)

print(f"Combined data saved to {output_json}")

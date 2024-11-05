from ultralytics import YOLO

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# Train the model using your custom dataset
results = model.train(data='dataset.yaml', epochs=100, imgsz=640)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on a test image
results = model('path/to/test/image.jpg')

# Export the model to ONNX format
success = model.export(format='onnx')

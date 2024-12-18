# Automation-Anywhere-1A - Vision Model for Signature Detection

# Overview

This project implements a vision-based data extraction system designed to detect signatures on documents. Using state-of-the-art object detection models, YOLO and Detectron2, the system processes a dataset of various documents to identify and localize signatures with high accuracy.

# Project Workflow

1. Dataset Preparation

The dataset consists of a diverse set of documents with labeled signature regions. Each document has annotations in a format compatible with both YOLO and Detectron2 (e.g., COCO JSON for Detectron2 and TXT files for YOLO).

The dataset was split into three subsets:

Train: Used for training the models.

Validation: Used to tune hyperparameters and monitor model performance during training.

Test: Used for final evaluation of the trained models.

2. Model Selection

Two object detection frameworks were selected for the task:

YOLO (You Only Look Once):

A single-stage object detection model that predicts bounding boxes and class probabilities directly.

Chosen for its speed and suitability for real-time applications.

Used the YOLOv5 variant for training due to its improved accuracy and efficiency for detecting objects of varying sizes.

Detectron2:

A two-stage region-based convolutional neural network (R-CNN) framework.

Detectron2 first identifies regions of interest and then classifies and refines bounding boxes in these regions.

Chosen for its high accuracy, especially in detecting smaller objects, albeit at a higher computational cost.

3. Model Training

Both models were trained on the Train subset of the dataset.

Hyperparameters such as learning rate, batch size, and the number of epochs were tuned based on performance on the Validation subset.

The COCO-Detection/faster_rcnn_R_50_FPN_1x model was selected for Detectron2 due to its effectiveness in detecting small to medium-sized objects.

4. Model Evaluation

Performance was evaluated using metrics such as Precision, Recall, F1-score, and mAP (mean Average Precision) on the Test subset.

Comparisons between YOLO and Detectron2 were made to analyze trade-offs between speed and accuracy.

5. Deployment

The trained models were deployed in a pipeline to process new documents and detect signatures.

Results included the bounding box coordinates and confidence scores for each detected signature.


# Overall Results

YOLO:

Speed: High

Accuracy: Moderate (best for medium to large signatures)

Detectron2:

Speed: High

Accuracy: High (particularly effective for smaller signatures)

# Data Visualization

<img width="962" alt="Screenshot 2024-12-13 at 6 19 57 PM" src="https://github.com/user-attachments/assets/d57b81cc-e4db-4524-a3aa-83d919bd4bb1" />
<img width="962" alt="Screenshot 2024-12-13 at 6 19 57 PM" src="https://github.com/user-attachments/assets/1b8529e3-d979-4a62-a7d0-5b12885c3cc5" />


## Detectron:

# Sample Output

## Yolo:

<img width="956" alt="Screenshot 2024-12-13 at 6 22 04 PM" src="https://github.com/user-attachments/assets/75dde058-4ceb-4079-bac4-fec9a1430948" />

## Detectron:

<img width="951" alt="Screenshot 2024-12-13 at 6 21 54 PM" src="https://github.com/user-attachments/assets/1ddbac04-3f6e-499b-a9cb-8a746a61b039" />

# Individual Contributions

**Data Preprocessing:** Harini, Savannah, Ananya <br />
**Detectron2 Model:** Harini, Makayla <br />
**YOLOV8 Model:** Savannah, Ananya <br />
**Streamlit Application:** Savannah, Harini <br /> <br />

**Shoutout** to our **Challenge Advisor, Anish** and our **AI Studio TA, Aditya** for guiding us along the way

# Potential Next Steps

- Increasing AP scores for both models
- utilizing synthetic data to better train each model
- analyzing wrong predictions to find patterns in mistakes



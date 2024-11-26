import streamlit as st
from PIL import Image
import torch
import numpy as np
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from detectron2.model_zoo import get_config_file

# Page Title
st.title("Signature Identification Vision Model")

# Left column: Select Model
st.sidebar.header("Select Model")
model_choice = st.sidebar.radio("Choose your model:", ("YOLO", "Detectron2"))

# Load Detectron2 Model
@st.cache_resource
def load_detectron2_model():
    cfg = get_cfg()
    # Base configuration from a Detectron2 model zoo
    cfg.merge_from_file(get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_1x.yaml"))
    cfg.MODEL.WEIGHTS = "model_final (1).pth"  # Path to your model
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # Confidence threshold
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1  # Assuming one class (signature)
    cfg.MODEL.DEVICE = "cpu"  # Change to "cuda" if GPU is available
    return DefaultPredictor(cfg)

predictor = load_detectron2_model()

# Main Section Layout
col1, col2 = st.columns([1, 1])

# # Left column: Upload Section
# with col1:
#     st.header("Upload an Image")
#     uploaded_file = st.file_uploader("Upload your file", type=["pdf", "png", "jpg"], label_visibility="collapsed")
#     if uploaded_file:
#         st.success("File uploaded successfully!", icon="✅")
#     if st.button("Evaluate", key="evaluate"):
#         if uploaded_file:
#             st.info("Model is processing the file...")
#         else:
#             st.error("Please upload a file before evaluating.")

# # Right column: Results Section
# with col2:
#     st.header("Results")
#     # Placeholder image for signature
#     placeholder_image_path = "/Users/savannahgong/Documents/GitHub/Automation-Anywhere-1A/signature_data/images/chicago_8.pdf_2.jpg"  # Replace with the path to your placeholder image
#     try:
#         placeholder_image = Image.open(placeholder_image_path)
#         st.image(placeholder_image, caption="Detected Signature", use_column_width=True)
#     except:
#         st.text("Signature output will appear here.")
#     st.markdown("**Confidence:** 89%")

# Left Column: Upload Section
with col1:
    st.header("Upload an Image")
    uploaded_file = st.file_uploader("Upload your file", type=["png", "jpg"], label_visibility="collapsed")
    
    if uploaded_file:
        st.success("File uploaded successfully!", icon="✅")
        
        # Convert to PIL Image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Evaluate", key="evaluate"):
        if uploaded_file:
            st.info("Model is processing the file...")

            # Convert PIL image to NumPy array
            image_np = np.array(image)
            
            # Run Detectron2 Prediction
            outputs = predictor(image_np)
            v = Visualizer(image_np[:, :, ::-1], scale=0.5)
            out = v.draw_instance_predictions(outputs["instances"].to("cpu"))

            # Display results
            st.image(out.get_image()[:, :, ::-1], caption="Detected Signature", use_column_width=True)
            if len(outputs["instances"].scores) > 0:
                confidence = outputs["instances"].scores[0].item() * 100
                st.markdown(f"**Confidence:** {confidence:.2f}%")
            else:
                st.markdown("**No signatures detected.**")
        else:
            st.error("Please upload a file before evaluating.")

# Right Column: Results Section
with col2:
    st.header("Results")
    st.text("Signature output will appear here after evaluation.")

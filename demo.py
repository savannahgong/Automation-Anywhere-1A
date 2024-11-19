import streamlit as st
from PIL import Image

# Page Title
st.title("Signature Identification Vision Model")

# Left column: Select Model
st.sidebar.header("Select Model")
model_choice = st.sidebar.radio("Choose your model:", ("YOLO", "Detectron2"))

# Main Section Layout
col1, col2 = st.columns([1, 1])

# Left column: Upload Section
with col1:
    st.header("Upload an Image")
    uploaded_file = st.file_uploader("Upload your file", type=["pdf", "png", "jpg"], label_visibility="collapsed")
    if uploaded_file:
        st.success("File uploaded successfully!", icon="✅")
    if st.button("Evaluate", key="evaluate"):
        if uploaded_file:
            st.info("Model is processing the file...")
        else:
            st.error("Please upload a file before evaluating.")

# Right column: Results Section
with col2:
    st.header("Results")
    # Placeholder image for signature
    placeholder_image_path = "/Users/savannahgong/Documents/GitHub/Automation-Anywhere-1A/signature_data/images/chicago_8.pdf_2.jpg"  # Replace with the path to your placeholder image
    try:
        placeholder_image = Image.open(placeholder_image_path)
        st.image(placeholder_image, caption="Detected Signature", use_column_width=True)
    except:
        st.text("Signature output will appear here.")
    st.markdown("**Confidence:** 89%")

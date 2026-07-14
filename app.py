import os
import streamlit as st
from PIL import Image

from preprocessing import preprocess_image
from ocr import HindiOCR
from translate import HindiTranslator


# -----------------------------
# Load models only once
# -----------------------------
@st.cache_resource
def load_models():
    ocr = HindiOCR()
    translator = HindiTranslator()
    return ocr, translator


ocr, translator = load_models()


st.set_page_config(
    page_title="Offline Hindi OCR & Translation",
    layout="wide"
)

st.title("📝 Offline Hindi OCR & English Translation")

uploaded_file = st.file_uploader(
    "Upload a handwritten Hindi image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    input_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    output_path = os.path.join(
        "outputs",
        "processed_" + uploaded_file.name
    )

    preprocess_image(
        input_path,
        output_path
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(input_path)

    with col2:
        st.subheader("Processed Image")
        st.image(output_path)

    if st.button("Run OCR & Translate"):

        with st.spinner("Recognizing Hindi text..."):

            hindi = ocr.recognize(output_path)

        with st.spinner("Translating..."):

            english = translator.translate(hindi)

        st.success("Done!")

        st.subheader("Recognized Hindi Text")
        st.write(hindi)

        st.subheader("English Translation")
        st.write(english)
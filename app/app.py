import streamlit as st
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "src")

sys.path.append(SRC_DIR)

from predict import predict_audio

st.set_page_config(
    page_title="Deepfake Audio Detection",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ Deepfake Audio Detection")

st.write(
    """
    Upload a WAV audio file and the model will predict whether
    the speech is REAL or AI-GENERATED.
    """
)

uploaded_file = st.file_uploader(
    "Upload Audio File",
    type=["wav"]
)

if uploaded_file is not None:

    # Save uploaded file temporarily
    temp_path = "temp.wav"

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.audio(temp_path)

    try:
        result = predict_audio(temp_path)

        st.subheader("Prediction Result")

        if result == "REAL":
            st.success("✅ REAL AUDIO")
        else:
            st.error("🚨 FAKE AUDIO")

    except Exception as e:
        st.error(f"Error: {e}")
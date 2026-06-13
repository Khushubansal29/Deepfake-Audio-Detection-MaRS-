import streamlit as st
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(ROOT, "src"))

from predict import predict_audio

st.set_page_config(
    page_title="Deepfake Audio Detection",
    page_icon="🎙️",
    layout="centered"
)

# Sidebar
st.sidebar.title("About")

st.sidebar.write("""
### Model Information

**Algorithm:** Random Forest

**Audio Features Used:**
- MFCC (13 coefficients)
- Zero Crossing Rate
- Spectral Centroid
- RMS Energy

**Test Accuracy:** 93%
""")

# Main Page
st.title("🎙️ Deepfake Audio Detection")

st.metric("Model Accuracy", "93%")

st.info(
    """
    Upload a WAV audio file and the model will analyze
    speech characteristics to determine whether the audio
    is human-generated or AI-generated.
    """
)

uploaded_file = st.file_uploader(
    "Upload Audio File",
    type=["wav"]
)

if uploaded_file is not None:

    temp_path = "temp.wav"

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.audio(temp_path)

    try:

        result, confidence = predict_audio(temp_path)

        st.subheader("Prediction Result")

        if result == "REAL":
            st.success("✅ REAL AUDIO")
        else:
            st.error("🚨 AI GENERATED AUDIO")

        st.progress(float(confidence))

        st.metric(
            "Confidence Score",
            f"{confidence * 100:.2f}%"
        )

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")

st.caption(
    "Built by Khushboo | IIT Roorkee | Deepfake Audio Detection System"
)
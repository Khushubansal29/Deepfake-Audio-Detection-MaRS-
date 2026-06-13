import os
import joblib
from feature_extraction import extract_features

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "random_forest_model.pkl"
)

model = joblib.load(MODEL_PATH)

def predict_audio(file_path):

    features = extract_features(file_path)

    prediction = model.predict([features])[0]
    confidence = max(model.predict_proba([features])[0])

    if prediction == 0:
        return "FAKE", confidence
    else:
        return "REAL", confidence
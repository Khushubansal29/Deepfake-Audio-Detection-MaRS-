import joblib
from src.feature_extraction import extract_features

model = joblib.load("../model/random_forest_model.pkl")

def predict_audio(file_path):
    features = extract_features(file_path)

    prediction = model.predict([features])

    return prediction[0]
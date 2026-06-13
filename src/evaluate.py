import pandas as pd
import joblib

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

data = pd.read_csv(
    "../dataset/for-2sec/for-2seconds/features/audio_features.csv"
)

X = data.drop("label", axis=1)
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = joblib.load(
    "../model/random_forest_model.pkl"
)

predictions = model.predict(X_test)

print(classification_report(y_test, predictions))
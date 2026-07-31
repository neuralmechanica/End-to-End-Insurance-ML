import pandas as pd
import pickle
with open('Model/model.pkl', 'rb') as f:
    model = pickle.load(f)

class_labels = model.classes_.tolist()
def predict_output(input_df: dict):
    input_df = pd.DataFrame([input_df])
    predicted_class = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]
    confidence = f"{max(probabilities)*100:.2f}%"

    class_proba = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return{
        "prediction category": predicted_class,
        "confidence": confidence,
        "class probalities": class_proba
    }

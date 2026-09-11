import json
import numpy as np
from PIL import Image
import tensorflow as tf

# ---- LOAD MODEL ONCE ----
MODEL_PATH = "models/plant_disease_model.h5"
CLASS_PATH = "models/class_names.json"

model = tf.keras.models.load_model(MODEL_PATH)

with open(CLASS_PATH, "r") as f:
    class_names = json.load(f)

# ---- IMAGE PREPROCESS ----
IMG_SIZE = (224, 224)  # match your training

def preprocess_image(file):
    img = Image.open(file).convert("RGB")
    img = img.resize(IMG_SIZE)
    arr = np.array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)
    return arr

# ---- PREDICT ----
def predict_image(file):
    try:
        img = preprocess_image(file)
        preds = model.predict(img)

        idx = int(np.argmax(preds))
        confidence = float(np.max(preds) * 100)

        label = class_names[idx]

        # simple status rule
        if "healthy" in label.lower():
            status = "Healthy"
            recommendation = "Crop is healthy. No action needed."
        else:
            status = "Disease Detected"
            recommendation = "Apply suitable fungicide and monitor plant."

        return {
            "class": label,
            "confidence": round(confidence, 2),
            "status": status,
            "recommendation": recommendation
        }

    except Exception as e:
        return {"error": str(e)}
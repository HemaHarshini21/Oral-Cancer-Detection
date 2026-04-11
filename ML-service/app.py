from flask import Flask, request, jsonify
import numpy as np
import cv2
from PIL import Image
import io
import base64
from tensorflow.keras.models import load_model
from utils import generate_gradcam

app = Flask(__name__)

# Load model once
model = load_model("model/model.h5")

# Preprocess
def preprocess(image):
    image = cv2.resize(image, (224,224))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/predict', methods=['POST'])
def predict():

    try:
        file = request.files['file']

        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        image = np.array(image)

        # ✅ NOW defined here
        processed = preprocess(image)

        # ✅ Prediction inside function
        pred = model.predict(processed)[0][0]

        if pred > 0.5:
            label = "Normal"
            confidence = float(pred)
        else:
            label = "Cancer"
            confidence = float(1 - pred)

        # ✅ Grad-CAM
        heatmap = generate_gradcam(model, processed)

        heatmap = cv2.resize(heatmap, (224, 224))

        # 🔥 Focus only strong regions
        threshold = 0.6
        heatmap = np.where(heatmap > threshold, heatmap, 0)

        heatmap = np.uint8(255 * heatmap)
        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

        original = cv2.resize(image, (224, 224))

        overlay = cv2.addWeighted(original, 0.7, heatmap, 0.3, 0)

        _, buffer = cv2.imencode('.jpg', overlay)
        heatmap_base64 = base64.b64encode(buffer).decode('utf-8')

        return jsonify({
            "label": label,
            "confidence": confidence,
            "heatmap": heatmap_base64
        })

    except Exception as e:
        print(e)
        return jsonify({"error": "Prediction failed"}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
import json
from urllib import response
from fastapi import FastAPI, UploadFile, File
import uvicorn
import requests
import absl.logging
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import cv2

# Ignoring all unnecessary warnings.
absl.logging.set_verbosity(absl.logging.ERROR)
tf.get_logger().setLevel("ERROR")

# Instantiate fastapi server
app = FastAPI()

endpoint = "http://localhost:8501/v1/models/brain_tumour:predict"

# Constants
# MODEL = tf.keras.models.load_model(r"C:/Users/ifunanyaScript/Everything/BrainTumour_DiagnosisApp/saved_models/2")
LABELS = ['no_tumour', 'tumour']


# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive!!!"

def bytes_to_image(bytes) -> np.ndarray:
    image = np.array(Image.open(BytesIO(bytes)))
    return image

@app.post("/classify")
async def clasify(file: UploadFile = File(...)):
    image = bytes_to_image(await file.read())
    image = cv2.resize(image, (224, 224))

    # Create a batch.
    image_batch = np.expand_dims(image, 0)

    json_data = {
        "instances": image_batch.tolist()
    }

    response = requests.post(endpoint, json=json_data)
    prediction = response.json()["predictions"][0]

    predicted_label = LABELS[np.argmax(prediction)]
    confidence = np.round(np.max(prediction), 2)

    return {
        "label": predicted_label,
        "confidence": confidence
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
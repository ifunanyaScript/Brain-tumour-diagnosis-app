# Import all necessary packages
import json
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

# Instantiate fastapi server.
app = FastAPI()

LABELS = ['no_tumour', 'tumour']

# This is the tf_serving link, We'll call the predict function of the model through this link. 
endpoint = "http://localhost:8501/v1/models/brain_tumour:predict"


# @app.get("/awake")
# async def awake():
#     return "I am awake!!!"


def bytes_to_image(bytes) -> np.ndarray:
    image = np.array(Image.open(BytesIO(bytes)))
    return image

@app.post("/classify")
async def clasify(file: UploadFile = File(...)):
    # file.read returns a byte array which is converted to an image
    image = bytes_to_image(await file.read())
    # Resize the image because the model expects (224, 224)
    image = cv2.resize(image, (224, 224))

    # Create a batch.
    image_batch = np.expand_dims(image, 0)

    # Convert image to tf_serving data format.
    image_data = {
        "instances": image_batch.tolist()
    }

    # tf_serving response.
    response = requests.post(endpoint, json=image_data)


    prediction = response.json()["predictions"][0]

    predicted_label = LABELS[np.argmax(prediction)]
    confidence = str(np.round(100 * np.max(prediction), 2)) + "%"

    return {
        "label": predicted_label,
        "confidence": confidence
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)

# ifunanyaScript
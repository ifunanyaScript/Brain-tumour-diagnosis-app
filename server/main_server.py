# Import necessary packages.
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
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

# Define links that CORS policy should allow.
origins = [
    "http://localhost",
    "http://localhost:3000"
]

# Add middlewares to the fastapi instance.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Constants
MODEL = tf.keras.models.load_model(r"../saved_models/2")

# Note: This should correspond with the one in the notebooks. 
LABELS = ['No Tumour', 'Tumour']


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

    prediction = MODEL.predict(image_batch)
    predicted_label = LABELS[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])
    return {
        "label": predicted_label,
        "confidence": float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)

# ifunanyaScript
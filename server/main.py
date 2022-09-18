# Import necessary packages.
from fastapi import FastAPI, UploadFile, File
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

# Constants
MODEL = tf.keras.models.load_model(r"C:/Users/ifunanyaScript/Everything/BrainTumour_DiagnosisApp/saved_models/2")
LABELS = ['no_tumour', 'tumour']


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
    confidence = round(np.max(prediction[0] * 100), 2)
    return {
        "label": predicted_label,
        "confidence": float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)

# ifunanyaScript
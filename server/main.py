from fastapi import FastAPI, UploadFile, File
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

# Instantiate fastapi server
app = FastAPI()

# Constants
MODEL = tf.keras.models.load_model(r"../saved_models/multiclass_model")

# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive!!!"

def bytes_to_image(bytes) -> np.ndarray:
    image = np.array(Image.open(BytesIO(bytes)))
    return image

@app.post("/classify")
async def clasify(file: UploadFile = File(...)):
    image = bytes_to_image(await file.read())
    return

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
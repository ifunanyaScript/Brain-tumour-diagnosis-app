from fastapi import FastAPI, UploadFile, File
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
# import tensorflow as tf

# Instantiate fastapi server
app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello, I am alive!!!"

@app.post("/classify")
async def classify(
    file: UploadFile = File(...)
):
    bytes = await file.read()
    return

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=5000)
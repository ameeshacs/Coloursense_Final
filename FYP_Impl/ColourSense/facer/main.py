import json
import fastapi
import functions as f
import cv2
from PIL import Image
from collections import Counter
import numpy as np
import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile
import base64
import skin_model as m
import requests
from pathlib import Path
import shutil
            

app = FastAPI()

origins = [
    "*"  # Allow requests from all origins
]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/save-profile-picture")
async def save_profile_picture(image: UploadFile = File(...)):
    try:
        contents = await image.read()
        with open("saved.jpg", "wb") as f:
            f.write(contents)
        return JSONResponse(content={"message": "Profile picture saved successfully"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": "Failed to save profile picture", "error": str(e)}, status_code=500)

# Define the root endpoint
@app.post("/image")
async def image():

    try:
        # decoded_image = base64.b64decode(image_data.split(",")[1])

        # with open("saved.jpg","wb") as fi:
        #     fi.write(decoded_image)
      
        f.save_skin_mask("saved.jpg")
   
        ans = m.get_season("temp.jpg")

   
        if ans == 3:
            ans += 1
        elif ans == 0:
            ans = 3

        # Create a response dictionary including the analysis result
        response_data = {'message': 'complete', 'result': ans}

        # Return the response with the analysis result
        return JSONResponse(content=response_data)
        # return JSONResponse(content={"message": "complete"})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="fail")
# def save_uploaded_image(file: UploadFile):
#     # Define the directory to save uploaded images
#     upload_dir = "images"
#     os.makedirs(upload_dir, exist_ok=True)  # Ensure the directory exists
#     file_path = os.path.join(upload_dir, file.filename)
#     with open(file_path, "wb") as buffer:
#         buffer.write(file.file.read())
#     return file_path

# @app.post("/image")
# async def image(file: UploadFile = File(...)):
#     try:
#         # Save the uploaded image
#         image_path = save_uploaded_image(file)
        
#         # Process the image
#         f.save_skin_mask(image_path)
#         ans = m.get_season("temp.jpg")
        
#         # Clean up temporary files
#         os.remove("temp.jpg")
#         os.remove(image_path)
        
#         # Determine the result
#         if ans == 3:
#             ans += 1
#         elif ans == 0:
#             ans = 3
        
#         # Prepare the result
#         test = {'result': ans}
#         encoded_data = base64.b64encode(str(test).encode('utf-8')).decode('utf-8')
        
#         # Send the result to another endpoint
#         response = requests.post('http://localhost:8000/output', json={'encodedData': encoded_data})
#         print(response.text) 
#         return JSONResponse(content={"message": "complete"})
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="fail")

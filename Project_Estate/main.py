from flask import Flask, request, Response, jsonify
import pickle
import numpy as np
import uvicorn
import json
from typing import List
import pandas as pd
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from salling_price_pred import prediction

app = FastAPI()

templates = Jinja2Templates(directory='templates')

class Item(BaseModel):
    status: str
    propertyType: str
    baths: float
    fireplace: int
    city: str
    sqft: float
    beds: float
    state: str
    stories: str
    PrivatePool: int
    Heating: str
    Cooling: int
    Parking: str
    Age: float
    Repaired: int
    
class Items(BaseModel):
    objects: List[Item]

@app.get("/")
async def root(request: Request, message='Samples'):
    return templates.TemplateResponse('index.html',
                                      {"request": request,
                                       "message": message})

@app.post("/predict_item")
def predict_item(item: Item) -> float:
    values = [v for k, v in dict(item).items()]
    columns = [k for k, v in dict(item).items()]
    sample = pd.DataFrame(data=values).T
    sample.columns = columns
    sample_pred = prediction(sample)
    return sample_pred[0]
  
@app.post("/one_object")
def upload_single(name: str = Form()):
    print(name)
    name = json.loads(name)
    y_pred = predict_item(name)

    return {'price': y_pred.round(2)}
        
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
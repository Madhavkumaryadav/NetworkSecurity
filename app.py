import os
import sys

import certifi 
ca = certifi.where()
import pymongo 

from dotenv import load_dotenv 
load_dotenv()

mongo_db_url = os.getenv("MONGODB_URL_KEY")
print(mongo_db_url)


from networksecurity.exception.exception import NetworkSecurityException 
from networksecurity.logger.logger1 import logging 

from networksecurity.pipeline.training_Pipeline import TrainingPipeline

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,File,UploadFile,Request 
from uvicorn import run as app_run 
from fastapi.responses import Response 
from starlette.responses import RedirectResponse 
import pandas as pd

from networksecurity.utils.main_utils.Utils import load_object

client = pymongo.MongoClient(mongo_db_url,tlsCAFile = ca)

from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME
from networksecurity.utils.ml_utils.model.estimator import NetworkModel


database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 
templates = Jinja2Templates(directory="./templates")


@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train_route():
    try:
        train_pipeline=TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Trainingis Successful")
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
   
@app.post("/predict", response_class=HTMLResponse)
async  def predict_route(request:Request , file:UploadFile = File(...)):
    try:
        df=pd.read_csv(file.file)
        #print(df)
        preprocesor=load_object("final_models/preprocessor.pkl")
        final_model=load_object("final_models/models.pkl")
        network_model = NetworkModel(preprocessor = preprocesor,model=final_model)
        print(df.iloc[0])
        y_pred=network_model.predict(df)
        print(y_pred)
        df['predicted_column']=y_pred 
        print(df['predicted_column'])
        
        #df['predicted_column'].replace(-1,0)
        # return df.to_json()
        df.to_csv("prediction_output/output.csv")
        table_html = df.to_html(classes='table table-striped')
        # Print(table )
        
        return templates.TemplateResponse("table.html",{"request":request ,"table":table_html})
        
    except   Exception as e:
        raise NetworkSecurityException(e,sys) 
    
if __name__=="__main__":
    app_run(app,host="localhost",port=8000)
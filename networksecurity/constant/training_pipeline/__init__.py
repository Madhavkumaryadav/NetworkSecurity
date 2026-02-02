import os
import sys
import numpy as np
import pandas as pd



'''
DEFINING COMMON CONSTANT VARIABLE FOR TRAINING PIPELINE 
'''
TARGET_COLUMN="CLASS_LABEL"
PEPELINE_NAME:str="NetworkSecurity"
ARTIFACT_DIR:str="artifacts"
FILE_NAME:str = "phisingData.csv"

TRAIN_FILE_NAME:str ='train.csv'
TEST_FILE_NAME:str ='test.csv'

SCHEMA_FILE_PATH =os.path.join('data_schema','schema.yaml')

SAVED_MODEL_DIR = os.path.join('saved_models')
MODEL_FILE_NAME = "model.pkl"


"""
Data Ingestion Related Constant Start with DATA_INGESTION VAR NAME 
"""

DATA_INGESTION_COLLECTION_NAME:str = "NetworkData"
DATA_INGESTION_DATABASE_NAME:str="collage"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str ="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2


'''
Data Validation related constant start with DATA_VALIDATION VAR NAMW 
'''

DATA_VALIDATION_DIR_NAME:str = 'data_validation'
DATA_VALIDATION_VALID_DIR:str = 'validated'
DATA_VALIDATION_INVALID_DIR:str = 'invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR:str = 'drift report '
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str ='report.yaml'
PREPROCESSING_OBJECT_FILE_NAME:str="Preprocessing.pkl"


"""
Data Transformation relateed constant start with DATA_TRANSFORMATION_VAR_NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

## Knn Imputer to replace nan values 
DATA_TRANSFORMATION_IMPUTER_PARAMS:dict ={
    
    "n_neighbors":3,
    "weights":"uniform",
}

DATA_TRANSFORMATION_TRAIN_FILE_PATH:str = "train.npy"
DATA_TRANSFORMATION_TEST_FILE_PATH:str = "test.npy"

"""
Model trainer related constant start with MODE TRAINER VAR NAME 
"""

MODEL_TRAINER_DIR_NAME:str ="model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str ="trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME:str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD:float = 0.05 
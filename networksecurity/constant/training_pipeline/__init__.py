import os
import sys
import numpy as np
import pandas as pd



'''
DEFINING COMMON CONSTANT VARIABLE FOR TRAINING PIPELINE 
'''
TRAGET_COLUMN="Result"
PEPELINE_NAME:str="NetworkSecurity"
ARTIFACT_DIR:str="artifacts"
FILE_NAME:str = "phisingData.csv"


TRAIN_FILE_NAME:str ='train.csv'
TEST_FILE_NAME:str ='test.csv'


"""
Data Ingestion Related Constant Start with DATA_INGESTION VAR NAME 
"""

DATA_INGESTION_COLLECTION_NAME:str = "NetworkData"
DATA_INGESTION_DATABASE_NAME:str="collage"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str ="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2

SCHEMA_FILE_PATH =os.path.join('data_schema','schema.yaml')

'''
Data Validation related constant start with DATA_VALIDATION VAR NAMW 
'''

DATA_VALIDATION_DIR_NAME:str = 'data_validation'
DATA_VALIDATION_VALID_DIR:str = 'validated'
DATA_VALIDATION_INVALID_DIR:str = 'invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR:str = 'drift report '
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str ='report.yaml'
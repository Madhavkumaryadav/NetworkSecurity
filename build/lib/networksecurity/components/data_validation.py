from networksecurity.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger1 import logging 
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from scipy.stats import ks_2samp
import pandas as pd
import os,sys
from networksecurity.utils.main_utils.Utils import read_yaml_file


class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config = data_validation_config 
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
            
        except Exception as e:
            raise NetworkSecurityException(e,sys) #type:ignore 
     
     
    @staticmethod 
    def read_data(file_path)->pd.DataFrame: #type:ignore 
        try:
            return pd.read_csv(file_path)
        except Exception as e :
            raise NetworkSecurityException(e,sys) # type:ignore 
           
    
    def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool: #type:ignore
        try:
            number_of_columns=len(self._schema_config)
            logging.info(f"Require number of columns {number_of_columns}")
            logging.info(f"Data Frame has columns : {len(dataframe.columns)}")
            
            if len(dataframe.columns) == number_of_columns:
                return True 
            return False 
        except Exception as e:
            raise NetworkSecurityException(e,sys) # type:ignore 
        
    def detect_dataset_drift(self,base_df,current_df,threshold=0.05)->bool : #type:ignore
        try:
            status=True
            report={}
            for column in base_df.columns:
                d1=base_df[column]
                d2=current_df[column]
                is_sample_dist=ks_2samp(d1,d2)
                '''
                Performs the two-sample Kolmogorov-Smirnov test for goodness of fit.

                This test compares the underlying continuous distributions F(x) and G(x) of two 
                independent samples. See Notes for a description of the available null and 
                alternative hypotheses.
                '''
                if threshold <= is_sample_dist.pvalue:
                    if_found=False 
                else:
                    is_found=True
                    status=False
                
                
                    
        except Exception as e:
            raise NetworkSecurityException(e,sys) #type:ignore
        
    def initiate_data_validation(self)->DataValidationArtifact: #type:ignore
        try:
            train_file_path=self.data_ingestion_artifact.trained_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path
            
            ## Read the data from train and test 
            
            train_dataframe=DataValidation.read_data(train_file_path)
            test_dataframe=DataValidation.read_data(test_file_path)
            
            ##Validate number of columns 
            
            status =self.validate_number_of_columns(dataframe=train_dataframe)
            if not status :
                error_message=f"{error_message} Train dataframe does not contain all columns . \n" # type:ignore 
            
            status=self.validate_number_of_columns(dataframe=test_dataframe)
            if not status :
                error_message = f"{error_message} Test dataframe does not contain all columns. \n"
                
            ## Lets check datadrift 
            
                
        except Exception as e:
            raise NetworkSecurityException(e,sys) #type:ignore 
        


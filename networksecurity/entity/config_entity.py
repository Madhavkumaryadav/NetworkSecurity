from datetime import datetime 
import os

from networksecurity.constant import training_pipeline

print(training_pipeline.PEPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%y_%H_%M_%S")
        self.pipeline_name=training_pipeline.PEPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.timestamp: str=timestamp 
        

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME
        ) # type: ignore
        self.feature_store_file_path:str=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,training_pipeline.FILE_NAME
        ) # type: ignore
        self.training_file_path:str=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
        ) # type: ignore
        self.testing_file_path:str=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME
        ) # type: ignore
        
        self.train_test_split_ratio:float=training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name:str=training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name:str = training_pipeline.DATA_INGESTION_DATABASE_NAME
        
        
# class DataValidationConfig:
#     def __init__(self,training_pipeline_config:TrainingPipelineConfig):
#         self.data_validation_dir:str = os.path.join(training_pipeline_config.artifact_dir , training_pipeline.DATA_VALIDATION_DIR_NAME)
#         self.valid_data_dir:str =os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALID_DIR)
#         self.invalid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_DIR)
#         self.valid_train_file_path:str = os.path.join(self.valid_data_dir,training_pipeline.TRAIN_FILE_NAME)
#         self.valid_test_file_path:str = os.path.join(self.valid_data_dir,training_pipeline.TEST_FILE_NAME)
#         self.invalid_train_file_path:str = os.path.join(self.invalid_data_dir,training_pipeline.TRAIN_FILE_NAME)
#         self.invalid_test_file_path:str = os.path.join(self.invalid_data_dir,training_pipeline.TEST_FILE_NAME)
#         self.drift_report_file_path:str = os.path.join(
#             training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
#             training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
#         )


class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):

        self.data_validation_dir = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_VALIDATION_DIR_NAME
        )

        self.valid_data_dir = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_VALID_DIR
        )

        self.invalid_data_dir = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_INVALID_DIR
        )

        self.valid_train_file_path = os.path.join(
            self.valid_data_dir,
            training_pipeline.TRAIN_FILE_NAME
        )

        self.valid_test_file_path = os.path.join(
            self.valid_data_dir,
            training_pipeline.TEST_FILE_NAME
        )

        self.invalid_train_file_path = os.path.join(
            self.invalid_data_dir,
            training_pipeline.TRAIN_FILE_NAME
        )

        self.invalid_test_file_path = os.path.join(
            self.invalid_data_dir,
            training_pipeline.TEST_FILE_NAME
        )

        self.drift_report_file_path = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME
        )

        os.makedirs(self.valid_data_dir, exist_ok=True)
        os.makedirs(self.invalid_data_dir, exist_ok=True)
        os.makedirs(os.path.dirname(self.drift_report_file_path), exist_ok=True)
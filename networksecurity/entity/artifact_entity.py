from dataclasses import dataclass

@dataclass 
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 


@dataclass 
class DataValidationArtifact:
    validation_status:bool
    valid_train_file_path:str 
    valid_test_file_path:str
    invalid_train_file_path:str 
    invalid_test_file_path:str 
    drift_report_file_path:str 


@dataclass
class DataTransformationArtifact:
    transformed_objed_file_path:str 
    transformed_train_file_path:str 
    transformed_test_file_path: str 
    

@dataclass 
class ClassificationMetricsArtifact:
    f1_score:float 
    precision_score:float 
    recall_score: float 
    
@dataclass 
class MOdelTrainerArtifact:
    trained_model_file_path:str 
    train_metrics_artifact:ClassificationMetricsArtifact
    test_metrics_artifact:ClassificationMetricsArtifact

    
from networksecurity.entity.artifact_entity import ClassificationMetricsArtifact
from networksecurity.exception.exception import NetworkSecurityException
from sklearn.metrics import f1_score,precision_score,recall_score
import sys


def get_classification_score(y_true,y_pred)->ClassificationMetricsArtifact:
    try:
        
        model_f1_score = f1_score(y_true,y_pred,average='weighted',zero_division=0)
        model_recall_score=recall_score(y_true,y_pred,average='weighted',zero_division=0)
        model_precision_score=precision_score(y_true,y_pred,average='weighted',zero_division=0)
        
        classification_metric = ClassificationMetricsArtifact(f1_score=float(model_f1_score),
                                                              precision_score=float(model_precision_score),
                                                              recall_score=float(model_recall_score))
        return classification_metric 
    except Exception as e:
        raise NetworkSecurityException(e,sys)
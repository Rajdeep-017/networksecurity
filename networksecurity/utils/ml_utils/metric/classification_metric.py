from networksecurity.entity.artifact_entity import Classificationmetricsartifact
from networksecurity.exception.exception import Networksecurity
from sklearn.metrics import f1_score,precision_score,recall_score
import sys
def get_classifaction_score(y_true,y_pred)->Classificationmetricsartifact:
    try:
        model_f1_score=f1_score(y_true,y_pred)
        model_recall_score=recall_score(y_true,y_pred)
        model_precision_score=precision_score(y_true,y_pred)
        classifcation_metric=Classificationmetricsartifact(f1_score=model_f1_score,
                                                           precision_score=model_precision_score,
                                                           recall_score=model_recall_score)
        return classifcation_metric
    except Exception as e:
        raise Networksecurity(e,sys)
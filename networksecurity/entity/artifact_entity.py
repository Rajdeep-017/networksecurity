from dataclasses import dataclass
@dataclass
class Dataingestionartifact:
    trained_file_path:str
    test_file_path:str

@dataclass
class Datavalidationartifact:
    validation_status:bool
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path:str

@dataclass
class Datatransformationartifact:
    transformed_object_file_path: str
    transfromed_train_file_path: str
    transformed_test_file_path: str
    
@dataclass
class Classificationmetricsartifact:
    f1_score:float
    precision_score: float
    recall_score:float

@dataclass
class Modeltrainerartifact:
    trained_model_file_path : str
    train_metric_artifact:Classificationmetricsartifact
    test_metric_artifact:Classificationmetricsartifact

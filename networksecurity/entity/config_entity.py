from datetime import datetime
import os
from networksecurity.constant import train_pipeline
print(train_pipeline.PIPELINE_NAME)
print(train_pipeline.ARTIFACT_DIR)

class trainingpipelineconfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name=train_pipeline.PIPELINE_NAME
        self.artifact_name=train_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.timestamp:str=timestamp
        

class Dataingestionconfig:
    def __init__(self,train_pipeline_config:trainingpipelineconfig):
        self.data_ingestion_dir:str=os.path.join(
               train_pipeline_config.artifact_dir,train_pipeline.DATA_INGESTION_DIR_NAME    
        )
        self.feature_store_file_path:str=os.path.join(
               self.data_ingestion_dir,train_pipeline.DATA_INGESTION_FEATURE_STORE_NAME,train_pipeline.FILE_NAME
        )
        self.train_file_path:str=os.path.join(
                self.data_ingestion_dir,train_pipeline.DATA_INGESTION_DIR_NAME,train_pipeline.TRAIN_FILE_NAME
        )
        self.test_file_path:str=os.path.join(
                self.data_ingestion_dir,train_pipeline.DATA_INGESTION_DIR_NAME,train_pipeline.TEST_FILE_NAME
        )
        self.train_test_split_ratio: float=train_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name:str=train_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name:str=train_pipeline.DATA_INGESTION_DATABASE_NAME

class Datavalidationconfig:
    def __init__(self,train_pipeline_config:trainingpipelineconfig):
        self.data_validation_dir:str=os.path.join(
               train_pipeline_config.artifact_dir,train_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir:str=os.path.join(self.data_validation_dir,train_pipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir:str=os.path.join(self.data_validation_dir,train_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path:str=os.path.join(self.valid_data_dir,train_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path:str=os.path.join(self.valid_data_dir,train_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path:str=os.path.join(self.invalid_data_dir,train_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path:str=os.path.join(self.invalid_data_dir,train_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path=os.path.join(
            self.data_validation_dir,
            train_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            train_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
        )

class Datatransformationconfig:
    def __init__(self,train_pipeline_config:trainingpipelineconfig):
        self.data_transformation_dir:str=os.path.join(train_pipeline_config.artifact_dir,train_pipeline.DATA_TRANSFORMATION_DIR_NAME)
        self.transformed_train_file_path:str=os.path.join(self.data_transformation_dir,train_pipeline.DATA_TRANSFORMATION_DATA_DIR,train_pipeline.TRAIN_FILE_NAME.replace("csv","npy"),)
        self.transformed_test_file_path: str=os.path.join(self.data_transformation_dir,train_pipeline.DATA_TRANSFORMATION_DATA_DIR,train_pipeline.TEST_FILE_NAME.replace("csv","npy"),)
        self.transformed_object_file_path: str=os.path.join(self.data_transformation_dir,train_pipeline.DATA_TRANSFORMATION_DATA_DIR,train_pipeline.PREPROCESSING_OBJECT_FILE_NAME)

class Modeltrainerconfig:
    def __init__(self,train_pipeline_config:trainingpipelineconfig):
        self.model_trainer_dir: str=os.path.join(train_pipeline_config.artifact_dir,train_pipeline.MODEL_TRAINER_DIR_NAME)
        self.trained_model_file_path: str=os.path.join(self.model_trainer_dir,train_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR,train_pipeline.MODEL_FILE_NAME)
        self.excepted_accuracy:float=train_pipeline.MODEL_TRAINER_EXCEPTED_SCORE
        self.overfitting_underfitting_threshold=train_pipeline.MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD
        
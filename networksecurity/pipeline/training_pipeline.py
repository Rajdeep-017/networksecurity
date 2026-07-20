from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import Datavalidation
from networksecurity.components.data_transformation import Datatransformation
from networksecurity.components.model_trainer import Modeltrainer
from networksecurity.exception.exception import Networksecurity
from networksecurity.utils.ml_utils.model.estimator import Networkmodel
from networksecurity.logging.logger import logging
import os,sys
from networksecurity.cloud.s3_syncer import S3Sync
from networksecurity.constant.train_pipeline import TRAINING_BUCKET_NAME,SAVED_MODEL_DIR

from networksecurity.entity.config_entity import (
    trainingpipelineconfig,
    Dataingestionconfig,
    Datavalidationconfig,
    Datatransformationconfig,
    Modeltrainerconfig,
)
from networksecurity.entity.artifact_entity import(
    Dataingestionartifact,
    Datatransformationartifact,
    Datavalidationartifact,
    Modeltrainerartifact,
)
class Trainingpipeline:
    def __init__(self):
        self.training_pipeline_config=trainingpipelineconfig()
        self.s3_sync=S3Sync()
    
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config=Dataingestionconfig(train_pipeline_config=self.training_pipeline_config)
            logging.info("start the ingestion")
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info(f"data ingestion completed {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise Networksecurity(e,sys)
        
    def start_data_validation(self,data_ingestion_artifact:Dataingestionartifact):
        try:
            data_validation_config=Datavalidationconfig(train_pipeline_config=self.training_pipeline_config)
            data_validation=Datavalidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=data_validation_config)
            data_validation_artifact=data_validation.initiate_data_validation()
            logging.info(f"data validation completed")
            return data_validation_artifact
        except Exception as e:
            raise Networksecurity(e,sys)
    
    def start_data_transformation(self,data_validation_artifact:Datavalidationartifact):
        try:
            data_transformation_config=Datatransformationconfig(train_pipeline_config=self.training_pipeline_config)
            data_transformation=Datatransformation(data_validation_artifact=data_validation_artifact,data_transformation_config=data_transformation_config)
            data_transformation_artifact=data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise Networksecurity(e,sys)
    
    def start_model_trainer(self,data_transformation_artifact:Datatransformationartifact)->Modeltrainerartifact:
        try:
            self.model_trainer_config:Modeltrainerconfig=Modeltrainerconfig(
                train_pipeline_config=self.training_pipeline_config
            )
            model_trainer=Modeltrainer(
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_config=self.model_trainer_config,
            )
            model_trainer_artifact=model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except Exception as e:
            raise Networksecurity(e,sys)
    
    #local artifact is going to  s3 bucket
    def sync_arifact_dir_to_s3(self):
        try:
            aws_bucket_url=f"s3://{TRAINING_BUCKET_NAME}/artifact/{self.training_pipeline_config.timestamp}"
            self.s3_sync.sync_folder_to_s3(folder=self.training_pipeline_config.artifact_dir,aws_bucket_url=aws_bucket_url)
        except Exception as e:
            raise Exception(e,sys)
    #local final model is going to S3 bucket

    def sync_saved_model_dir_to_s3(self):
        try:
            aws_bucket_url=f"s3://{TRAINING_BUCKET_NAME}/artifact/{self.training_pipeline_config.timestamp}"
            self.s3_sync.sync_folder_to_s3(folder=self.training_pipeline_config.artifact_dir,aws_bucket_url=aws_bucket_url)
        except Exception as e:
            raise Networksecurity(e,sys)

    
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact=self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            self.sync_arifact_dir_to_s3()
            self.sync_saved_model_dir_to_s3()
            return model_trainer_artifact
        except Exception as e:
            raise Networksecurity(e,sys)
    


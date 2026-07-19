from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import Datavalidation
from networksecurity.components.data_transformation import Datatransformation
from networksecurity.components.model_trainer import Modeltrainer
from networksecurity.exception.exception import Networksecurity
from networksecurity.utils.ml_utils.model.estimator import Networkmodel
from networksecurity.logging.logger import logging
import os,sys

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
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact=self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            return model_trainer_artifact
        except Exception as e:
            raise Networksecurity(e,sys)
    


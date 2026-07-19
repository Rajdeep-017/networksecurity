from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import Datavalidation
from networksecurity.components.data_transformation import Datatransformation
from networksecurity.components.model_trainer import Modeltrainer
from networksecurity.exception.exception import Networksecurity
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import Dataingestionconfig,Datavalidationconfig,Datatransformationconfig,Modeltrainerconfig
from networksecurity.entity.config_entity import trainingpipelineconfig
import sys
if __name__=="__main__":
    try:
        train_pipeline_config=trainingpipelineconfig()
        data_ingestion_config = Dataingestionconfig(train_pipeline_config)

        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        data_validation_config=Datavalidationconfig(train_pipeline_config)
        data_validation=Datavalidation(dataingestionartifact,data_validation_config)
        data_validation_artifact=data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("data transformation config")
        data_transformation_config=Datatransformationconfig(train_pipeline_config)
        data_transformation=Datatransformation(data_validation_config,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data validation complete")

        logging.info("model traininig started")
        model_trainer_config=Modeltrainerconfig(train_pipeline_config)
        model_trainer=Modeltrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info("model artifact created")

    except Exception as e:
        raise Networksecurity(e,sys)
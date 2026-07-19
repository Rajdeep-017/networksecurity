from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import Datavalidation
from networksecurity.exception.exception import Networksecurity
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import Dataingestionconfig,Datavalidationconfig
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
        logging.info("data validation complete")
    except Exception as e:
        raise Networksecurity(e,sys)
from networksecurity.exception.exception import Networksecurity
from networksecurity.logging.logger import logging
##configuraation of the data ingestion config
from networksecurity.entity.config_entity import Dataingestionconfig
from networksecurity.entity.artifact_entity import Dataingestionartifact


import os
import sys
import numpy as np
import pymongo
import pandas as pd
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self,data_ingestion_config:Dataingestionconfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise Networksecurity(e,sys)
    def export_collection_as_dataframe(self):
        try:
            database_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            collection=self.mongo_client[database_name][collection_name]
            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"])
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise Networksecurity
    def export_data_into_feature_stor(self,dataframe:pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            #creating folder
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise Networksecurity(e,sys)
    
    def split_data_as_train_test(self,dataframe: pd.DataFrame):
        try:
            train_set,test_set=train_test_split(
                dataframe,test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logging.info("performed train test split")
            logging.info("exited split_daata_train_test method of Data_ingestion")
            dir_path=os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info("exporting traintest file path")
            train_set.to_csv(
                self.data_ingestion_config.train_file_path,index=False,header=True
            )
            test_set.to_csv(
                self.data_ingestion_config.test_file_path,index=False,header=True
            )
        except Exception as e:
            raise Networksecurity(e,sys)


    def initiate_data_ingestion(self):
        """read data from mongo db"""
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_data_into_feature_stor(dataframe)
            self.split_data_as_train_test(dataframe)
            dataingestionartifact=Dataingestionartifact(trained_file_path=self.data_ingestion_config.train_file_path,
                                                        test_file_path=self.data_ingestion_config.test_file_path)
            return dataingestionartifact

        except Exception as e:
            raise Networksecurity(e,sys)

        

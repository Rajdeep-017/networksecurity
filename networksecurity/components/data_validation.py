from networksecurity.entity.artifact_entity import Dataingestionartifact,Datavalidationartifact
from networksecurity.entity.config_entity import Datavalidationconfig
from networksecurity.exception.exception import Networksecurity
from networksecurity.logging.logger import logging
from scipy.stats import ks_2samp
from networksecurity.constant.train_pipeline import SCHEMA_FILE_PATH
import pandas as pd
import os,sys
from networksecurity.utils.main_utils.utils import read_yaml_file,write_yaml_file
class Datavalidation:
    def __init__(self,data_ingestion_artifact:Dataingestionartifact,
        data_validation_config:Datavalidationconfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config=read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise Networksecurity(e,sys)
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise Networksecurity(e,sys)
    
    def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            number_of_col=len(self._schema_config)
            logging.info(f"required no of columns :{number_of_col}")
            logging.info(f"dataframse has columns: {len(dataframe.columns)}")
            if len(dataframe.columns)==number_of_col:
                return True
            return False
        except Exception as e:
            raise Networksecurity(e,sys)
    def detect_dataset_drift(self,base_df,curr_df,threshold=0.05)->bool:
        try:
            status =True
            report={}
            for col in base_df.columns:
                d1=base_df[col]
                d2=curr_df[col]
                is_sample_dist=ks_2samp(d1,d2)
                if threshold<=is_sample_dist.pvalue:
                    is_found=False
                else:
                    is_found=True
                    status=False
                report.update({col:{
                    "p_value":float(is_sample_dist.pvalue),
                    "drift_status":is_found
                }})
            drift_report_file_path=self.data_validation_config.drift_report_file_path
            dir_path=os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path,content=report)
        except Exception as e:
            raise Networksecurity(e,sys)

    def initiate_data_validation(self)->Datavalidationartifact:
        try:
            train_file_path=self.data_ingestion_artifact.trained_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path
            #read train test_path
            train_dataframe=Datavalidation.read_data(train_file_path)
            test_dataframe=Datavalidation.read_data(test_file_path)

            #validate number of columns
            status=self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_msg=f" train dataframe does not contain all col"
            status=self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_msg=f"{error_msg} test dataframe does not contain all col"

            #check data drift
            status=self.detect_dataset_drift(base_df=train_dataframe,curr_df=test_dataframe)
            dir_path=os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(dir_path,exist_ok=True)
            train_dataframe.to_csv(
                self.data_validation_config.valid_train_file_path,index=False,header=True
            )
            test_dataframe.to_csv(
                self.data_validation_config.valid_test_file_path,index=False,header=True
            )
            data_validation_artifact=Datavalidationartifact(
                validation_status=status,
                valid_train_file_path=self.data_ingestion_artifact.trained_file_path,
                valid_test_file_path=self.data_ingestion_artifact.test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path
            )
            return data_validation_artifact
        except Exception as e:
            raise Networksecurity(e,sys)

        

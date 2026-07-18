import os
import sys
import numpy as np
import pandas as pd
TARGET_COLUMNS="Result"
PIPELINE_NAME: str="networksecurity"
ARTIFACT_DIR: str="artifacts"
FILE_NAME: str="phishingData.csv"

TRAIN_FILE_NAME: str='train.csv'
TEST_FILE_NAME: str='test.csv'
SCHEMA_FILE_PATH=os.path.join('data_schema','schema.yaml')
"""
Data Ingestion related sonstant start Data_Ingestion VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str= "networkdata"
DATA_INGESTION_DATABASE_NAME: str="Rajdeep"
DATA_INGESTION_DIR_NAME: str='data_ingestion'
DATA_INGESTION_FEATURE_STORE_NAME:str='feature_store'
DATA_INGESTION_INGESTED_DIR: str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float=0.2

"""data validation related constant with DATA_VALIDATION"""

DATA_VALIDATION_DIR_NAME: str='data_validation'
DATA_VALIDATION_VALID_DIR: str='validated'
DATA_VALIDATION_INVALID_DIR: str='invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR: str='drift_report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str='report.yml'
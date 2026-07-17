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
"""
Data Ingestion related sonstant start Data_Ingestion VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str= "networkdata"
DATA_INGESTION_DATABASE_NAME: str="Rajdeep"
DATA_INGESTION_DIR_NAME: str='data_ingestion'
DATA_INGESTION_FEATURE_STORE_NAME:str='feature_store'
DATA_INGESTION_INGESTED_DIR: str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float=0.2
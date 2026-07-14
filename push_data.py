import os 
import sys
import json
from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi#valid request madde
ca=certifi.where() #So this line retrieves the part to the bundle of CA certificates provided by certify and store it in the variable CA.

#ca =certificate authority
"""
The certify is a Python package that provides a set of root certificates.

Okay.

It is commonly used by Python libraries.

That needs to probably make a secure HTTP connection. here mongodb"""

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import Networksecurity
from networksecurity.logging import logger
class Networkdataextract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise Networksecurity(e,sys)

    def cv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise Networksecurity(e,sys)

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            print(self.mongo_client.admin.command("ping"))
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise Networksecurity(e,sys)

if __name__=='__main__':
    FILE_PATH="network_data/phisingData.csv"
    DATABASE="Rajdeep"
    collection="networkdata"
    networkobj=Networkdataextract()
    records=networkobj.cv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,collection)
    print(no_of_records)




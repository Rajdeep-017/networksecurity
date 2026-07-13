
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Rajdeep:G4llR4V1GlWpU0C4@cluster0.ocetz93.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
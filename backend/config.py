import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# load local environments variables .env
load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

uri = f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@cluster0.odvnp.mongodb.net/?appName=Cluster0"

# Conect MongoDB
client = MongoClient(uri, server_api=ServerApi('1'))

# Conection test
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error connecting to MongoDB:", e)

# Export DB
db = client[DB_NAME]

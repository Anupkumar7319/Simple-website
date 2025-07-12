import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load .env variables (like MONGO_URI)
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "video_links_app")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

def get_db():
    return db

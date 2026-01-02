from pymongo import MongoClient
import os

# MongoDB connection string from environment variables
MONGO_URL = os.environ.get("MONGO_URL")

if not MONGO_URL:
    raise Exception("MONGO_URL environment variable not set")

client = MongoClient(MONGO_URL)

# Database name
db = client["webrtcsocket"]

# Users collection
users = db["users"]

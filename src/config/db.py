from pymongo import MongoClient
from config.env import MONGO_DB_URI

conn = MongoClient(MONGO_DB_URI)
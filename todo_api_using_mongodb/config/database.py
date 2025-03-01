import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

client = MongoClient(
    f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.jqge6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

db = client.todo_db

collection_name = db["todo_collection"]

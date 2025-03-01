from fastapi import FastAPI
from routes.route import router

app = FastAPI()

app.include_router(router=router)




### THE FOLLOWING CODE TESTS IF OUR APPLICATION IS SUCCESSFULLY CONNECTED 
### WITH MONGODB DATABASE. THE CODE CAN BE FOUND IN THE MONGODB WEBSITE 
### RIGHT AFTER YOU CREATE YOUR OWN CLUSTER.

# from dotenv import load_dotenv
# import os

# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# load_dotenv()
# USERNAME = os.environ["USERNAME"]
# PASSWORD = os.environ["PASSWORD"]

# uri = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.jqge6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi("1"))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command("ping")
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

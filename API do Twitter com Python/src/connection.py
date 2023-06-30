from pymongo import MongoClient


client = "mongodb+srv://flaysonemail:<password>@cluster0.fd6a6vt.mongodb.net/?retryWrites=true&w=majority"

db = client.MONGO_DIO_PROJECT

trends_collection = db.trends

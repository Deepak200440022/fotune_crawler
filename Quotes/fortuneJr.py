from pymongo import MongoClient
import random
from scrapy.utils.project import get_project_settings


settings = get_project_settings()
mongo_uri = settings.get("MONGO_URI", "mongodb://localhost:27017")
mongo_db = settings.get("MONGO_DATABASE", "quotes_db")


with MongoClient(mongo_uri) as client:
    db = client[mongo_db]
    collection = db["quotes"]

    count = collection.count_documents({})

    if(count):
        random_index = random.randint(0,count - 1)
        doc = collection.find().skip(random_index).limit(1).next()
        print(doc)

    else:
        print("Nothing there!")
        print("please run the following command in the terminal :  scrapy crawl quote  ")


import pymongo
client = pymongo.MongoClient()
db = client['starwars']

print(db)

from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)

client = MongoClient('mongodb://localhost:27017/')
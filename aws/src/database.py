import os
#import pymongo

# Fetch mongo env vars
usr = os.environ.get('MONGO_DB_USER')
pwd = os.environ.get('MONGO_DB_PASS')
mongo_db_name = os.environ.get('MONGO_DB_NAME')
mongo_collection_name = os.environ.get('MONGO_COLLECTION_NAME')
url = os.environ.get('MONGO_DB_URL')

# Connection String
#client = pymongo.MongoClient("mongodb+srv://" + usr + ":" + pwd + "@" + url + "/test?retryWrites=true&w=majority")
#db = client[mongo_db_name]
#collection = db[mongo_collection_name]

# Dummy MongoDB collection
class MongoDB_Collection:
    def find(self, query):
        return { "name": query["name"], "location": "C-53" }

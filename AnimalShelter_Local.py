from pymongo import MongoClient
import pandas as pd
from bson.objectid import ObjectId

class AnimalShelter:
    def __init__(self, host='localhost', port=27017, db='AAC', collection='animals'):
        try:
            self.client = MongoClient(host, port)
            self.database = self.client[db]
            self.collection = self.database[collection]
        except Exception as e:
            print(f"Connection error: {e}")


    def create(self, data):
        try:
            if data:
                self.collection.insert_one(data)
                return True
            else:
                raise ValueError("Nothing to insert")
        except Exception as e:
            print(f"Insert error: {e}")
            return False

    def read(self, query=None):
        try:
            if query is None:
                query = {}
            cursor = self.collection.find(query)
            return list(cursor)
        except Exception as e:
            print(f"Query error: {e}")
            return []

    def update(self, query, update_values):
        try:
            result = self.collection.update_many(query, {"$set": update_values})
            return result.modified_count
        except Exception as e:
            print(f"Update error: {e}")
            return 0

    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete error: {e}")
            return 0



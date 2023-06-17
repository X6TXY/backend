from datetime import datetime
from typing import List

from bson.objectid import ObjectId
from pymongo.database import Database


class ShanyraksRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_tweet(self, input: dict):
        payload = {
            "content": input["content"],
            "user_id": ObjectId(input["user_id"]),
            "created_at": datetime.utcnow(),
        }

        self.database["tweets"].insert_one(payload)

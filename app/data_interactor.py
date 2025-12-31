from bson import ObjectId
from pydantic import BaseModel
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from typing import Optional

class Contact(BaseModel):
    id:Optional[int]
    first_name:str
    last_name:str
    phone_number:str


    def get_dict(self):
        return {"id":self._id,"first name":self.first_name,
                "last name":self.last_name,"phone number":self.phone_number}


def get_database():
    try:
        client = MongoClient(
            "mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
        client.admin.command("ping")
        print("✓ Successfully connected to MongoDB!")
        my_db = client["contacts_db"]
        return my_db

    except ConnectionFailure as e:
        print(f"✗ Failed to connect to MongoDB: {e}")
        print("Make sure MongoDB is running on localhost:27017")
        return None


db = get_database()
contacts_collection = db["contacts"] if db is not None else None


def create_contact(document:Contact):
    result = contacts_collection.insert_one(Contact.get_dict(document))
    return f"Inserted ID: {result.inserted_id}"

def get_all_contacts():
    cursor = contacts_collection.find()
    result = []
    for doc in cursor:
        result.append(doc)
    return result

def update_contact(id,update:dict):
    contacts_collection.update_one({"_id": ObjectId(id)},{"$set": update})
    return True

def delete_contact(id):
    contacts_collection.delete_one({"_id": ObjectId(id)})
    return True


# create_contact(Contact(first_name="aaa",last_name="bbb",phone_number="000"))
# print(get_all_contacts())
# print(update_contact({"name": "John Doe"},{"age": 8880, "status": "updated"}))
# print(delete_contact('6953c40ebcf8f66b1cb209e1'))


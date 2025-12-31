from bson import ObjectId
from pydantic import BaseModel
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure



class Contact(BaseModel):
    first_name:str
    last_name:str
    phone_number:str


    def get_dict(self):
        return {"first_name":self.first_name,
                "last_name":self.last_name,"phone_number":self.phone_number}


def get_database():

    try:
        client = MongoClient("mongodb-service", 27017)
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
    exists = contacts_collection.count_documents(
        {"phone_number": document.phone_number}, limit=1) <= 0
    if exists:
        result = contacts_collection.insert_one(Contact.get_dict(document))
        return f"message : Contact created successfully , Inserted ID: {result.inserted_id} "
    else:
        raise TypeError("The number entered already exists")

def get_all_contacts():
    cursor = contacts_collection.find()
    result = []
    for doc in cursor:
        result.append({"id":str(doc["_id"]),"first name":doc["first_name"],
                       "last name":doc["last_name"],"phone number":doc["phone_number"]})
    return result

def update_contact(id,update:dict):
    exists = contacts_collection.count_documents({"_id": id}, limit=1) > 0
    if exists:
        contacts_collection.update_one({"_id": ObjectId(id)},{"$set": update})
        return True
    else:
        raise TypeError("ID number not found")

def delete_contact(id):
    exists = contacts_collection.count_documents({"_id": id}, limit=1) > 0
    if exists:
        contacts_collection.delete_one({"_id": ObjectId(id)})
        return True
    else:
        raise TypeError("ID number not found")


# create_contact(Contact(first_name="aaa",last_name="bbb",phone_number="111"))
print(get_all_contacts())
# print(update_contact("6954decd4d207e1ece4548f9",{"phone_number": "11111"}))
# print(delete_contact('6954dd926cf5597b972aba1f'))


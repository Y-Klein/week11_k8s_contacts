from fastapi import FastAPI
from app.data_interactor import *

db = get_database()
contacts_collection = db["contacts"] if db is not None else None
app = FastAPI()


@app.get("/contacts")
def get_all():
    try:
        get_all_contacts()
    except Exception as err:
        return f"Unexpected {err=}, {type(err)=}"

@app.post("/contacts")
def create(contact):
    try:
        create_contact(contact)
    except Exception as err:
        return f"Unexpected {err=}, {type(err)=}"

@app.put("/contacts/{id}")
def update(id,update):
    try:
        update_contact(id,update)
    except Exception as err:
        return f"Unexpected {err=}, {type(err)=}"

@app.delete("/contacts/{id}")
def delete(id):
    try:
        delete_contact(id)
    except Exception as err:
        return f"Unexpected {err=}, {type(err)=}"


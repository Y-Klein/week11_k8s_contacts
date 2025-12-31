from fastapi import FastAPI
from data_interactor import *


app = FastAPI()


@app.get("/contacts")
def get_all():
    try:
        return get_all_contacts()
    except Exception as err:
        return f"Unexpected {err=}, {type(err)=}"

@app.post("/contacts")
def create(contact:Contact):
    try:
        return create_contact(contact)
    except Exception as err:
        return f"Unexpected {err=}, {type(err)=}"

@app.put("/contacts/{id}")
def update(id,update:dict):
    try:
        return update_contact(id,update)
    except Exception as err:
        return f"Unexpected {err=}, {type(err)=}"

@app.delete("/contacts/{id}")
def delete(id):
    try:
        return delete_contact(id)
    except Exception as err:
        return f"Unexpected {err=}, {type(err)=}"


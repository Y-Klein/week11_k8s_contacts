from fastapi import FastAPI,HTTPException


app = FastAPI()


@app.get("/contacts")
def get_all():
    try:
        pass
    except:
        raise TypeError("Something went wrong")

@app.post("/contacts")
def create(contact):
    try:
        pass
    except:
        raise TypeError("Something went wrong")

@app.put("/contacts/{id}")
def update(my_id,change_place,new_value):
    try:
        pass
    except:
        raise TypeError("Something went wrong")

@app.delete("/contacts/{id}")
def delete(my_id):
    try:
        pass
    except:
        raise TypeError("Something went wrong")



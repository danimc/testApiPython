from fastapi import FastAPI
from model.usuario import User, user_db

app = FastAPI(title="Api Sencilla",
            description="Api sencilla con endpoints para test")


@app.get("/api/users/")
def get_all_users():
    return user_db


@app.post("/api/users/")
def new_user(user:User):
    user_db.setdefault(len(user_db)+1, user)
    return user_db.get(2)

@app.delete("/api/users/{id}")
def delete_user(id:int):
    user_db.pop(id)
    return "eliminado"

@app.put("/api/users/{id}")
def edit_user(id:int, fullname:str):
        
    return "eliminado"
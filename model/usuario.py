from pydantic import BaseModel

class User (BaseModel):
    fullnameS  : str
    username  : str
    email     : str



user_db = dict()

user_db.setdefault(1, {
        "fullname": "admin",
        "username": "danimc",
        "email"   : "daniel_k310a@hotmail.com"   
    })

from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload

# Entidad user 

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name="Brais", surname="Moure", url="https://moure.dev", age=35),
              User(name="Paco", surname="Dev", url="https://Paco.dev", age=34),
              User(name="Pepe", surname="pepito", url="https://Pepe.dev", age=33)]

    
@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35}
           , {"name": "Paco", "surname": "Dev", "url": "https://Paco.dev", "age": 34}
           , {"name": "Pepe", "surname": "pepito", "url": "https://Pepe.dev", "age": 33}]

@app.get("/users")
async def users():
    return users_list
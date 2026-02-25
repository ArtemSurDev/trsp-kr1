from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class User(BaseModel):
    name: str
    age: int

@app.get("/")
async def read_root():
    return {
        "example": {
            "name": "Суринов Артём",
            "age": 19
        }
    }
@app.post("/user")
async def create_user(user: User):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }
@app.get("/user")
async def get_user_info():
    return {
        "example": {
            "name": "Суринов Артём",
            "age": 19
        }
    }
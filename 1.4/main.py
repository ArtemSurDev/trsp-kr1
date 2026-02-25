from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User

app = FastAPI()
user = User(name="Артём Суринов", id=1)

@app.get("/")
async def read_root():
    return FileResponse("index.html")

@app.get("/users")
async def get_user():
    return user
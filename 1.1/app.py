from fastapi import FastAPI

application = FastAPI()

@application.get("/")
async def root():
    return {"message": "Авторелоад действительно работает"}
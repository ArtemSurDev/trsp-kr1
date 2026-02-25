from fastapi import FastAPI
from models import User, Feedback
app = FastAPI()
feedback_list = []
user = User(name="Артём Суринов", id=1)
@app.get("/")
async def read_root():
    return {"message": "Добро пожаловать в API отзывов"}
@app.get("/users")
async def get_user():
    return user
@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedback_list.append(feedback)
    return {
        "message": f"Feedback received. Thank you, {feedback.name}."
    }
@app.get("/feedback")
async def get_all_feedback():
    return {
        "total": len(feedback_list),
        "feedbacks": feedback_list
    }
@app.get("/debug")
async def debug():
    return {
        "feedback_count": len(feedback_list),
        "user": user
    }
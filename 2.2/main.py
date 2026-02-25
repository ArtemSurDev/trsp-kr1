from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
app = FastAPI()
feedbacks = []
BAD_WORDS = ["кринж", "рофл", "вайб"]

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Имя от 2 до 50 символов")
    message: str = Field(..., min_length=10, max_length=500, description="Сообщение от 10 до 500 символов")
    @validator('message')
    def check_bad_words(cls, v):
        message_lower = v.lower()
        for word in BAD_WORDS:
            if word in message_lower:
                raise ValueError(f'Использование недопустимых слов')

        return v
@app.get("/")
async def read_root():
    return {
        "message": "Отправьте POST запрос на /feedback с JSON данными",
        "example": {
            "name": "Артур",
            "message": "Это тяжело, но я справлюсь!"
        },
        "requirements": {
            "name": "от 2 до 50 символов",
            "message": "от 10 до 500 символов, без слов: кринж, рофл, вайб"
        }
    }
@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    }
@app.get("/feedback")
async def get_all_feedbacks():
    return {
        "total": len(feedbacks),
        "feedbacks": feedbacks
    }
@app.get("/feedback/{index}")
async def get_feedback_by_index(index: int):
    if index < 0 or index >= len(feedbacks):
        raise HTTPException(status_code=404, detail="Отзыв не найден")

    return feedbacks[index]
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Numbers(BaseModel):
    num1: int
    num2: int

@app.get("/")
async def read_root():
    return {
        "message": "Калькулятор. Отправьте POST запрос на /calculate с двумя числами",
        "example": {"num1": 5, "num2": 10}
    }

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}
@app.get("/calculate")

async def calculate_get(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}
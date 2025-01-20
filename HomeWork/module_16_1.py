"""
Задача начало пути
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home_page():
    return "Главная страница"


@app.get("/user/admin")
async def user_admin():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def user_id(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def user_info(username: str = "Илья", age: int = 24):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

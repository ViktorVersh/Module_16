"""
Имитация работы с БД
"""
from fastapi import FastAPI, Path  # из библиотеки fastapi импортируем класс FastAPI и метод Path
from typing import Annotated  # из библиотеки typing импортируем Annotated

app = FastAPI()  # создаем экземпляр класса FastAPI

users = {'1': 'Имя: Example, возраст:18'}  # Создаем словарь


@app.get("/user")
async def get_users():
    """
    функция создает GET запрос по маршруту '/user'
    :return: dict users
    """
    return users


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=3, max_length=15, description="Введите свое имя",
                                      example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Введите свой возраст", example=24)]) -> str:
    """
    Функция добавления данных
    :param username:
    :param age:
    :return: str
    """
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, Возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[
            int, Path(ge=0, le=100, description="Введите свой id", example=1)],
        username: Annotated[
            str, Path(min_length=3, max_length=15, description="Введите свое имя", example="UrbanProfi")],
        age: Annotated[int, Path(ge=18, le=120, description="Введите свой возраст", example=28)]) -> str:
    """
    Функция внесения изменений в данные
    :param user_id:
    :param username:
    :param age:
    :return: str
    """
    users[user_id] = f"Имя: {username}, Возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[
            str, Path(min_length=1, max_length=3, description="Введите свой id", example="2")]) -> str:
    """
    Функция удаления данных по id
    :param user_id:
    :return: str
    """
    users.pop(user_id)
    return f"User {user_id} has been deleted"

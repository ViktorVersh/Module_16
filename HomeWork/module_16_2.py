"""
Аннотация и валидация
"""
from typing import Annotated  # из библиотеки typing импортируем Annotated

from fastapi import FastAPI, Path  # из библиотеки fastapi импортируем класс FastAPI и метод Path

app = FastAPI()  # создаем экземпляр класса FastAPI


@app.get("/")
async def get_home_page():
    """
    Функция выводит главную страницу
    :return:
    """
    return "Главная страница"


@app.get("/user/admin")
async def get_user_admin():
    """
    Функция выводит страницу администратора
    :return:
    """
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def get_user_id(
        user_id: Annotated[
            int, Path(ge=1, le=100, description="Enter User ID", example="10")
        ]
):
    """
    Функция выводит страницу пользователя
    :param user_id:
    :return:
    """
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def get_user_info(
        username: Annotated[
            str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[
            int, Path(ge=18, le=120, description="Enter age", example="24")
        ]):
    """
    Функция выводит информацию о пользователе
    :param username:
    :param age:
    :return:
    """
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

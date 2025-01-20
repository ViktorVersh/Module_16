"""
Задача начало пути
"""
from fastapi import FastAPI  # Импортируем из библиотеки fastapi класс FastAPI

app = FastAPI() # Создаем экземпляр класса FastAPI


@app.get("/")
async def home_page():
    """
    Функция выводит главную страницу
    :return:
    """
    return "Главная страница"


@app.get("/user/admin")
async def user_admin():
    """
    Функция выводит страницу администратора
    :return:
    """
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def user_id(user_id: int):
    """
    Функция выводит страницу пользователя
    :param user_id:
    :return:
    """
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def user_info(username: str = "Илья", age: int = 24):
    """
    Функция выводит информацию о пользователе
    :param username:
    :param age:
    :return:
    """
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

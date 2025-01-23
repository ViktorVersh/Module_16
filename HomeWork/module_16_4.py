"""
Модель пользователя
"""
from fastapi import FastAPI, HTTPException  # из библиотеки fastapi импортируем класс FastAPI и HTTPException
from typing import List  # из библиотеки typing импортируем List
from pydantic import BaseModel

app = FastAPI()  # создаем экземпляр класса FastAPI
users = []  # Создаем пустой список


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/user")
async def get_users() -> List[User]:
    """
    функция возвращает GET запрос по маршруту '/user'
    :return: users
    """
    return users


@app.post("/user/{username}/{age}")
async def create_user(username, age):
    """
    Функция добавления данных
    :param username:
    :param age:
    :return:
    """
    user_id = len(users) + 1
    users.append(User(id=user_id, username=username, age=age))
    return User(id=user_id, username=username, age=age)


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    """
    Функция внесения изменений в данные
    :param user_id:
    :param username:
    :param age:
    :return:
    """
    for i in users:
        if i.id == user_id:
            i.username = username
            i.age = age
            return User(id=user_id, username=username, age=age)
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    """
    Функция удаления данных по id
    :param user_id:
    :return: str
    """
    for i, u in enumerate(users):
        if u.id == user_id:
            user_del = users[i]
            del users[i]
            return user_del
    raise HTTPException(status_code=404, detail="User was not found")

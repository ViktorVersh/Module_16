"""
Список пользователей в шаблоне
"""
from fastapi import FastAPI, HTTPException, Request, Path  # импортируем класс FastAPI, HTTPException и Request
from typing import List, Annotated  # из библиотеки typing импортируем List
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates


app = FastAPI()  # создаем экземпляр класса FastAPI

templates = Jinja2Templates(directory="templates")

users = []  # Создаем пустой список


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def get_home_page(request: Request) -> HTMLResponse:
    """
    Функция выводит главную страницу
    :return:
    """
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_users(request: Request, user_id: Annotated[int, Path(ge=1)]) -> HTMLResponse:
    """
    функция возвращает GET запрос по маршруту '/user'
    :return:
    """
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")


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

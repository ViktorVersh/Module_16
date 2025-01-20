from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def home_page():
    return "Главная страница"


@app.get("/id")
async def id_paginator(username: str = "Alex", age: int = 34) -> dict:
    return {"User": username, "Age": age}


@app.get("/user/{username}/{id}")
async def news(
        username: Annotated[str, Path(min_length=3, max_length=15,description="Введите свое имя", example="montes")],
        id: Annotated[int, Path(ge=0, le=100, description="Введите свой id", example=75)]
) -> dict:
    return {"message": f"Hello {username} {id}"}



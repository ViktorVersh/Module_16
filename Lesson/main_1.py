from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


@app.get("/user/A/B")
async def news() -> dict:
    return {"message": f"Hello Tester!"}


@app.get("/user/{first_name}/{last_name}")
async def news(first_name: str, last_name: str) -> dict:
    return {"message": f"Hello {first_name} {last_name}"}


@app.get("/id")
async def id_paginator(username: str = "Alex", age: int = 34) -> dict:
    return {"User": username, "Age": age}


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10) -> dict:
    items = [{"item_id": i} for i in range(skip, skip + limit)]
    return {"items": items}


@app.get("/items/new")
async def read_new_items() -> dict:
    return {"message": "This is a list of new items"}


@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    return {"item_id": item_id, "name": f"Item {item_id}"}

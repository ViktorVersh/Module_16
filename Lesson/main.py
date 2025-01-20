from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


@app.get("/main")
async def welcome() -> dict:
    return {"message": "Main page"}


@app.get("/items/{item_id")
async def read_item(item_id: int):
    return {"item_id": item_id}


class Item(BaseModel):
    name: str
    price: float


@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": "Item deleted", "item_id": item_id}

@app.post("/products/")
async def create_product():
    """
    Создает новый продукт в системе.
    - ** name**: название продукта
    - ** price**: цена продукта
    - ** quantity**: количество продукта
    """
    return

#  Get - адрес в строке ? переменная значения
#  Post - формы - оформить заказ в магазине
#  Put - обновить заказ
#  Delete - удалить заказ

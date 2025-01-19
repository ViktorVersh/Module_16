from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


@app.get("/main")
async def welcome() -> dict:
    return {"message": "Main page"}


#  Get - адрес в строке ? переменная значения
#  Post - формы - оформить заказ в магазине
#  Put - обновить заказ
#  Delete - удалить заказ

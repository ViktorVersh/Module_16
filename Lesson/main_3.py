from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

message_db = {'1': "First post in FastApi"}


@app.get("/")
async def get_all_message():
    return message_db


@app.get("/message/{message_id}")
async def get_message(message_id: str):
    return message_db[message_id]


@app.post("/message")
async def create_message(message: str) -> str:
    current_index = str(int(max(message_db, key=int)) + 1)
    message_db[current_index] = message
    return "Message created"


@app.put("/message/{message_id}")
async def update_message(message_id: str, message: str) -> str:
    message_db[message_id] = message
    return "Message updated."


@app.delete("/message/{message_id}")
async def delete_message(message_id: str) -> str:
    message_db.pop(message_id)
    return f"Message with {message_id} was deleted."


@app.delete("/")
async def delete_all_message() -> str:
    message_db.clear()
    return "All messages deleted."

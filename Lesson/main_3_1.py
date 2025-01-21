from fastapi import FastAPI, Path, HTTPException
from typing import Annotated


app = FastAPI()

message_db = [{'id': 1, 'message': "First post in FastApi"},
              {'id': 2, 'message': "Second post in FastApi"},
              {'id': 3, 'message': "Third post in FastApi"}]

@app.get("/")
async def get_all_message():
    return "Home page"


@app.get("/message_db")
async def get_message():
    return message_db

@app.get("/message/{message_id}")
async def get_message(message_id: int):
    for message in message_db:
        if message['id'] == message_id:
            return message
    raise HTTPException(status_code=404, detail="Message not found")

@app.post("/message")
async def create_message(description: str):
    curent_index = max(message["id"] for message in message_db) + 1 if message_db else 1
    new_message = {'id': curent_index, 'message': description}
    message_db.append(new_message)
    return new_message


@app.put("/message/{message_id}")
async def update_message(message_id: int, description: str):
    for message in message_db:
        if message['id'] == message_id:
            message['description'] = description
            return message
    raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/message/{message_id}")
async def delete_message(message_id: int) -> str:
    message_db.pop(message_id)
    return f"Message with {message_id} was deleted."

@app.delete("/")
async def delete_all_message() -> str:
    message_db.clear()
    return "All messages deleted."

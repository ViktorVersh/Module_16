from pydantic import BaseModel, Field
from typing import List
from fastapi import FastAPI, HTTPException

app = FastAPI()


class Task(BaseModel):  # Проверка и изменение задачи
    id: int
    description: str
    is_completed: bool


class TaskCreate(BaseModel):  # Создание задачи
    description: str = Field(..., min_length=5,
                             max_length=100,
                             description="Описание задачи")
    is_completed: bool = False


# Инициализируем список задач с явной типизацией
tasks: List[Task] = [
    Task(id=1, description="Пример задачи", is_completed=False),
    Task(id="2", description="Пример задачи", is_completed=False)
]


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    """
    Получение списка задач
    :return:
    """
    return tasks


@app.post("/tasks", response_model=Task)
async def create_task(task: TaskCreate):
    """
    Создание задачи
    :param task:
    :return:
    """
    new_id = max((t.id for t in tasks), default=0) + 1
    new_task = Task(id=new_id, description=task.description, is_completed=task.is_completed)
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskCreate):
    """
    Изменение задачи
    :param task_id:
    :param task:
    :return:
    """
    for t in tasks:
        if t.id == task_id:
            t.description = task.description
            t.is_completed = task.is_completed
            return t
    raise HTTPException(status_code=404, detail="Задача не найдена")


@app.delete("/tasks/{task_id}", response_model=dict)
async def delete_task(task_id: int):
    """
    Удаление задачи
    :param task_id:
    :return: dict
    """
    for i, t in enumerate(tasks):
        if t.id == task_id:
            del tasks[i]
            return {"detail": "Задача удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")

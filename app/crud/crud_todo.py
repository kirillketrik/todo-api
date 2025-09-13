
from typing import List

from app.models.todo import Todo
from app.models.user import User
from app.schemas.todo import TodoCreate, TodoUpdate


async def create_todo(todo: TodoCreate, user: User) -> Todo:
    return await Todo.create(**todo.model_dump(), author=user)


async def get_todos(user: User) -> List[Todo]:
    return await Todo.filter(author=user)


async def get_todo(todo_id: int, user: User) -> Todo:
    return await Todo.get_or_none(id=todo_id, author=user)


async def update_todo(todo: Todo, todo_in: TodoUpdate) -> Todo:
    todo.title = todo_in.title if todo_in.title is not None else todo.title
    todo.description = todo_in.description if todo_in.description is not None else todo.description
    todo.done = todo_in.done if todo_in.done is not None else todo.done
    await todo.save()
    return todo


async def delete_todo(todo: Todo):
    await todo.delete()

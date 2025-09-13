
from fastapi import APIRouter, Depends, HTTPException, status

from app.models.user import User
from app.schemas.todo import TodoCreate, TodoInDB, TodoUpdate
from app.crud.crud_todo import create_todo, get_todos, get_todo, update_todo, delete_todo
from app.auth import get_current_user

router = APIRouter()


@router.post("/todos", response_model=TodoInDB)
async def create_todo_endpoint(
    todo_in: TodoCreate, current_user: User = Depends(get_current_user)
):
    return await create_todo(todo=todo_in, user=current_user)


@router.get("/todos", response_model=list[TodoInDB])
async def read_todos_endpoint(current_user: User = Depends(get_current_user)):
    return await get_todos(user=current_user)


@router.get("/todos/{todo_id}", response_model=TodoInDB)
async def read_todo_endpoint(
    todo_id: int, current_user: User = Depends(get_current_user)
):
    todo = await get_todo(todo_id=todo_id, user=current_user)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo


@router.put("/todos/{todo_id}", response_model=TodoInDB)
async def update_todo_endpoint(
    todo_id: int,
    todo_in: TodoUpdate,
    current_user: User = Depends(get_current_user),
):
    todo = await get_todo(todo_id=todo_id, user=current_user)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return await update_todo(todo=todo, todo_in=todo_in)


@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo_endpoint(
    todo_id: int, current_user: User = Depends(get_current_user)
):
    todo = await get_todo(todo_id=todo_id, user=current_user)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await delete_todo(todo=todo)

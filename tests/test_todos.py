
import pytest
from httpx import AsyncClient

from app.schemas.user import UserCreate
from app.schemas.todo import TodoCreate, TodoUpdate


@pytest.mark.anyio
async def test_create_and_read_todos(client: AsyncClient):
    # Register and login to get a token
    user_in = UserCreate(username="testuser_todos", password="testpassword")
    await client.post("/register", json=user_in.model_dump())
    login_data = {"username": user_in.username, "password": user_in.password}
    response = await client.post("/login", data=login_data)
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create a new todo
    todo_in = TodoCreate(title="Test Todo", description="Test Description")
    response = await client.post("/todos", headers=headers, json=todo_in.model_dump())
    assert response.status_code == 200
    assert response.json()["title"] == todo_in.title
    todo_id = response.json()["id"]

    # Read all todos
    response = await client.get("/todos", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 1

    # Read a specific todo
    response = await client.get(f"/todos/{todo_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == todo_in.title


@pytest.mark.anyio
async def test_update_and_delete_todo(client: AsyncClient):
    # Register and login to get a token
    user_in = UserCreate(username="testuser_update_delete", password="testpassword")
    await client.post("/register", json=user_in.model_dump())
    login_data = {"username": user_in.username, "password": user_in.password}
    response = await client.post("/login", data=login_data)
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create a new todo
    todo_in = TodoCreate(title="Test Todo Update", description="Test Description")
    response = await client.post("/todos", headers=headers, json=todo_in.model_dump())
    todo_id = response.json()["id"]

    # Update the todo
    todo_update = TodoUpdate(title="Updated Todo")
    response = await client.put(f"/todos/{todo_id}", headers=headers, json=todo_update.model_dump())
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Todo"

    # Delete the todo
    response = await client.delete(f"/todos/{todo_id}", headers=headers)
    assert response.status_code == 204

    # Verify the todo is deleted
    response = await client.get(f"/todos/{todo_id}", headers=headers)
    assert response.status_code == 404

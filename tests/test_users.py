
import pytest
from httpx import AsyncClient

from app.schemas.user import UserCreate


@pytest.mark.anyio
async def test_read_users_me(client: AsyncClient):
    # Register and login to get a token
    user_in = UserCreate(username="testuser_me", password="testpassword")
    await client.post("/register", json=user_in.model_dump())
    login_data = {"username": user_in.username, "password": user_in.password}
    response = await client.post("/login", data=login_data)
    token = response.json()["access_token"]

    # Get the current user
    headers = {"Authorization": f"Bearer {token}"}
    response = await client.get("/users/me", headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == user_in.username


@pytest.mark.anyio
async def test_update_user_me(client: AsyncClient):
    # Register and login to get a token
    user_in = UserCreate(username="testuser_update", password="testpassword")
    await client.post("/register", json=user_in.model_dump())
    login_data = {"username": user_in.username, "password": user_in.password}
    response = await client.post("/login", data=login_data)
    token = response.json()["access_token"]

    # Update the current user
    headers = {"Authorization": f"Bearer {token}"}
    update_data = {"username": "new_username"}
    response = await client.put("/users/me", headers=headers, json=update_data)
    assert response.status_code == 200
    assert response.json()["username"] == "new_username"

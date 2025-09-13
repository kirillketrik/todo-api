
import pytest
from httpx import AsyncClient

from app.schemas.user import UserCreate


@pytest.mark.anyio
async def test_register_and_login(client: AsyncClient):
    # Register a new user
    user_in = UserCreate(username="testuser", password="testpassword")
    response = await client.post("/register", json=user_in.model_dump())
    assert response.status_code == 200
    assert response.json()["username"] == user_in.username

    # Login with the new user
    login_data = {"username": user_in.username, "password": user_in.password}
    response = await client.post("/login", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

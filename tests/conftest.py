
import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import FastAPI
from tortoise import Tortoise

from app.api.api import api_router
from app.core.config import Settings

class TestSettings(Settings):
    database_url: str = "sqlite://:memory:"

test_settings = TestSettings()



def create_test_app():
    app = FastAPI()
    app.include_router(api_router)
    return app


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session", autouse=True)
async def initialize_database():
    await Tortoise.init(
        db_url=test_settings.database_url,
        modules={"models": ["app.models.user", "app.models.todo"]}
    )
    await Tortoise.generate_schemas()
    yield
    await Tortoise.close_connections()


@pytest.fixture(scope="session")
async def client() -> AsyncClient:
    app = create_test_app()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

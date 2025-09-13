
from tortoise.contrib.fastapi import register_tortoise
from app.core.config import settings


async def init_db(app, settings=settings):
    register_tortoise(
        app,
        db_url=settings.database_url,
        modules={"models": ["app.models.user", "app.models.todo"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

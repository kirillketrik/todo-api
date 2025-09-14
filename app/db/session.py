from tortoise import Tortoise


async def init_db(settings):
    await Tortoise.init(
        db_url=settings.database_url,
        modules={"models": ["app.models"]},
    )
    await Tortoise.generate_schemas()

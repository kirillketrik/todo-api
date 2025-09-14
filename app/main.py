from fastapi import FastAPI

from app.api import api_router
from app.core.config import get_settings
from app.db.session import init_db

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_db(settings=get_settings())
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api_router)

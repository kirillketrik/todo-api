from fastapi import FastAPI

from app.api import api_router
from app.db.session import init_db

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db(app, settings=get_settings())
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)

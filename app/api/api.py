
from fastapi import APIRouter

from app.api.endpoints import login, todos, users

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, tags=["users"])
api_router.include_router(todos.router, tags=["todos"])

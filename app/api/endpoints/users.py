
from fastapi import APIRouter, Depends, HTTPException, status

from app.models.user import User
from app.schemas.user import UserCreate, UserInDB, UserUpdate
from app.crud.crud_user import create_user, get_user_by_username
from app.auth import get_current_user
from app.core.security import get_password_hash

router = APIRouter()


@router.post("/register", response_model=UserInDB)
async def register(user_in: UserCreate):
    user = await get_user_by_username(user_in.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    return await create_user(user=user_in)


@router.get("/users/me", response_model=UserInDB)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("/users/me", response_model=UserInDB)
async def update_user_me(
    user_in: UserUpdate, current_user: User = Depends(get_current_user)
):
    if user_in.username:
        existing_user = await get_user_by_username(user_in.username)
        if existing_user and existing_user.id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered",
            )
        current_user.username = user_in.username
    if user_in.password:
        current_user.password_hash = get_password_hash(user_in.password)
    await current_user.save()
    return current_user

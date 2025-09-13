
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash


async def create_user(user: UserCreate) -> User:
    hashed_password = get_password_hash(user.password)
    return await User.create(username=user.username, password_hash=hashed_password)


async def get_user_by_username(username: str) -> User:
    return await User.get_or_none(username=username)

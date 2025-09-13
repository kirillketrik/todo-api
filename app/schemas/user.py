
from pydantic import BaseModel, constr
from typing import Optional

class UserCreate(BaseModel):
    username: constr(pattern=r"^[a-zA-Z0-9_]+$")
    password: str

class UserInDB(BaseModel):
    id: int
    username: str

    model_config = {"from_attributes": True}

class UserUpdate(BaseModel):
    username: Optional[constr(pattern=r"^[a-zA-Z0-9_]+$")] = None
    password: Optional[str] = None

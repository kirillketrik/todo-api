
from pydantic import BaseModel
from typing import Optional

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None

class TodoInDB(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    done: bool

    model_config = {"from_attributes": True}

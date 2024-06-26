from pydantic import BaseModel
from typing import List

# schemas/item.py
# schemas/user.py
class ItemBase(BaseModel):
    title: str
    description: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    title: str | None = None
    description: str | None = None

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class User(UserBase):
    id: int    
    items: List[Item]

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    hashed_password: str

class UserUpdate(UserBase):
    email: str | None = None
    hashed_password: str | None = None # python 3.10부터 추가된 기능입니다.
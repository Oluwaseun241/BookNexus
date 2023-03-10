# Pydantic Imports
from pydantic import BaseModel

# Third party Imports
from decimal import Decimal
from typing import Optional

class BookBase(BaseModel):
    isbn: int 
    title: str
    description: str
    categories: str
    amount: Decimal
    pages: int
    authors: str


class Book(BookBase):
    book_id: Optional[str] = None
    class Config:
        orm_mode = True

    

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    description: str
    amount: Decimal

class UserBase(BaseModel):
    username: str
    email: str
    password: str
    is_staff: bool

class User(UserBase):
    user_id: Optional[str] = None
    class Config:
        orm_mode = True


class ShowUser(UserBase):
    pass
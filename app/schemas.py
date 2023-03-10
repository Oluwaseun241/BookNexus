# Pydantic Imports
from pydantic import BaseModel, EmailStr

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
    email: EmailStr
    password: str
    is_staff: bool

class User(UserBase):
    pass

class ShowUser(BaseModel):
    user_id: Optional[str] = None
    username: str
    email: EmailStr
    is_staff: bool
    
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class CartItem(BaseModel):
    book_id: str
    quantity: int
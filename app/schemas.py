# Pydantic Imports
from pydantic import BaseModel, EmailStr

# Third party Imports
# from decimal import Decimal
from typing import Optional

class BookBase(BaseModel):
    isbn: int 
    title: str
    description: str
    categories: str
    amount: float
    pages: int
    authors: str


class Book(BookBase):
    id: Optional[str] = None
    class Config:
        orm_mode = True

    

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    description: str
    amount: float

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_staff: bool

class User(UserBase):
    pass

class ShowUser(BaseModel):
    id: Optional[str] = None
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
    # id: str
    quantity: int


# class PaymentInfo(BaseModel):
#     card_number: str
#     expiration_date: str
#     cvv: str
#     total_amount: float
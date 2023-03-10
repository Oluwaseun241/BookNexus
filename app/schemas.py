# Pydantic Imports
from pydantic import BaseModel, constr

# Third party Imports
from decimal import Decimal
from typing import Optional

class Book(BaseModel):
    book_id: Optional[str] = None
    isbn: int 
    title: constr(max_length=4)
    description: str
    categories: str
    amount: Decimal
    pages: int
    authors: str

    class Config:
        orm_mode = True

    

class BookCreate(BaseModel):
    isbn: int
    title: str
    description: str
    categories: str
    amount: Decimal
    pages: int
    authors: str

class BookUpdate(BaseModel):
    description: str
    amount: Decimal
    pages: int
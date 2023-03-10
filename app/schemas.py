# Pydantic Imports
from pydantic import BaseModel

# Third party Imports
from decimal import Decimal
from typing import Optional

class Book(BaseModel):
    book_id: Optional[str] = None
    isbn: int 
    title: str
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
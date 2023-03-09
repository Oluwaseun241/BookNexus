# Pydantic Imports
from pydantic import BaseModel

# Third party Imports
from decimal import Decimal
from typing import Optional

class Book(BaseModel):
    book_id: Optional[str] = None
    ISBN: int
    title: str
    description: str
    category: str
    amount: Decimal
    pages: int
    author: str

    class Config:
        orm_mode = True

    

class BookCreate(BaseModel):
    ISBN: int
    title: str
    description: str
    category: str
    amount: Decimal
    pages: int
    author: str

class BookUpdate(BaseModel):
    description: str
    amount: Decimal
    pages: int
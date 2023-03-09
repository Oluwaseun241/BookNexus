# Pydantic Imports
from pydantic import BaseModel

# Third party Imports
from decimal import Decimal
from typing import Optional

class Book(BaseModel):
    book_id: Optional[str] = None
    title: str
    description: str
    amount: Decimal

    class Config:
        orm_mode = True

class BookCreate(Book):
    pass

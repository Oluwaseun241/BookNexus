# Pydantic Imports
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    description: str
    amount: str
# SqlAlchemy Imports
from sqlalchemy import Column, Numeric, Integer, String
from sqlalchemy.orm import relationship

# UUID Import
import uuid

# Own Imports
from .database import Base

class Book(Base):

    __tablename__ = 'books'

    book_id = Column(String(36), primary_key=True, index=True, default=str(uuid.uuid4()))
    isbn = Column(Integer, nullable=False, unique=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)
    categories = Column(String, nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    pages = Column(Integer, nullable=False)
    authors = Column(String, nullable=False)
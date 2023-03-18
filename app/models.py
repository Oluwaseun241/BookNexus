# SqlAlchemy Imports
from sqlalchemy import Column, Numeric, Integer, String, ForeignKey
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

class User(Base):

    __tablename__ = 'users'

    user_id = Column(String(36), primary_key=True, index=True, default=str(uuid.uuid4()))
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_staff = Column(String, default=False, nullable=False)

class Cart(Base):

    __tablename__ = 'carts'

    book_id = Column(String(36), ForeignKey("books.book_id"))
    quantity = Column(Integer, nullable=False)
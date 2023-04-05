# SqlAlchemy Imports
from sqlalchemy import Column, Numeric, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# UUID Import
import uuid

# Own Imports
from .database import Base

class Book(Base):

    __tablename__ = 'books'

    id = Column(String(36), primary_key=True, index=True, default=str(uuid.uuid4()))
    isbn = Column(Integer, nullable=False, unique=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)
    categories = Column(String, nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    pages = Column(Integer, nullable=False)
    authors = Column(String, nullable=False)


class User(Base):

    __tablename__ = 'users'

    id = Column(String(36), primary_key=True, index=True, default=str(uuid.uuid4()))
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_staff = Column(String, default=False, nullable=False)


class Cart(Base):

    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    book_id = Column(String, ForeignKey("books.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.id"))

class Order(Base):

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)
    cart = relationship("Cart")
    payment_card_number = Column(String, nullable=False)
    payment_expiration_date = Column(String, nullable=False)
    payment_cvv = Column(String, nullable=False)
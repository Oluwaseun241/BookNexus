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
    title = Column(String)
    description = Column(String)
    amount = Column(Numeric(4,2))
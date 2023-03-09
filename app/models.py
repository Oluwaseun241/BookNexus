# SqlAlchemy Imports
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# UUID Import
from uuid import UUID

# Own Imports
from .database import Base

class Book(Base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    amount = Column(Integer)
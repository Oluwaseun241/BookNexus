# SqlAlchemy Import
from sqlalchemy.orm import Session
import uuid
from decimal import Decimal

# Own Import
from . import models, schemas

def get_book(db: Session):
    return db.query(models.Book).all()

def create_book(db: Session, request: schemas.BookCreate):
    new_book = models.Book(
        book_id=str(uuid.uuid4()),
        title=request.title,
        description=request.description,
        amount=Decimal(request.amount)
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

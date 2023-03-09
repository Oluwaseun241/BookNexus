# SqlAlchemy Import
from sqlalchemy.orm import Session

# Own Import
from . import models, schemas

def get_book(db: Session):
    return db.query(models.Book).all()

def create_book(db: Session, book: schemas.Book):
    new_book = models.Book(title=book.title, description=book.description, amount=book.amount)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

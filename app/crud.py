from fastapi import HTTPException
# SqlAlchemy Import
from sqlalchemy.orm import Session
import uuid
from decimal import Decimal

# Own Import
from . import models, schemas

def get_book(db: Session):
    return db.query(models.Book).all()

def get_book_category(categories: str, db: Session):
    return db.query(models.Book).filter(models.Book.categories == categories).first()

def create_book(db: Session, request: schemas.BookCreate):
    new_book = models.Book(
        book_id=str(uuid.uuid4()),
        isbn=request.isbn,
        title=request.title,
        description=request.description,
        categories=request.categories,
        amount=Decimal(request.amount),
        pages=request.pages,
        authors=request.authors
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def update_book(title: str, db: Session, request: schemas.BookUpdate):
    book = db.query(models.Book).filter(models.Book.title == title).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Title incorrect")

    book.description=request.description
    book.amount=Decimal(request.amount)

    db.commit()
    db.refresh(book)
    return book

def delete_book(isbn, db: Session):
    book = db.query(models.Book).filter(models.Book.isbn == isbn).delete(synchronize_session=False)
    
    db.commit()
    return book
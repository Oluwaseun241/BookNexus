from fastapi import HTTPException
# SqlAlchemy Import
from sqlalchemy.orm import Session
import uuid
from decimal import Decimal

# Own Import
from . import models, schemas

def get_book(db: Session):
    return db.query(models.Book).all()

def get_book_category(category: str, db: Session):
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

def update_book(category: str, db: Session, request: schemas.BookUpdate):
    book = db.query(models.Book).filter(models.Book.category == category).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Category not found")

    book.description=request.description
    book.amount=Decimal(request.amount)
    book.pages=request.pages

    db.commit()
    db.refresh(book)
    return book

def delete_book(isbn, db: Session):
    book = db.query(models.Book).filter(models.Book.isbn == isbn).delete(synchronize_session=False)
    
    db.commit()
    return book
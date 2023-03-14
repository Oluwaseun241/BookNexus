# FastAPU Import
from fastapi import HTTPException, status
from typing import List
# SqlAlchemy Import
from sqlalchemy.orm import Session
from sqlalchemy import or_
import uuid
from decimal import Decimal

# Own Import
from . import models, schemas
from app.core.hash import Hash

def get_book(db: Session):
    return db.query(models.Book).all()

def get_book_category(categories: List[str], db: Session):
    return db.query(models.Book).filter(or_(*[models.Book.categories.contains(categories) for category in categories])).all()
    #return db.query(models.Book).filter(models.Book.categories == categories).all()

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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Title incorrect")

    book.description=request.description
    book.amount=Decimal(request.amount)
    db.commit()
    db.refresh(book)
    return book

def delete_book(isbn, db: Session):
    book = db.query(models.Book).filter(models.Book.isbn == isbn).delete(synchronize_session=False)
    db.commit()
    return book

def create_user(db: Session, request: schemas.User):
    user_with_username = db.query(models.User).filter(
        models.User.username == request.username).first()
    user_with_email = db.query(models.User).filter(
        models.User.email == request.email).first()

    if user_with_username or user_with_email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Username or email already used")
                            
    hashed_password = Hash.get_password_hash(request.password)
    new_user = models.User(
        user_id=str(uuid.uuid4()),
        username=request.username,
        email=request.email,
        password=hashed_password,
        is_staff=request.is_staff
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session):
    return db.query(models.User).all()

def delete_user(username: str, db: Session):
    user = db.query(models.User).filter(models.User.username == username).delete(synchronize_session=False)
    db.commit()
    return user
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
    # return db.query(models.Book).filter(models.Book.categories == categories).all()


def get_book_id(id: str, db: Session) -> schemas.Book:
    return db.query(models.Book).filter(models.Book.id == id).first()


def create_book(db: Session, request: schemas.BookCreate):
    new_book = models.Book(
        id=str(uuid.uuid4()),
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Title incorrect")

    book.description = request.description
    book.amount = Decimal(request.amount)
    db.commit()
    db.refresh(book)
    return book


def delete_book(isbn, db: Session):
    book = db.query(models.Book).filter(models.Book.isbn ==
                                        isbn).delete(synchronize_session=False)
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
        id=str(uuid.uuid4()),
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
    user = db.query(models.User).filter(models.User.username ==
                                        username).delete(synchronize_session=False)
    db.commit()
    return user


def add_cart(request: schemas.CartItem, db: Session):
    cart = db.query(models.Book).filter(
        models.Book.id == request.book_id).first()

    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Book_id not found")
    new_cart = models.Cart(
        book_id=request.book_id,
        quantity=request.quantity
    )
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart


def delete_cart(id: int, db: Session):
    cart = db.query(models.Cart).filter(models.Cart.id ==
                                        id).delete(synchronize_session=False)
    db.commit()
    return cart


def get_cart(db: Session):
    return db.query(models.Cart).all()


def create_order(request: schemas.Order, db: Session):
    # Retrieve the cart instance with the given cart_id
    cart = db.query(models.Cart).filter(models.Cart.id == request.cart_id).first()

    # If the cart doesn't exist, raise a 404 error
    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart ID is invalid")

    # Create a new order instance and assign the cart instance to it
    new_order = models.Order(cart=cart, payment_card_number=request.payment_card_number,
                             payment_expiration_date=request.payment_expiration_date, payment_cvv=request.payment_cvv)

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

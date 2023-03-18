from fastapi import HTTPException, Depends, APIRouter
from app import models, Oauth2, crud, schemas
from app.core import token
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.post("/cart")
def add_to_cart(title: str, request: schemas.CartItem, db: Session = Depends(get_db)):
    cart = crud.cart_book(title, db)
    return cart
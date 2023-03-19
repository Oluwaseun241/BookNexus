from fastapi import HTTPException, Depends, APIRouter
from app import models, Oauth2, crud, schemas
from app.core import token
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.post("/cart")
def add_to_cart(book_id: str, request: schemas.CartItem, db: Session = Depends(get_db)):
    return crud.add_cart(book_id,request=request, db=db)
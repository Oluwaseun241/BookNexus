# FastAPI imports
from fastapi import HTTPException, Depends, APIRouter, status
from sqlalchemy.orm import Session
from typing import List

# Own Imports
from app import models, Oauth2, crud, schemas
from app.core import token
from app.database import get_db

router = APIRouter(
    tags=["Carts"]
)

@router.get("/cart")
def get_cart(db: Session = Depends(get_db)):
    return crud.get_cart(db)

@router.post("/cart")
def add_to_cart(request: schemas.CartItem, db: Session = Depends(get_db)):
    return crud.add_cart(request, db)

@router.delete("/cart/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_cart(id: int, db: Session = Depends(get_db)):
    cart = crud.delete_cart(id, db)

    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart not found")
    return {"detail": f"Cart with id {id} is sucessfully deleted"}
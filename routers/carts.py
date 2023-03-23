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

@router.post("/cart/checkout")
async def checkout(cart: schemas.Cart, payment_info: schemas.Order):
    # calculate the total amount of the order
    total = 0
    for item in cart.items:
        book = await crud.get_book_id(item.book_id)
        total += schemas.book.amount * item.quantity

    # check if the total amount matches the payment information
    if total != float(payment_info.cart.total):
        return {"message": "Payment information does not match the total amount of the order."}

    # create the order and return a success message
    await crud.create_order(payment_info, total)
    return {"message": "Order successfully placed."}
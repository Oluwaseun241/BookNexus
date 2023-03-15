from fastapi import HTTPException, Depends, APIRouter
from app import models, Oauth2
from app.core import token
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/cart")
def add_to_cart():
    pass
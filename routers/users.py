# FastAPI Import
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Own imports
from app import crud, models, schemas, Oauth2
from app.database import get_db

router = APIRouter(
    tags=["Users"]
)

@router.post("/user", response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, request=request)

@router.get("/user", response_model=List[schemas.ShowUser], status_code=status.HTTP_200_OK)
def user(db: Session = Depends(get_db), current_user: models.User = Depends(Oauth2.get_current_user)):
    users = crud.get_user(db)
    return users

@router.delete("/user/{username}", status_code=status.HTTP_202_ACCEPTED)
def delete_user(username: str, db: Session = Depends(get_db), current_user: models.User = Depends(Oauth2.get_current_user)):
    user = crud.delete_user(username, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"detail": f"User with username {username} is sucessfully deleted"}
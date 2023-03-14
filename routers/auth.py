# FastAPI Import
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

# SqlAlchemy Import
from sqlalchemy.orm import Session

# Own imports
from app.database import get_db


router = APIRouter(
    tags=["Auth"]
)

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        #return False
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify_password(request.password, user.password):
        #return False
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    access_token = token.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
from fastapi import HTTPException, Depends
from app import models, Oauth2
from app.core import token
from sqlalchemy.orm import Session

def staff_only(db: Session):
    pr = db.query(models.User.is_staff).all()
    if pr:
        print("admin")
    print("false")
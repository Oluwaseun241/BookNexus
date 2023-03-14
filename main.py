# FastAPI Imports
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm

# Own Imports
from app import crud, models, schemas, Oauth2
from app.database import SessionLocal, engine
from app.core import token
from app.core.hash import Hash

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/book", response_model=List[schemas.Book], status_code=status.HTTP_200_OK)
def book(db: Session = Depends(get_db)):
    books = crud.get_book(db)
    return books

@app.get("/book/{category}", response_model=List[schemas.Book], status_code=status.HTTP_202_ACCEPTED)
def book(categories: str, db: Session = Depends(get_db)):
    book = crud.get_book_category(categories, db)
    if not book:
        raise HTTPException(status_code=404, detail="Category not found")
    return book

@app.post("/book", response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
def create_book(request: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, request=request)

@app.put("/book/{title}", response_model=schemas.Book, status_code=status.HTTP_202_ACCEPTED)
def update_book(title: str, request: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = crud.update_book(title, db, request=request)
    return book

@app.delete("/book/{isbn}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(isbn: str, db: Session = Depends(get_db), current_user: models.User = Depends(Oauth2.get_current_user)):
    book = crud.delete_book(isbn, db)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return {"detail": f"Book with isbn {isbn} is sucessfully deleted"}

@app.post("/user", response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, request=request)

@app.get("/user", response_model=List[schemas.ShowUser], status_code=status.HTTP_200_OK)
def user(db: Session = Depends(get_db), current_user: models.User = Depends(Oauth2.get_current_user)):
    users = crud.get_user(db)
    return users

@app.delete("/user/{username}", status_code=status.HTTP_202_ACCEPTED)
def delete_user(username: str, db: Session = Depends(get_db), current_user: models.User = Depends(Oauth2.get_current_user)):
    user = crud.delete_user(username, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"detail": f"User with username {username} is sucessfully deleted"}


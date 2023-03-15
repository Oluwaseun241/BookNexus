# FastAPI imports
from fastapi import APIRouter, status, Depends, HTTPException
from typing import List

# SqlAlchemy Import
from sqlalchemy.orm import Session

# Own imports
from app import crud, models, schemas, Oauth2
from app.database import get_db

router = APIRouter(
    tags=["Books"]
)


@router.get("/book", response_model=List[schemas.Book], status_code=status.HTTP_200_OK)
def book(db: Session = Depends(get_db)):
    books = crud.get_book(db)
    return books


@router.get("/book/{category}", response_model=List[schemas.Book], status_code=status.HTTP_202_ACCEPTED)
def book(categories: str, db: Session = Depends(get_db)):
    book = crud.get_book_category(categories, db)
    if not book:
        raise HTTPException(status_code=404, detail="Category not found")
    return book


@router.post("/book", response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
def create_book(request: schemas.BookCreate, db: Session = Depends(get_db), current_user: models.User = Depends(Oauth2.get_current_user)):
    return crud.create_book(db=db, request=request)


@router.put("/book/{title}", response_model=schemas.Book, status_code=status.HTTP_202_ACCEPTED)
def update_book(title: str, request: schemas.BookUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(Oauth2.get_current_user)):
    book = crud.update_book(title, db, request=request)
    return book


@router.delete("/book/{isbn}", status_code=status.HTTP_202_ACCEPTED)
def delete_book(isbn: str, db: Session = Depends(get_db), current_user: models.User = Depends(Oauth2.get_current_user)):
    book = crud.delete_book(isbn, db)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return {"detail": f"Book with isbn {isbn} is sucessfully deleted"}

# @router.get("/protected_route")
# async def protected_route(current_user: models.User = Depends(Oauth2.is_staff)):
#     return {"message": "You are authorized to access this route."}

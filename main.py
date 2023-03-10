# FastAPI Imports
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Own Imports
from app import crud, models, schemas
from app.database import SessionLocal, engine

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
async def book(db: Session = Depends(get_db)):
    books = crud.get_book(db)
    return books

@app.get("/book/{category}", response_model=schemas.Book, status_code=status.HTTP_302_FOUND)
async def book(category: str, db: Session = Depends(get_db)):
    book = crud.get_book_category(category, db)
    if not book:
        raise HTTPException(status_code=404, detail="Category not found")
    return book

@app.post("/book", response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
async def create_book(request: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, request=request)

@app.put("/book/{title}", response_model=schemas.Book, status_code=status.HTTP_202_ACCEPTED)
async def update_book(title: str, request: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = crud.update_book(title, db, request=request)
    return book

@app.delete("/book/{isbn}", status_code=status.HTTP_202_ACCEPTED)
async def delete_book(isbn: str, db: Session = Depends(get_db)):
    book = crud.delete_book(isbn, db)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": f"Book with isbn{isbn} is sucessful deleted"}
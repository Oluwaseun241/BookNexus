# FastAPI Imports
from fastapi import FastAPI, Depends, HTTPException
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


@app.get("/book", response_model=List[schemas.Book])
async def book(db: Session = Depends(get_db)):
    books = crud.get_book(db)
    return books

@app.get("/book/{category}", response_model=schemas.Book)
async def book(category: str, db: Session = Depends(get_db)):
    book = crud.get_book_category(category, db)
    if not book:
        raise HTTPException(status_code=404, detail="Category not found")
    return book

@app.post("/book", response_model=schemas.Book)
async def create_book(request: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, request=request)

@app.put("/book/{category}", response_model=schemas.Book)
async def update_book(category: str, request: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = crud.update_book(category, db, request=request)
    return book

@app.delete("/book/{isbn}")
async def delete_book(isbn: str, db: Session = Depends(get_db)):
    book = crud.delete_book(isbn, db)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": f"book with isbn{isbn} is sucessful deleted"}
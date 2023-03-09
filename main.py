# FastAPI Imports
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

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


@app.get("/", response_model=List[schemas.Book])
async def home(db: Session = Depends(get_db)):
    books = crud.get_book(db)
    return books

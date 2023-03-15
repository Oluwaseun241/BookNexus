# FastAPI Imports
from fastapi import FastAPI, Security, Depends

# Own Imports
from app import models, Oauth2, schemas, crud
from app.database import engine, get_db
from routers import books, users, auth, carts



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books.router)

app.include_router(users.router)

app.include_router(auth.router)

app.include_router(carts.router)
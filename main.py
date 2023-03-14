# FastAPI Imports
from fastapi import FastAPI, Security

# Own Imports
from app import models, Oauth2
from app.database import engine
from routers import books, users, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



app.include_router(books.router)

app.include_router(users.router)

app.include_router(auth.router)
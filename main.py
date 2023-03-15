# FastAPI Imports
from fastapi import FastAPI, Security

# Own Imports
from app import models, Oauth2, schemas
from app.database import engine
from routers import books, users, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

cart_db = {}

@app.post("/cart/add")
async def add_to_cart(item: schemas.CartItem, user_id: int):
    if user_id not in cart_db:
        cart_db[user_id] = []
    cart_db[user_id].append(item)
    return {"message": "Item added to cart"}

app.include_router(books.router)

app.include_router(users.router)

app.include_router(auth.router)
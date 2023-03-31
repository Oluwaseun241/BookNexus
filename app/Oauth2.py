# FastAPI Imports
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from app.core import token
from app import schemas, Oauth2, crud, models
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

from decouple import config
from secret_key_generator import secret_key_generator
SECRET_KEY = secret_key_generator.generate()
ALGORITHM: str = config('JWT_ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES: int = config('TOKEN_LIFETIME')

async def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(data, credentials_exception)
    

async def is_staff(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_staff:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    elif current_user is None:
        return None
    return current_user

# fake_users_db = {
#     "johndoe": {
#         "username": "admin",
#         "email": "admin@example.com",
#         "hashed_password": "$2b$12$4g/yAkHu1vcI3AfUvXzb..vPOaYy4DE7TotmSsmMgpppBMFjtiuL6",
#         "disabled": False,
#     }
# }

# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = schemas.TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     print(user)
#     if user is None:
#         raise credentials_exception
#     return user



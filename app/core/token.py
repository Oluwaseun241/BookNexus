# JWT Imports
from jose import JWTError, jwt
from secret_key_generator import secret_key_generator

# Other Imports
from datetime import datetime, timedelta
from .. import schemas
from typing import Union
from decouple import config

SECRET_KEY = secret_key_generator.generate()
ALGORITHM: str = config('JWT_ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES: int = config('TOKEN_LIFETIME')


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
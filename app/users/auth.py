from app.users.schemas import SAuth
from app.users.dao import UsersDAO
from app.exceptions import UserDoesNotExistException, IncorrectPasswordException
from app.config import settings

from argon2 import PasswordHasher
from datetime import datetime, timezone, timedelta
from jose import jwt

pwd_context = PasswordHasher()

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(hashed_password: str, plain_password: str) -> bool:
    return pwd_context.verify(hashed_password, plain_password)

async def auth_user(auth_data: SAuth):
    user = await UsersDAO.find_one_or_none(email=auth_data.email)
    
    if user is None:
        raise UserDoesNotExistException
    
    correct_pwd = verify_password(user.hashed_password, auth_data.password.get_secret_value())
    
    if not correct_pwd:
        raise IncorrectPasswordException
    
    return user

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=1)
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.HASH_ALGO
    )
    
    # decoded_jwt = jwt.decode(
    #     str(encoded_jwt), settings.SECRET_KEY, settings.HASH_ALGO
    # )
    
    # print(decoded_jwt)
    
    return encoded_jwt
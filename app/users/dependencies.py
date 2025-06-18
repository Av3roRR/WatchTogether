from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError
from datetime import datetime, timezone

from app.users.schemas import SRegistration
from app.exceptions import (IncorrectPasswordException, IncorrectNameException,
                            LongNicknameException, IncorrectSurnameException,
                            IncorrectAgeException, IncorrectTokenException,
                            ExpiredTokenException, NoUserException)
from app.config import settings
from app.users.dao import UsersDAO

def check_registration_info(schema: SRegistration):
    pw = schema.password
    if len(pw) < 6 or len(pw) > 32:
        raise IncorrectPasswordException
    
    if len(schema.nickname) > 20:
        raise LongNicknameException
    
    if schema.name is not None and not schema.name.isalpha():
        raise IncorrectNameException
    
    if schema.surname is not None and not schema.surname.isalpha():
        raise IncorrectSurnameException
    
    age = schema.age
    if age is not None and (not isinstance(age, int) 
                                or (isinstance(age, int) and (age < 12 or age > 120))):
        raise IncorrectAgeException

def get_token(request: Request):
    token = request.cookies.get("watch_cookie")
    
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Куки нет - пользователь не авторизован")
    
    return token

async def get_current_user(current_token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            current_token, settings.SECRET_KEY, settings.HASH_ALGO
        )
    except JWTError:
        raise IncorrectTokenException
    
    expire: str = payload.get('exp')
    if not expire or (int(expire) < datetime.now(timezone.utc).timestamp()):
        raise ExpiredTokenException
    
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Отсутствуют данные о пользователе")
    
    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if user is None:
        raise NoUserException
    
    return user
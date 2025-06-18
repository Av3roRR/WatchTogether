from app.users.schemas import SRegistration, SAuth
from app.users.dao import UsersDAO
from app.exceptions import (UserAlreadyExistException, UserDoesNotExistException)
from app.users.models import Users

from app.users.auth import get_password_hash, auth_user, create_access_token
from app.users.dependencies import check_registration_info, get_current_user


from fastapi import APIRouter, Response, Depends

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)

@router.post("/registration")
async def registration(user_info: SRegistration):
    user = await UsersDAO.find_one_or_none(email=user_info.email)
    
    if user:
        raise UserAlreadyExistException
    
    check_registration_info(user_info)
    
    hashed_pwd = get_password_hash(user_info.password.get_secret_value())
    
    new_user = await UsersDAO.add(
        nickname=user_info.nickname,
        email=user_info.email,
        hashed_password=hashed_pwd,
        room_id=None,
        title=user_info.title,
        name=user_info.name,
        surname=user_info.surname,
        age=user_info.age
    )
    
    return "Пользователь успешно создан"

@router.post("/login")
async def authentication(response: Response, auth_data: SAuth):
    existing_user = await auth_user(auth_data)
    
    token_data = create_access_token({"sub": str(existing_user.id)})
    response.set_cookie("watch_cookie", token_data, httponly=True)
    
    return {"access_token": token_data}

@router.get('/me')
async def get_yourself(current_user: Users = Depends(get_current_user)):
    return current_user
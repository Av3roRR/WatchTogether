from app.users.schemas import SRegistration
from app.users.dao import UsersDAO
from app.exceptions import UserAlreadyExistException

from app.users.auth import get_password_hash
from app.users.dependencies import check_registration_info

from fastapi import APIRouter

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
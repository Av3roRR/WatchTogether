from typing import Optional
from fastapi import HTTPException, status


class WatchingException(HTTPException):
    status_code = 500
    detail=""
    
    def __init__(self, detail: Optional[str] = None):
        super().__init__(status_code=self.status_code, detail=detail or self.detail)


class IncorrectPasswordException(WatchingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Неправильная длина пароля"


class IncorrectNameException(WatchingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Имя содержит лишние символы"

class IncorrectSurnameException(WatchingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Фамилия содержит лишние символы"

class UserAlreadyExistException(WatchingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Пользователь с такой почтой уже существует"

class LongNicknameException(WatchingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Слишком длинный никнейм"

class IncorrectAgeException(WatchingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="""Некорректный возраст. Был ввёден либо возраст до 12 лет, либо слишком большой возраст.
    Перепроверьте данные"""

class UserDoesNotExistException(WatchingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Пользователя с такой почтой не существует. Можете пройти регистрацию"

class IncorrectPasswordException(WatchingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Неправильный пароль"

class IncorrectTokenException(WatchingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Некорректный токен"

class ExpiredTokenException(WatchingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Токен истёк"

class NoUserException(WatchingException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Пользователя с таким id нет"
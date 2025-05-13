from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey
from typing import Optional

from app.database import Base

class Users(Base):
    __tablename__="users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(25))
    email: Mapped[str]
    hashed_password: Mapped[str]
    room_id: Mapped[Optional[int]] = mapped_column(ForeignKey("rooms.id")) # тут будет хранится id комнаты в которой пользователь находится прямо сейчас, чтобы он не мог заходить в несколько комнат сразу
    title: Mapped[Optional[str]] = mapped_column(String(70))
    name: Mapped[Optional[str]] = mapped_column(String(255))
    surname: Mapped[Optional[str]] = mapped_column(String(255))
    age: Mapped[Optional[int]]
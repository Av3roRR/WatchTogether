from app.rooms.models import Rooms

from app.dao.base import BaseDao

class RoomsDAO(BaseDao):
    model=Rooms
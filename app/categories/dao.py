from app.dao.base import BaseDao

from app.categories.models import Categories

class CategoriesDAO(BaseDao):
    model=Categories
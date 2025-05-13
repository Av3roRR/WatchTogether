from sqlalchemy import select, insert, update, delete

from app.database import async_session_maker

class BaseDao:
    model=None
    
    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=model_id)
            result = await session.execute(query)
            
            return result.mappings().one_or_none()
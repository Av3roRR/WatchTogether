from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, JSON

from app.database import Base

class Categories(Base):
    __tablename__="categories"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(20))
    videos: Mapped[dict | None] = mapped_column(JSON)
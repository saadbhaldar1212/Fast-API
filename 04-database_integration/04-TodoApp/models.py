from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Todos(Base):
    __tablename__ = "todos"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String)
    description: str = Column(String)
    priority: int = Column(Integer)
    complete: bool = Column(Boolean)

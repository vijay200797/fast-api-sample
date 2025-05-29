from .database import Base
from sqlalchemy import Column, Integer, String


class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, index= True, autoincrement = True)
    age = Column(Integer)
    name =Column(String(64))
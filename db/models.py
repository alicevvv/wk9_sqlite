from .database import Base
from sqlalchemy import Column, Integer, String


class articals(Base):
    __tablename__ = 'articals'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    content = Column(String)


class users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    email = Column(String)
    password = Column(String)

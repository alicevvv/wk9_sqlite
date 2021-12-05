from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class articalsData(Base):
    __tablename__ = 'articals'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    content = Column(String)
    articals_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('usersData', back_populates='created_artical')
    # comment = relationship('commentData', back_populates='comment')
    # likes = relationship('likeData', back_populates='')


class usersData(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    email = Column(String)
    password = Column(String)
    created_artical = relationship('articalsData', back_populates='owner')
    # created_comment = relationship('commentData', back_populates='user')


class commentData(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    comment = Column(String)
    artical_id = Column(Integer)
    user_id = Column(Integer)
    # comment_person = relationship('usersData', back_populates='user')


class likeData(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    artical_id = Column(Integer)
    user_id = Column(Integer)

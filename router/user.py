from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from router.schemas import UserRequestSchema, UserResponseSchema
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(
    prefix='/api/v1/user',
    tags=['users']
)


@router.post('', response_model=UserResponseSchema)
def create(request: UserRequestSchema, db: Session = Depends(get_db)):
    return db_user.create(db=db, request=request)


@router.get('/feed', response_model=List[UserResponseSchema])
def feed_intial_users(db: Session = Depends(get_db)):
    return db_user.users_feed(db)


@router.get('/all', response_model=List[UserResponseSchema])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all(db=db)


@router.get('/id/{id}', response_model=UserResponseSchema)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(id=id, db=db)


@router.get('/name/{user}', response_model=UserResponseSchema)
def get_user_by_name(user: str, db: Session = Depends(get_db)):
    return db_user.get_user_by_name(name=user, db=db)

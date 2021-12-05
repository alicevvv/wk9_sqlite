from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import user
from router.schemas import UserRequestSchema
from .user_feed import user_feed

from db.models import usersData


def users_feed(db: Session):
    new_user_list = [usersData(
        user=userlist["user"],
        email=userlist["email"],
        password=userlist["password"],
    )for userlist in user_feed]
    db.query(usersData).delete()
    db.commit()
    db.add_all(new_user_list)
    db.commit()
    return db.query(usersData).all()


def create(db: Session, request: UserRequestSchema):
    new_user = usersData(
        user=request.user,
        email=request.email,
        password=request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session) -> list[usersData]:
    return db.query(usersData).all()


def get_user_by_id(id: int, db: Session) -> usersData:
    user = db.query(usersData).filter(usersData.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id ={id} 沒這個人')
    return user


def get_user_by_name(name: str, db: Session) -> usersData:
    user = db.query(usersData).filter(usersData.user == name).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User width name = {name} 沒有註冊')
    return user

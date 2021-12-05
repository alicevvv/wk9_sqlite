from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from router.schemas import ArticalRequestSchema, ArticalResponseSchema
from db.database import get_db
from typing import List
from db import db_articals


router = APIRouter(
    prefix='/api/v1/articals',
    tags=['articals']
)


@router.post('', response_model=ArticalResponseSchema)
def create(request: ArticalRequestSchema, db: Session = Depends(get_db)):
    return db_articals.create(db=db, request=request)


@router.get('/feed', response_model=List[ArticalResponseSchema])
def feed_intial_articals(db: Session = Depends(get_db)):
    return db_articals.artical_feed(db)


@router.get('/all', response_model=List[ArticalResponseSchema])
def get_all_articals(db: Session = Depends(get_db)):
    return db_articals.get_all(db=db)


@router.get("/id/{id}", response_model=ArticalResponseSchema)
def get_artical_by_id(id: int, db: Session = Depends(get_db)):
    return db_articals.get_artical_by_id(id=id, db=db)


@router.get("/{author}", response_model=List[ArticalResponseSchema])
def get_artical_by_author(author: str, db: Session = Depends(get_db)):
    return db_articals.get_artical_by_author(author=author, db=db)

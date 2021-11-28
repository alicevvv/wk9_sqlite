from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from router.schemas import ArticalRequestSchema, ArticalResponseSchema
from db.database import get_db
from db import db_articals
from typing import List


router = APIRouter(
    prefix='/api/v1/articals',
    tags=['articals']
)


@router.post('', response_model=ArticalResponseSchema)
def create(request: ArticalRequestSchema, db: Session = Depends(get_db)):
    return db_articals.create(db, request)


@router.get('/all', response_model=List[ArticalResponseSchema])
def get_all_articals(db: Session = Depends(get_db)):
    return db_articals.get_all(db)


@router.get("/", response_model=ArticalResponseSchema)
def get_all_articals(db: Session = Depends(get_db)):
    return db_articals.get_all(db)


@router.get("/id/{id}", response_model=List[ArticalResponseSchema])
def get_artical_by_id(id: int, db: Session = Depends(get_db)):
    return db_articals.get_product_by_id(id, db)


@router.get("/{author}")
def get_artical_by_author(author: str, db: Session = Depends(get_db)):
    return db_articals.get_product_by_author(author, db)

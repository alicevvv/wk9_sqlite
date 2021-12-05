from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from router.schemas import ArticalRequestSchema
from .articals_feed import articals_feed

from db.models import articalsData


def artical_feed(db: Session):
    new_artical_list = [articalsData(
        title=articals["title"],
        author=articals["author"],
        content=articals["content"],
        articals_id=articals["articals_id"],
    )for articals in articals_feed]
    db.query(articalsData).delete()
    db.commit()
    db.add_all(new_artical_list)
    db.commit()
    return db.query(articalsData).all()


def create(db: Session, request: ArticalRequestSchema) -> articalsData:
    new_artical = articalsData(
        title=request.title,
        author=request.author,
        content=request.content,
        articals_id=request.articals_id,
    )
    db.add(new_artical)
    db.commit()
    db.refresh(new_artical)
    return new_artical


def get_all(db: Session) -> list[articalsData]:
    return db.query(articalsData).all()


def get_artical_by_id(id: int, db: Session) -> articalsData:
    artical = db.query(articalsData).filter(articalsData.id == id).first()
    if not artical:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Artical with id = {id} 找不到啦')
    return artical


def get_artical_by_author(author: str, db: Session) -> list[articalsData]:
    author = db.query(articalsData).filter(articalsData.author == author).all()
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Author with {author} not found')
    return author

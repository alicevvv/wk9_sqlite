from sqlalchemy.orm.session import Session
from db.models import articals
from router.schemas import ArticalRequestSchema


def create(db: Session, request: ArticalRequestSchema) -> articals:
    new_artical = articals(
        title=request.title,
        author=request.author,
        content=request.content
    )
    db.add(new_artical)
    db.commit()
    db.refresh(new_artical)
    return new_artical


def get_all(db: Session):
    return db.query(articals).all()


def get_product_by_id(id: int, db: Session):
    return db.query(articals).filter(articals.id == id).first()


def get_product_by_author(author: str, db: Session):
    return db.query(articals).filter(articals.author == author).all()

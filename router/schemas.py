from pydantic import BaseModel


class ArticalRequestSchema(BaseModel):
    title: str
    author: str
    content: str


class ArticalResponseSchema(ArticalRequestSchema):
    id: int

    class Config():
        orm_mode = True

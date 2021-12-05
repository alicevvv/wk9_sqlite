from pydantic import BaseModel
from typing import List


class ArticalRequestSchema(BaseModel):
    title: str
    author: str
    content: str
    articals_id: int


class UserRequestSchema(BaseModel):
    user: str
    email: str
    password: str


# class CommentRequestSchema(BaseModel):
#     user: str
#     comment: str
#     artical_id: int
#     user_id: int


class OnlyUserResponseSchema(UserRequestSchema):
    pass

    class Config:
        orm_mode = True


class ArticalResponseSchema(ArticalRequestSchema):
    id: int
    articals_id: int
    owner: OnlyUserResponseSchema

    class Config:
        orm_mode = True


class UserResponseSchema(UserRequestSchema):
    id: int
    created_artical: List[ArticalResponseSchema] = []

    class Config:
        orm_mode = True


# class CommentResponseSchema(UserRequestSchema):
#     comment_person: List[UserResponseSchema] = []

import uvicorn
from fastapi import FastAPI
from db.articalJson import artical_list
from router import artical

app = FastAPI(
    title="artical API",
    description="This is my homework i am trying",
    version="0.0.1",
    terms_of_service="http://localhost:5000"
)
app.include_router(artical.router)


# @app.get("/")
# def root():
#     return {"title": "Hello World Alice"}


# @app.get("/articals")
# def get_all_artical():
#     return artical_list


# @app.get("/articals/id/{id}")
# def get_artical_by_id(id):
#     return next(
#         (artical for artical in artical_list if artical['id'] == id
#          ), None
#     )


# @app.get("/articals/{author}")
# def get_artical_by_author(author):
#     author_list = []
#     for people in artical_list:
#         if people['author'] == author:
#             author_list.append(people)
#     return author_list


if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, reload=True)

from fastapi import APIRouter
from db.articalJson import artical_list

router = APIRouter(
    prefix='/api/v1/articals',
    tags=['articals']
)


@router.get('/all')
def get_all_articals():
    return artical_list


@router.get("/")
async def get_all_articals():
    return artical_list


@router.get("/id/{id}")
async def get_artical_by_id(id):
    return next(
        (artical for artical in artical_list if artical['id'] == id
         ), None
    )


@router.get("/{author}")
async def get_artical_by_author(author):
    author_list = []
    for people in artical_list:
        if people['author'] == author:
            author_list.append(people)
    return author_list

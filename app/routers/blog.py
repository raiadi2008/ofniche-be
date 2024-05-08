from fastapi import APIRouter, status

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
async def get_blogs():
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_blog():
    pass


@router.get("/{blog_id}", status_code=status.HTTP_200_OK)
async def get_blog(blog_id: str):
    pass


@router.put("/{blog_id}", status_code=status.HTTP_200_OK)
async def update_blog(blog_id: str):
    pass

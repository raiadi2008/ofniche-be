from fastapi import APIRouter, status

from app.models import niche

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
async def get_niches(niche: niche.Niche):
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_niche(niche: Nich):
    pass


@router.get("/{niche_id}", status_code=status.HTTP_200_OK)
async def get_niche(niche_id: str):
    pass


@router.put("/{niche_id}", status_code=status.HTTP_200_OK)
async def update_niche(niche_id: str):
    pass


@router.delete("/{niche_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_niche(niche_id: str):
    pass

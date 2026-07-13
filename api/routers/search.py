from fastapi import APIRouter

from api.services.search_service import (
    SearchService,
)

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@router.post("")
async def search(
    payload: dict,
):

    return SearchService.run(
        payload
    )
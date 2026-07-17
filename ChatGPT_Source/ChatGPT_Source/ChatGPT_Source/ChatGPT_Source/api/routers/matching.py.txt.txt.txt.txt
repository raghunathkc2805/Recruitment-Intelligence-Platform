from fastapi import APIRouter

from api.services.matching_service import (
    MatchingService,
)

router = APIRouter(
    prefix="/matching",
    tags=["Matching"],
)


@router.post("/run")
async def run_matching(
    payload: dict,
):

    return MatchingService.run(
        payload
    )
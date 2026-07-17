from fastapi import APIRouter

from api.services.ranking_service import (
    RankingService,
)

router = APIRouter(
    prefix="/ranking",
    tags=["Ranking"],
)


@router.post("/run")
async def run_ranking(
    payload: dict,
):

    return RankingService.run(
        payload
    )
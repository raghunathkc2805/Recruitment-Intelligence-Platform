from fastapi import APIRouter

from api.dependencies import DatabaseSession
from api.services.matching_service import MatchingService

router = APIRouter(
    prefix="/matching",
    tags=["Matching"],
)


@router.post("/run")
async def run_matching(
    payload: dict,
    db: DatabaseSession,
):

    return MatchingService.run(
        db,
        payload,
    )

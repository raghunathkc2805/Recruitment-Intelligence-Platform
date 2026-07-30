from fastapi import APIRouter
from fastapi import Depends

from api.auth.permission_constants import Permission
from api.auth.permission_dependency import require_permission
from api.services.ranking_service import RankingService

router = APIRouter(
    prefix="/ranking",
    tags=["Ranking"],
)


@router.post(
    "/run",
    dependencies=[
        Depends(
            require_permission(
                Permission.RANKING_RUN,
            )
        )
    ],
)
async def run_ranking(
    payload: dict,
):
    return RankingService.run(
        payload,
    )

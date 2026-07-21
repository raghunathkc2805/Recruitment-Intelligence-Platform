from fastapi import APIRouter
from fastapi import Depends

from api.auth.permission_constants import Permission
from api.auth.permission_dependency import require_permission
from api.dependencies import DatabaseSession
from api.services.matching_service import MatchingService

router = APIRouter(
    prefix="/matching",
    tags=["Matching"],
)


@router.post(
    "/run",
    dependencies=[
        Depends(
            require_permission(
                Permission.MATCHING_RUN,
            )
        )
    ],
)
async def run_matching(
    payload: dict,
    db: DatabaseSession,
):
    return MatchingService.run(
        db,
        payload,
    )

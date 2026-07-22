from fastapi import APIRouter
from fastapi import Depends

from api.auth.permission_constants import Permission
from api.auth.permission_dependency import require_permission
from api.dependencies import DatabaseSession
from api.services.matching_service import MatchingService
from api.background import background_manager
from api.background.jobs.candidate_matching_job import process_candidate_matching

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

# ==============================================================================
# Queue Candidate Matching
# ==============================================================================

def queue_candidate_matching(
    matching_service,
    candidate_id: str,
    job_id: str,
):

    return background_manager.submit(
        "candidate_matching",
        process_candidate_matching,
        matching_service,
        candidate_id,
        job_id,
    )


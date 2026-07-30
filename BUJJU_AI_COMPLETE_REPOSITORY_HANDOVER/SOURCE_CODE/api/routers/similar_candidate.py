from fastapi import APIRouter

from api.dependencies import DatabaseSession
from api.services.similar_candidate_service import SimilarCandidateService


router = APIRouter(
    prefix="/similar-candidates",
    tags=["Similar Candidates"],
)


@router.post("/recommend")
def recommend(
    payload: dict,
    db: DatabaseSession,
):

    return SimilarCandidateService.recommend(
        db,
        payload["candidate_id"],
        payload.get(
            "limit",
            10,
        ),
    )
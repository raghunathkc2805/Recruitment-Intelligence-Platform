from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.candidate_rediscovery_service import (
    CandidateRediscoveryService,
)

from api.services.similar_candidate_service import (
    SimilarCandidateService,
)


router = APIRouter(
    prefix="/candidate-discovery",
    tags=["Candidate Discovery"],
)


@router.post("/rediscover")
def rediscover(
    payload: dict,
    db: DatabaseSession,
):

    return CandidateRediscoveryService.search(
        db,
        payload.get(
            "skills",
            [],
        ),
        payload.get(
            "limit",
            20,
        ),
    )


@router.post("/similar")
def similar(
    payload: dict,
    db: DatabaseSession,
):

    return SimilarCandidateService.recommend(
        db,
        payload["candidate_id"],
        payload.get(
            "candidates",
            [],
        ),
    )
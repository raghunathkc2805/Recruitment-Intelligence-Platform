from fastapi import APIRouter

from api.dependencies import DatabaseSession
from api.services.candidate_intelligence_service import (
    CandidateIntelligenceService,
)


router = APIRouter(
    prefix="/candidate-intelligence",
    tags=["Candidate Intelligence"],
)


@router.post("/rediscover")
def rediscover(
    payload: dict,
    db: DatabaseSession,
):

    return CandidateIntelligenceService.rediscover(
        db,
        payload,
    )


@router.post("/rank")
def rank(
    payload: dict,
    db: DatabaseSession,
):

    return CandidateIntelligenceService.rank_candidates(
        payload.get(
            "candidates",
            [],
        ),
        payload.get(
            "job",
            {},
        ),
    )
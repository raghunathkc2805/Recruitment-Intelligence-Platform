from fastapi import APIRouter

from api.services.ai_candidate_ranking_service import (
    AICandidateRankingService,
)


router = APIRouter(
    prefix="/ai-ranking",
    tags=["AI Candidate Ranking"],
)


@router.post("/rank")
def rank(
    payload: dict,
):

    return AICandidateRankingService.rank(
        payload.get(
            "candidates",
            [],
        ),
        payload.get(
            "job",
            {},
        ),
    )
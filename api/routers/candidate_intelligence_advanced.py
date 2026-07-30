from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.candidate_career_intelligence_service import (
    CandidateCareerIntelligenceService,
)

from api.services.candidate_risk_service import (
    CandidateRiskService,
)


router = APIRouter(
    prefix="/candidate-analysis",
    tags=["Candidate Intelligence Advanced"],
)


@router.post("/career")
def career(
    payload: dict,
    db: DatabaseSession,
):

    return CandidateCareerIntelligenceService.analyse(
        db,
        payload["candidate_id"],
        payload.get(
            "experience",
            [],
        ),
        payload.get(
            "designation_history",
            [],
        ),
    )


@router.post("/risk")
def risk(
    payload: dict,
    db: DatabaseSession,
):

    return CandidateRiskService.analyse(
        db,
        payload["candidate_id"],
        payload.get(
            "employment_history",
            [],
        ),
        payload.get(
            "resume",
            {},
        ),
    )
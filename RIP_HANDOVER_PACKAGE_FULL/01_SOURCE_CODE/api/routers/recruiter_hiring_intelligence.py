from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.recruiter_intelligence_service import RecruiterIntelligenceService
from api.services.hiring_success_service import HiringSuccessService


router = APIRouter(
    prefix="/recruitment-intelligence",
    tags=["Recruiter Intelligence"],
)


@router.post("/recruiter")
def recruiter_analysis(
    payload: dict,
    db: DatabaseSession,
):

    return RecruiterIntelligenceService.analyse(
        db,
        payload["recruiter_id"],
        payload.get(
            "hires",
            [],
        ),
        payload.get(
            "domains",
            [],
        ),
    )


@router.post("/hiring-success")
def hiring_success(
    payload: dict,
    db: DatabaseSession,
):

    return HiringSuccessService.record(
        db,
        payload["candidate_id"],
        payload["recruiter_id"],
        payload.get(
            "source",
            "",
        ),
        payload.get(
            "outcome",
            "",
        ),
        payload.get(
            "acceptance_score",
            0,
        ),
        payload.get(
            "joining_success",
            0,
        ),
        payload.get(
            "feedback",
            "",
        ),
    )


@router.get("/source-analysis/{source}")
def source_analysis(
    source: str,
    db: DatabaseSession,
):

    return HiringSuccessService.analyse_source(
        db,
        source,
    )
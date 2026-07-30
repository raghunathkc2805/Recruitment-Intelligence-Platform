from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.resume_intelligence_service import ResumeIntelligenceService
from api.services.jd_intelligence_service import JDIntelligenceService


router = APIRouter(
    prefix="/intelligence",
    tags=["AI Intelligence"],
)


@router.post("/resume/analyse")
def analyse_resume(
    payload: dict,
    db: DatabaseSession,
):

    return ResumeIntelligenceService.analyse(
        db,
        payload["candidate_id"],
        payload.get(
            "resume",
            {}
        ),
    )


@router.post("/jd/analyse")
def analyse_jd(
    payload: dict,
    db: DatabaseSession,
):

    return JDIntelligenceService.analyse(
        db,
        payload["job_id"],
        payload.get(
            "jd",
            {}
        ),
    )
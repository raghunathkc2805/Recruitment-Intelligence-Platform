from fastapi import APIRouter


from api.services.resume_intelligence_service import (
    ResumeIntelligenceService,
)

from api.services.jd_intelligence_service import (
    JDIntelligenceService,
)


router = APIRouter(
    prefix="/intelligence",
    tags=["AI Intelligence"],
)


@router.post("/resume")
def resume_analysis(
    payload: dict,
):

    return ResumeIntelligenceService.analyse(
        payload.get(
            "resume",
            {},
        ),
        payload.get(
            "job",
            {},
        ),
    )



@router.post("/jd")
def jd_analysis(
    payload: dict,
):

    return JDIntelligenceService.analyse(
        payload.get(
            "jd",
            {},
        )
    )
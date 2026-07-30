from fastapi import APIRouter

from api.services.explainable_ai_service import ExplainableAIService


router = APIRouter(
    prefix="/explainable-ai",
    tags=["Explainable AI"],
)


@router.post("/score")
def score(
    payload: dict,
):

    return ExplainableAIService.generate(
        payload.get(
            "skill_score",
            0,
        ),
        payload.get(
            "experience_score",
            0,
        ),
        payload.get(
            "location_score",
            0,
        ),
        payload.get(
            "organization_score",
            0,
        ),
    )
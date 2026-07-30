from fastapi import APIRouter

from api.dependencies import DatabaseSession
from api.services.skill_intelligence_service import SkillIntelligenceService


router = APIRouter(
    prefix="/skill-intelligence",
    tags=["Skill Intelligence"],
)


@router.post("/register")
def register_skill(
    payload: dict,
    db: DatabaseSession,
):

    return SkillIntelligenceService.register_skill(
        db,
        payload["skill_name"],
        payload.get(
            "category",
            "General",
        ),
        payload.get(
            "confidence",
            0,
        ),
    )


@router.post("/search")
def search_skill(
    payload: dict,
    db: DatabaseSession,
):

    return SkillIntelligenceService.search_skill(
        db,
        payload["skill_name"],
    )
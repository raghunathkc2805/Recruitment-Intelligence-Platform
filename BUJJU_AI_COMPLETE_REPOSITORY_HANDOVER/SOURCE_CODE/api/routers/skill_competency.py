from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.skill_adjacency_service import SkillAdjacencyService
from api.services.competency_gap_service import CompetencyGapService


router = APIRouter(
    prefix="/skill-intelligence",
    tags=["Skill Intelligence Advanced"],
)


@router.post("/adjacent")
def adjacent(
    payload: dict,
):

    return SkillAdjacencyService.recommend(
        payload.get(
            "skills",
            [],
        )
    )


@router.post("/competency-gap")
def competency_gap(
    payload: dict,
    db: DatabaseSession,
):

    return CompetencyGapService.analyse(
        db,
        payload["candidate_id"],
        payload["job_id"],
        payload.get(
            "candidate_skills",
            [],
        ),
        payload.get(
            "required_skills",
            [],
        ),
    )
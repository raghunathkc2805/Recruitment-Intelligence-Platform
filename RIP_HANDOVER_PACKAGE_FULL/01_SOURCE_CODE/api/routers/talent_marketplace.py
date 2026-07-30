from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.talent_marketplace_service import (
    TalentMarketplaceService,
)


router = APIRouter(
    prefix="/talent-marketplace",
    tags=["Internal Talent Marketplace"],
)


@router.post("/add")
def add(
    payload: dict,
    db: DatabaseSession,
):

    return TalentMarketplaceService.add_candidate(
        db,
        payload["candidate_id"],
        payload.get(
            "candidate_type",
            "Previous Applicant",
        ),
        payload.get(
            "skills",
            [],
        ),
        payload.get(
            "previous_outcome",
            "",
        ),
    )


@router.post("/search")
def search(
    payload: dict,
    db: DatabaseSession,
):

    return TalentMarketplaceService.search(
        db,
        payload.get(
            "skills",
            [],
        ),
    )
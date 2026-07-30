from fastapi import APIRouter

from api.dependencies import DatabaseSession
from api.services.designation_intelligence_service import (
    DesignationIntelligenceService,
)


router = APIRouter(
    prefix="/designation-intelligence",
    tags=["Designation Intelligence"],
)


@router.post("/register")
def register(
    payload: dict,
    db: DatabaseSession,
):

    return DesignationIntelligenceService.register_designation(
        db,
        payload["designation"],
        payload.get(
            "domain",
            "General",
        ),
    )


@router.post("/search")
def search(
    payload: dict,
    db: DatabaseSession,
):

    return DesignationIntelligenceService.search_designation(
        db,
        payload["designation"],
    )


@router.post("/related")
def related(
    payload: dict,
    db: DatabaseSession,
):

    return DesignationIntelligenceService.find_related_roles(
        db,
        payload["designation"],
    )
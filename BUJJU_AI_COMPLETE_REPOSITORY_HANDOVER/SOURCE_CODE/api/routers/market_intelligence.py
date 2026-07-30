from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.market_intelligence_service import MarketIntelligenceService
from api.services.knowledge_refresh_service import KnowledgeRefreshService


router = APIRouter(
    prefix="/market-intelligence",
    tags=["Market Intelligence"],
)


@router.post("/create")
def create(
    payload: dict,
    db: DatabaseSession,
):

    return MarketIntelligenceService.create(
        db,
        payload["domain"],
        payload["intelligence_type"],
        payload["title"],
        payload.get(
            "information",
            {},
        ),
        payload.get(
            "confidence_score",
            0,
        ),
    )


@router.get("/{domain}")
def search(
    domain: str,
    db: DatabaseSession,
):

    return MarketIntelligenceService.search(
        db,
        domain,
    )


@router.post("/refresh-schedule")
def refresh_schedule(
    payload: dict,
    db: DatabaseSession,
):

    return KnowledgeRefreshService.create_schedule(
        db,
        payload["domain"],
        payload.get(
            "frequency",
            "monthly",
        ),
    )


@router.get("/refresh/pending")
def pending(
    db: DatabaseSession,
):

    return KnowledgeRefreshService.pending_refreshes(
        db,
    )
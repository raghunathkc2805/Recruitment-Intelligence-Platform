from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.analytics_service import AnalyticsService


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.post("/event")
def event(
    payload: dict,
    db: DatabaseSession,
):

    return AnalyticsService.record(
        db,
        payload["event_type"],
        payload.get(
            "entity_type",
            "",
        ),
        payload.get(
            "entity_id",
            "",
        ),
        payload.get(
            "metric_value",
            0,
        ),
        payload.get(
            "metadata",
            {},
        ),
    )


@router.get("/dashboard")
def dashboard(
    db: DatabaseSession,
):

    return AnalyticsService.dashboard(
        db
    )
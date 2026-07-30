from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.continuous_learning_service import ContinuousLearningService


router = APIRouter(
    prefix="/learning",
    tags=["Continuous Learning"],
)


@router.post("/capture")
def capture(
    payload: dict,
    db: DatabaseSession,
):

    return ContinuousLearningService.capture(
        db,
        payload["event_type"],
        payload["entity_type"],
        payload["entity_id"],
        payload.get(
            "data",
            {},
        ),
        payload.get(
            "confidence_score",
            0,
        ),
    )


@router.get("/{entity_type}/{entity_id}")
def history(
    entity_type: str,
    entity_id: str,
    db: DatabaseSession,
):

    return ContinuousLearningService.history(
        db,
        entity_type,
        entity_id,
    )


@router.post("/approve/{event_id}")
def approve(
    event_id: str,
    db: DatabaseSession,
):

    return ContinuousLearningService.approve(
        db,
        event_id,
    )
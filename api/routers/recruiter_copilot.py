from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.recruiter_copilot_service import RecruiterCopilotService
from api.services.ai_search_assistant_service import AISearchAssistantService


router = APIRouter(
    prefix="/recruiter-ai",
    tags=["Recruiter AI"],
)


@router.post("/copilot")
def copilot(
    payload: dict,
    db: DatabaseSession,
):

    return RecruiterCopilotService.assist(
        db,
        payload.get(
            "recruiter_id",
            "system",
        ),
        payload["query"],
    )


@router.post("/boolean-search")
def boolean_search(
    payload: dict,
):

    return AISearchAssistantService.generate_search(
        payload
    )
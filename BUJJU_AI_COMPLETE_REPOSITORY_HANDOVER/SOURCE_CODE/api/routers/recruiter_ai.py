from fastapi import APIRouter


from api.services.recruiter_copilot_service import (
    RecruiterCopilotService,
)

from api.services.ai_search_assistant_service import (
    AISearchAssistantService,
)

from api.services.boolean_search_service import (
    BooleanSearchService,
)


router = APIRouter(
    prefix="/recruiter-ai",
    tags=["Recruiter AI"],
)



@router.post("/copilot")
def copilot(
    payload: dict,
):

    return RecruiterCopilotService.assist(
        payload.get(
            "query",
            "",
        ),
        payload.get(
            "context",
            {},
        ),
    )



@router.post("/search-assistant")
def search_assistant(
    payload: dict,
):

    return AISearchAssistantService.search_intent(
        payload.get(
            "query",
            "",
        )
    )



@router.post("/boolean")
def boolean(
    payload: dict,
):

    return BooleanSearchService.generate(
        payload.get(
            "designation",
            "",
        ),
        payload.get(
            "skills",
            [],
        ),
        payload.get(
            "experience",
            "",
        ),
    )
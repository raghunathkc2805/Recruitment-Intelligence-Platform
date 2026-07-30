from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.whatsapp_outreach_service import WhatsAppOutreachService


router = APIRouter(
    prefix="/whatsapp",
    tags=["WhatsApp Outreach"],
)


@router.post("/create")
def create(
    payload: dict,
    db: DatabaseSession,
):

    return WhatsAppOutreachService.create_template_message(
        db,
        payload["candidate_id"],
        payload.get(
            "template_name",
            "candidate_intro",
        ),
        payload.get(
            "variables",
            {},
        ),
    )
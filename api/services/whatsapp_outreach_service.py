from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.whatsapp_outreach import WhatsAppOutreach


class WhatsAppOutreachService:


    @classmethod
    def create_template_message(
        cls,
        db: Session,
        candidate_id: str,
        template_name: str,
        variables: dict,
    ):

        templates = {

            "candidate_intro":
            "Hello {name}, we have an opportunity matching your profile.",

            "follow_up":
            "Hello {name}, following up regarding the opportunity shared with you.",
        }


        template = templates.get(
            template_name,
            "Hello {name}, recruitment team would like to connect with you."
        )


        message = template.format(
            **variables
        )


        outreach = WhatsAppOutreach(
            candidate_id=candidate_id,
            template_name=template_name,
            message=message,
        )


        db.add(outreach)

        db.commit()

        db.refresh(outreach)


        return outreach
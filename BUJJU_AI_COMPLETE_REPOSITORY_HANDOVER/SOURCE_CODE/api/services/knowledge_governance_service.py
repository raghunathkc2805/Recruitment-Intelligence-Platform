from __future__ import annotations

import json

from sqlalchemy.orm import Session

from database.models.knowledge_version import KnowledgeVersion
from database.models.knowledge_audit import KnowledgeAudit
from database.models.knowledge_entry import KnowledgeEntry


class KnowledgeGovernanceService:


    @classmethod
    def create_version(
        cls,
        db: Session,
        knowledge_id: str,
        old_value: str,
        new_value: str,
        confidence_score: float,
    ):

        version = KnowledgeVersion(
            knowledge_id=knowledge_id,
            version="1.0",
            previous_value=old_value,
            new_value=new_value,
            confidence_score=confidence_score,
        )

        db.add(version)


        audit = KnowledgeAudit(
            knowledge_id=knowledge_id,
            action="VERSION_CREATED",
            details=json.dumps(
                {
                    "new_value": new_value,
                    "confidence": confidence_score,
                }
            ),
        )

        db.add(audit)

        db.commit()

        db.refresh(version)

        return version


    @classmethod
    def approve_version(
        cls,
        db: Session,
        version_id: str,
    ):

        version = (
            db.query(KnowledgeVersion)
            .filter(
                KnowledgeVersion.id ==
                version_id
            )
            .first()
        )

        if not version:
            return None


        version.approved = True


        audit = KnowledgeAudit(
            knowledge_id=version.knowledge_id,
            action="VERSION_APPROVED",
            details=json.dumps(
                {
                    "version": version.version
                }
            ),
        )

        db.add(audit)

        db.commit()

        db.refresh(version)

        return version


    @classmethod
    def audit_history(
        cls,
        db: Session,
        knowledge_id: str,
    ):

        return (
            db.query(KnowledgeAudit)
            .filter(
                KnowledgeAudit.knowledge_id ==
                knowledge_id
            )
            .order_by(
                KnowledgeAudit.created_at.desc()
            )
            .all()
        )
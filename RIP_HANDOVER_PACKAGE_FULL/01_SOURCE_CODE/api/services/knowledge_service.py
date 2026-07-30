from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.knowledge_entry import KnowledgeEntry
from database.models.knowledge_audit import KnowledgeAudit
from database.models.knowledge_version import KnowledgeVersion


class KnowledgeService:


    @classmethod
    def approve(
        cls,
        db: Session,
        knowledge_id: str,
        user="system",
    ):

        entry = (
            db.query(KnowledgeEntry)
            .filter(
                KnowledgeEntry.id == knowledge_id
            )
            .first()
        )

        if not entry:
            raise ValueError(
                "Knowledge entry not found"
            )

        entry.approved = True

        db.add(
            KnowledgeVersion(
                knowledge_id=entry.id,
                version=entry.version,
                value=entry.value,
                action="APPROVED",
                created_by=user,
            )
        )

        db.add(
            KnowledgeAudit(
                knowledge_id=entry.id,
                action="APPROVED",
                performed_by=user,
            )
        )

        db.commit()

        db.refresh(entry)

        return entry


    @classmethod
    def update(
        cls,
        db: Session,
        knowledge_id: str,
        value: str,
        user="system",
    ):

        entry = (
            db.query(KnowledgeEntry)
            .filter(
                KnowledgeEntry.id == knowledge_id
            )
            .first()
        )

        if not entry:
            raise ValueError(
                "Knowledge entry not found"
            )

        old_value = entry.value

        major, minor = entry.version.split(".")

        entry.version = (
            f"{major}.{int(minor)+1}"
        )

        entry.value = value
        entry.approved = False

        db.add(
            KnowledgeVersion(
                knowledge_id=entry.id,
                version=entry.version,
                value=value,
                action="UPDATED",
                created_by=user,
            )
        )

        db.add(
            KnowledgeAudit(
                knowledge_id=entry.id,
                action="UPDATED",
                old_value=old_value,
                new_value=value,
                performed_by=user,
            )
        )

        db.commit()

        db.refresh(entry)

        return entry


    @classmethod
    def history(
        cls,
        db: Session,
        knowledge_id: str,
    ):

        return (
            db.query(KnowledgeVersion)
            .filter(
                KnowledgeVersion.knowledge_id ==
                knowledge_id
            )
            .order_by(
                KnowledgeVersion.created_at.desc()
            )
            .all()
        )


    @classmethod
    def rollback(
        cls,
        db: Session,
        knowledge_id: str,
        version: str,
    ):

        target = (
            db.query(KnowledgeVersion)
            .filter(
                KnowledgeVersion.knowledge_id ==
                knowledge_id,
                KnowledgeVersion.version ==
                version,
            )
            .first()
        )

        if not target:
            raise ValueError(
                "Version not found"
            )

        entry = (
            db.query(KnowledgeEntry)
            .filter(
                KnowledgeEntry.id ==
                knowledge_id
            )
            .first()
        )

        entry.value = target.value
        entry.version = version
        entry.approved = False

        db.add(
            KnowledgeAudit(
                knowledge_id=entry.id,
                action="ROLLBACK",
                new_value=target.value,
            )
        )

        db.commit()

        return entry
"""
Resume Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.resume import Resume

from .base_repository import BaseRepository


class ResumeRepository(BaseRepository):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

    def create(
        self,
        resume: Resume,
    ) -> Resume:

        return self.add(
            resume
        )

    def get(
        self,
        resume_id: str,
    ) -> Resume | None:

        return (
            self.db.query(
                Resume
            )
            .filter(
                Resume.id == resume_id
            )
            .first()
        )

    def get_by_hash(
        self,
        resume_hash: str,
    ) -> Resume | None:

        return (
            self.db.query(
                Resume
            )
            .filter(
                Resume.resume_hash == resume_hash
            )
            .first()
        )

    def get_by_candidate(
        self,
        candidate_id: str,
    ) -> list[Resume]:

        return (
            self.db.query(
                Resume
            )
            .filter(
                Resume.candidate_id == candidate_id
            )
            .order_by(
                Resume.created_at.desc()
            )
            .all()
        )

    def list(
        self,
    ) -> list[Resume]:

        return (
            self.db.query(
                Resume
            )
            .order_by(
                Resume.created_at.desc()
            )
            .all()
        )

    def update(
        self,
        resume: Resume,
    ) -> Resume:

        self.db.commit()
        self.db.refresh(
            resume
        )
        return resume

    def delete(
        self,
        resume: Resume,
    ) -> None:

        self.db.delete(
            resume
        )

        self.db.commit()

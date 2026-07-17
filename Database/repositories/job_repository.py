"""
Job Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.job_description import JobDescription

from .base_repository import BaseRepository


class JobRepository(BaseRepository):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

    def create(
        self,
        job: JobDescription,
    ) -> JobDescription:

        return self.add(job)

    def get(
        self,
        job_id: str,
    ) -> JobDescription | None:

        return (
            self.db.query(JobDescription)
            .filter(JobDescription.id == job_id)
            .first()
        )

    def list(
        self,
    ) -> list[JobDescription]:

        return (
            self.db.query(JobDescription)
            .order_by(
                JobDescription.created_at.desc()
            )
            .all()
        )

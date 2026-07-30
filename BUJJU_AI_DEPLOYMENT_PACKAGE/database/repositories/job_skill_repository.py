"""
Job Skill Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.job_skill import JobSkill

from .base_repository import BaseRepository


class JobSkillRepository(BaseRepository):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

    def create(
        self,
        job_id: str,
        skill_name: str,
        category: str = "General",
    ):

        return self.add(

            JobSkill(

                job_id=job_id,

                skill_name=skill_name,

                skill_category=category,

            )

        )

    def list_by_job(
        self,
        job_id: str,
    ):

        return (

            self.db.query(JobSkill)

            .filter(
                JobSkill.job_id == job_id
            )

            .all()

        )

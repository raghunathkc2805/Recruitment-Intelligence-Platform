"""
Candidate Skill Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.candidate_skill import CandidateSkill

from .base_repository import BaseRepository


class CandidateSkillRepository(BaseRepository):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

    def create(
        self,
        candidate_id: str,
        skill_name: str,
        category: str = "General",
    ):

        return self.add(

            CandidateSkill(

                candidate_id=candidate_id,

                skill_name=skill_name,

                skill_category=category,

            )

        )

    def search(

        self,

        skill: str,

    ):

        return (

            self.db.query(

                CandidateSkill

            )

            .filter(

                CandidateSkill.skill_name.ilike(

                    f"%{skill}%"

                )

            )

            .all()

        )

    def list_by_candidate(

        self,

        candidate_id: str,

    ):

        return (

            self.db.query(

                CandidateSkill

            )

            .filter(

                CandidateSkill.candidate_id == candidate_id

            )

            .all()

        )

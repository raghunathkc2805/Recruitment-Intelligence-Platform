"""
Enterprise Candidate Search Repository
"""

from __future__ import annotations

from sqlalchemy import and_
from sqlalchemy.orm import Session

from database.models.candidate import Candidate
from database.models.candidate_skill import CandidateSkill


class CandidateSearchRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def search(
        self,
        *,
        skills: list[str] | None = None,
        designation: str | None = None,
        location: str | None = None,
        minimum_experience: float | None = None,
    ) -> list[Candidate]:

        query = self.db.query(
            Candidate
        )

        if designation:

            query = query.filter(

                Candidate.current_designation.ilike(

                    f"%{designation}%"

                )

            )

        if location:

            query = query.filter(

                Candidate.location.ilike(

                    f"%{location}%"

                )

            )

        if minimum_experience is not None:

            query = query.filter(

                Candidate.experience_years >= minimum_experience

            )

        candidates = query.all()

        if not skills:

            return candidates

        required = {

            skill.lower().strip()

            for skill in skills

        }

        matched_candidates = []

        for candidate in candidates:

            candidate_skills = {

                row.skill_name.lower()

                for row in self.db.query(

                    CandidateSkill

                ).filter(

                    CandidateSkill.candidate_id == candidate.id

                )

            }

            if required.issubset(

                candidate_skills

            ):

                matched_candidates.append(

                    candidate

                )

        return matched_candidates

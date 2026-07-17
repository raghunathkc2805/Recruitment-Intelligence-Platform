"""
Candidate Service
"""

from __future__ import annotations

from database.models.candidate import Candidate
from database.repositories.candidate_repository import (
    CandidateRepository,
)


class CandidateService:

    @classmethod
    def create(
        cls,
        db,
        payload: dict,
    ) -> Candidate:

        repository = CandidateRepository(db)

        existing = repository.get_by_email(
            payload["email"]
        )

        if existing:
            raise ValueError(
                "Candidate already exists."
            )

        candidate = Candidate(
            candidate_code=payload["candidate_code"],
            full_name=payload["full_name"],
            email=payload["email"],
            mobile=payload.get(
                "mobile",
                "",
            ),
            location=payload.get(
                "location",
                "",
            ),
            experience_years=payload.get(
                "experience_years",
                0,
            ),
            current_designation=payload.get(
                "current_designation",
                "",
            ),
        )

        return repository.create(candidate)

    @classmethod
    def list(
        cls,
        db,
    ):

        return CandidateRepository(db).list()
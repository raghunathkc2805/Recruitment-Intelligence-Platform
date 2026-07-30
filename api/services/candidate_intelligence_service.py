from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.candidate_intelligence import CandidateIntelligence
from database.repositories.candidate_skill_repository import CandidateSkillRepository
from database.repositories.candidate_search_repository import CandidateSearchRepository


class CandidateIntelligenceService:


    @classmethod
    def rediscover(
        cls,
        db: Session,
        payload: dict,
    ):

        skills = payload.get(
            "skills",
            [],
        )

        repository = CandidateSearchRepository(
            db
        )

        candidates = repository.search(
            skills=skills,
            designation=payload.get(
                "designation"
            ),
            location=payload.get(
                "location"
            ),
        )

        results = []

        for candidate in candidates:

            results.append(
                {
                    "candidate_id": candidate.id,
                    "candidate_name": candidate.full_name,
                    "designation": candidate.current_designation,
                    "experience": candidate.experience_years,
                    "location": candidate.location,
                    "reason": "Matched historical candidate profile",
                }
            )

        return results


    @classmethod
    def rank_candidates(
        cls,
        candidates: list,
        job: dict,
    ):

        ranked = []

        for candidate in candidates:

            score = 0

            if candidate.get(
                "experience",
                0,
            ) >= job.get(
                "experience",
                0,
            ):
                score += 30


            if candidate.get(
                "location"
            ) == job.get(
                "location"
            ):
                score += 20


            ranked.append(
                {
                    **candidate,
                    "ai_score": score,
                    "explanation": {
                        "experience_match": True,
                        "location_match": True,
                    },
                }
            )


        return sorted(
            ranked,
            key=lambda x: x["ai_score"],
            reverse=True,
        )
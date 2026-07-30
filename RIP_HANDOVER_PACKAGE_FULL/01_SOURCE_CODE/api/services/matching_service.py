"""
Enterprise Matching Service
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from api.services.search_service import SearchService
from database.models.job_description import JobDescription
from database.models.job_skill import JobSkill
from database.repositories.candidate_skill_repository import CandidateSkillRepository
from matching_engine.matching_service import MatchingService as Engine


class MatchingService:

    @classmethod
    def run(
        cls,
        db: Session,
        payload: dict,
    ):

        if "job_id" in payload:

            job = (
                db.query(JobDescription)
                .filter(
                    JobDescription.id == payload["job_id"]
                )
                .first()
            )

            if job is None:
                raise ValueError(
                    "Job description not found"
                )

            query = (
                job.designation
                or job.job_code
                or ""
            )

            job_skills = [
                item.skill_name
                for item in db.query(JobSkill)
                .filter(
                    JobSkill.job_id == job.id
                )
                .all()
            ]

            job_payload = {
                "job_id": str(job.id),
                "designation": job.designation or "",
                "location": job.location or "",
                "experience_required": job.experience_required or 0,
                "skills": job_skills,
            }

        else:

            query = payload.get(
                "query",
                "",
            )

            job_payload = payload.get(
                "job",
                {},
            )

        candidates = SearchService.run(
            db,
            {
                "query": query,
            },
        )

        if isinstance(candidates, dict):
            candidates = candidates.get(
                "results",
                [],
            )

        matches = []

        for candidate in candidates:

            if isinstance(candidate, dict):
                candidate_data = candidate.copy()

            elif hasattr(candidate, "__dict__"):
                candidate_data = {
                    key: value
                    for key, value in candidate.__dict__.items()
                    if not key.startswith("_")
                }

            else:
                candidate_data = {
                    "id": str(candidate)
                }

            candidate_data["experience"] = {
                "years": float(
                    candidate_data.get(
                        "experience_years",
                        candidate_data.get(
                            "experience",
                            0
                        )
                        if isinstance(
                            candidate_data.get("experience"),
                            (int, float)
                        )
                        else 0
                    )
                )
            }

            candidate_skill_repo = CandidateSkillRepository(db)

            stored_skills = candidate_skill_repo.list_by_candidate(
                candidate_data.get("id")
                or candidate_data.get("candidate_id")
            )

            candidate_data["skills"] = [
                skill.skill_name
                for skill in stored_skills
            ]

            job_payload["experience"] = {
                "years": float(
                    job_payload.get(
                        "experience_required",
                        0
                    )
                )
            }

            job_payload["skills"] = job_payload.get(
                "skills",
                []
            ) or []

            score = Engine.match(
                candidate_data,
                job_payload,
            )

            matches.append(
                {
                    "candidate": candidate_data,
                    "score": score,
                }
            )

        return matches

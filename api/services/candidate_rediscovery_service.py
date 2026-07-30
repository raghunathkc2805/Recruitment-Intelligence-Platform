from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.candidate import Candidate
from database.models.candidate_skill import CandidateSkill


class CandidateRediscoveryService:


    @classmethod
    def search(
        cls,
        db: Session,
        skills: list[str],
        limit: int = 20,
    ):

        skill_set = {
            skill.lower()
            for skill in skills
        }


        candidates = (
            db.query(Candidate)
            .limit(limit * 5)
            .all()
        )


        results = []


        for candidate in candidates:

            candidate_skills = {
                skill.skill_name.lower()
                for skill in candidate.skills
            }


            matched = (
                skill_set
                &
                candidate_skills
            )


            score = 0

            if skill_set:

                score = round(
                    (
                        len(matched)
                        /
                        len(skill_set)
                    )
                    *
                    100,
                    2,
                )


            if score > 0:

                results.append(
                    {
                        "candidate_id": candidate.id,
                        "candidate_name": candidate.name,
                        "matched_skills":
                            list(matched),
                        "rediscovery_score": score,
                    }
                )


        return sorted(
            results,
            key=lambda x: x["rediscovery_score"],
            reverse=True,
        )[:limit]
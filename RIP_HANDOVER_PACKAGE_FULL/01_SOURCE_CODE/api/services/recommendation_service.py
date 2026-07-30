"""
Enterprise Recommendation Service
"""

from __future__ import annotations

from database.models.match_result import MatchResult

from api.services.recommendation_engine import RecommendationEngine

from database.repositories.candidate_repository import CandidateRepository
from database.repositories.candidate_skill_repository import CandidateSkillRepository
from database.repositories.job_skill_repository import JobSkillRepository
from database.repositories.match_result_repository import MatchResultRepository


class RecommendationService:

    @classmethod
    def recommend(
        cls,
        db,
        job,
        limit: int = 10,
        persist: bool = True,
    ):

        candidate_repository = CandidateRepository(db)
        candidate_skill_repository = CandidateSkillRepository(db)
        job_skill_repository = JobSkillRepository(db)
        match_repository = MatchResultRepository(db)

        job_skills = job_skill_repository.list_by_job(
            job.id
        )

        required_skills = {
            skill.skill_name.lower()
            for skill in job_skills
        }

        recommendations = []

        for candidate in candidate_repository.list():

            candidate_skills = {
                skill.skill_name.lower()
                for skill in candidate_skill_repository.list_by_candidate(
                    candidate.id
                )
            }

            matched = candidate_skills.intersection(
                required_skills
            )

            result = RecommendationEngine.calculate(
                matched_skills=len(matched),
                total_required_skills=len(required_skills),
                experience_match=1.0,
                designation_match=True,
                certification_match=1.0,
                location_match=True,
            )

            if result.final_score >= 90:
                recommendation = "Strong"
            elif result.final_score >= 75:
                recommendation = "Good"
            elif result.final_score >= 60:
                recommendation = "Moderate"
            else:
                recommendation = "Weak"

            if persist:

                existing = None

                for row in match_repository.list_by_job(
                    job.id
                ):
                    if row.candidate_id == candidate.id:
                        existing = row
                        break

                if existing is None:

                    match_repository.create(
                        MatchResult(
                            candidate_id=candidate.id,
                            job_id=job.id,
                            score=result.final_score,
                            recommendation=recommendation,
                        )
                    )

            recommendations.append(
                {
                    "candidate_id": candidate.id,
                    "candidate_code": candidate.candidate_code,
                    "candidate_name": candidate.full_name,
                    "designation": candidate.current_designation,
                    "experience": candidate.experience_years,
                    "score": result.final_score,
                    "recommendation": recommendation,
                    "matched_skills": sorted(matched),
                    "missing_skills": sorted(
                        required_skills - matched
                    ),
                    "explanation": {
                        "skills": f"{len(matched)}/{len(required_skills)}",
                        "experience": result.experience_score,
                        "designation": result.designation_score,
                        "certification": result.certification_score,
                        "location": result.location_score,
                    },
                }
            )

        db.commit()

        recommendations.sort(
            key=lambda row: row["score"],
            reverse=True,
        )

        return recommendations[:limit]

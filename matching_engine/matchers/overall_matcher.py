"""
Recruitment Intelligence Platform
Overall Matcher
"""

from __future__ import annotations

from matching_engine.matchers.certification_matcher import (
    CertificationMatcher,
)
from matching_engine.matchers.designation_matcher import (
    DesignationMatcher,
)
from matching_engine.matchers.education_matcher import (
    EducationMatcher,
)
from matching_engine.matchers.experience_matcher import (
    ExperienceMatcher,
)
from matching_engine.matchers.location_matcher import (
    LocationMatcher,
)
from matching_engine.matchers.skill_matcher import (
    SkillMatcher,
)
from matching_engine.constants import DEFAULT_WEIGHTS


class OverallMatcher:
    """
    Executes all matching engines.
    """

    @classmethod
    def match(
        cls,
        candidate: dict,
        job: dict,
    ) -> dict:

        skill_match = SkillMatcher.match(
            candidate.get("skills", []),
            job.get("skills", []),
        )

        candidate_experience = candidate.get(
            "experience",
            0,
        )

        if isinstance(candidate_experience, dict):
            experience_payload = candidate_experience
        else:
            experience_payload = {
                "years": float(candidate_experience or 0)
            }

        job_experience = job.get(
            "experience",
            job.get(
                "experience_required",
                0
            ),
        )

        if isinstance(job_experience, dict):
            required_years = job_experience.get(
                "years",
                0
            )
        else:
            required_years = float(
                job_experience or 0
            )

        experience_match = ExperienceMatcher.match(
            experience_payload,
            required_years,
        )

        education_match = EducationMatcher.match(
            candidate.get("education", []),
            job.get("education", []),
        )

        designation_match = DesignationMatcher.match(
            candidate.get("designations", []),
            job.get("designations", []),
        )

        location_match = LocationMatcher.match(
            candidate.get("locations", []),
            job.get("locations", []),
        )

        certification_match = CertificationMatcher.match(
            candidate.get("certifications", []),
            job.get("certifications", []),
        )

        weighted_score = (
            skill_match["score"] * DEFAULT_WEIGHTS["skills"]
            +
            experience_match["score"] * DEFAULT_WEIGHTS["experience"]
            +
            education_match["score"] * DEFAULT_WEIGHTS["education"]
            +
            designation_match["score"] * DEFAULT_WEIGHTS["designation"]
            +
            location_match["score"] * DEFAULT_WEIGHTS["location"]
            +
            certification_match["score"] * DEFAULT_WEIGHTS["certification"]
        )

        overall_score = round(
            weighted_score / 100,
            2,
        )

        return {
            "overall_score": overall_score,
            "skill_match": skill_match,
            "experience_match": experience_match,
            "education_match": education_match,
            "designation_match": designation_match,
            "location_match": location_match,
            "certification_match": certification_match,
        }
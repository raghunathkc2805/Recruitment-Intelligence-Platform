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

        experience_match = ExperienceMatcher.match(
            candidate.get("experience"),
            job.get("experience", 0),
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

        scores = [
            skill_match["score"],
            experience_match["score"],
            education_match["score"],
            designation_match["score"],
            location_match["score"],
            certification_match["score"],
        ]

        overall_score = round(
            sum(scores) / len(scores),
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
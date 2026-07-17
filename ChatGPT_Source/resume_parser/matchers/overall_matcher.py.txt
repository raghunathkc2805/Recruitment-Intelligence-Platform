"""
Recruitment Intelligence Platform
Overall Matcher
"""

from __future__ import annotations

from resume_parser.matchers.certification_matcher import (
    CertificationMatcher,
)
from resume_parser.matchers.designation_matcher import (
    DesignationMatcher,
)
from resume_parser.matchers.education_matcher import (
    EducationMatcher,
)
from resume_parser.matchers.experience_matcher import (
    ExperienceMatcher,
)
from resume_parser.matchers.location_matcher import (
    LocationMatcher,
)
from resume_parser.matchers.skill_matcher import (
    SkillMatcher,
)


class OverallMatcher:
    """
    Aggregates all matcher scores into a single result.
    """

    @classmethod
    def match(
        cls,
        candidate: dict,
        requirements: dict,
    ) -> dict:

        skills = SkillMatcher.match(
            candidate.get("skills", []),
            requirements.get("skills", []),
        )

        experience = ExperienceMatcher.match(
            candidate.get("experience"),
            requirements.get("experience", 0),
        )

        education = EducationMatcher.match(
            candidate.get("education", []),
            requirements.get("education", []),
        )

        designation = DesignationMatcher.match(
            candidate.get("designations", []),
            requirements.get("designations", []),
        )

        location = LocationMatcher.match(
            candidate.get("locations", []),
            requirements.get("locations", []),
        )

        certification = CertificationMatcher.match(
            candidate.get("certifications", []),
            requirements.get("certifications", []),
        )

        scores = [
            skills["score"],
            experience["score"],
            education["score"],
            designation["score"],
            location["score"],
            certification["score"],
        ]

        overall_score = round(
            sum(scores) / len(scores),
            2,
        )

        return {
            "overall_score": overall_score,
            "skill_match": skills,
            "experience_match": experience,
            "education_match": education,
            "designation_match": designation,
            "location_match": location,
            "certification_match": certification,
        }
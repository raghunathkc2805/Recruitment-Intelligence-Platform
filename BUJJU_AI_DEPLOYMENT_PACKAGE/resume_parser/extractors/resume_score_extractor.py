"""
Recruitment Intelligence Platform
Resume Score Extractor
"""

from __future__ import annotations


class ResumeScoreExtractor:
    """
    Calculates a simple resume completeness score.
    """

    WEIGHTS = {
        "name": 10,
        "email": 10,
        "phone": 10,
        "summary": 10,
        "experience": 20,
        "education": 15,
        "skills": 15,
        "projects": 5,
        "certifications": 5,
    }

    @classmethod
    def extract(cls, candidate: dict) -> dict:

        score = 0

        if candidate.get("name"):
            score += cls.WEIGHTS["name"]

        if candidate.get("email"):
            score += cls.WEIGHTS["email"]

        if candidate.get("phone"):
            score += cls.WEIGHTS["phone"]

        if candidate.get("summary"):
            score += cls.WEIGHTS["summary"]

        if candidate.get("experience"):
            score += cls.WEIGHTS["experience"]

        if candidate.get("education"):
            score += cls.WEIGHTS["education"]

        skills = candidate.get("skills", {})

        if (
            skills.get("technical_skills")
            or skills.get("functional_skills")
            or skills.get("soft_skills")
        ):
            score += cls.WEIGHTS["skills"]

        if candidate.get("projects"):
            score += cls.WEIGHTS["projects"]

        if candidate.get("certifications"):
            score += cls.WEIGHTS["certifications"]

        return {
            "resume_score": score,
            "grade": (
                "A" if score >= 90
                else "B" if score >= 75
                else "C" if score >= 60
                else "D"
            ),
        }
"""
Recruitment Intelligence Platform
Skill Matcher
"""

from __future__ import annotations


class SkillMatcher:
    """
    Matches candidate skills with job skills.
    """

    @staticmethod
    def match(
        candidate_skills: list[str],
        required_skills: list[str],
    ) -> dict:

        candidate = {
            skill.strip().lower()
            for skill in candidate_skills
            if skill
        }

        required = {
            skill.strip().lower()
            for skill in required_skills
            if skill
        }

        matched = sorted(candidate & required)

        missing = sorted(required - candidate)

        additional = sorted(candidate - required)

        score = (
            round(
                (len(matched) / len(required)) * 100,
                2,
            )
            if required
            else 100.0
        )

        return {
            "matched": matched,
            "missing": missing,
            "additional": additional,
            "matched_count": len(matched),
            "candidate_count": len(candidate),
            "required_count": len(required),
            "score": score,
        }
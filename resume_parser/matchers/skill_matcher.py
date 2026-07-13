"""
Recruitment Intelligence Platform
Skill Matcher
"""

from __future__ import annotations


class SkillMatcher:
    """
    Match candidate skills against required skills.
    """

    @staticmethod
    def match(
        candidate_skills: list[str],
        required_skills: list[str],
    ) -> dict:

        candidate = {
            skill.lower().strip()
            for skill in candidate_skills
            if skill
        }

        required = {
            skill.lower().strip()
            for skill in required_skills
            if skill
        }

        matched = sorted(candidate & required)

        missing = sorted(required - candidate)

        score = (
            round(len(matched) / len(required) * 100, 2)
            if required
            else 100.0
        )

        return {
            "matched": matched,
            "missing": missing,
            "matched_count": len(matched),
            "required_count": len(required),
            "score": score,
        }
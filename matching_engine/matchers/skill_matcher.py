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

        skill_aliases = {
            "documentation": {
                "document",
                "documentation",
                "reporting",
                "technical documentation",
                "report preparation",
            },
        }

        normalized_candidate = set(candidate)
        normalized_required = set(required)

        for key, aliases in skill_aliases.items():
            if normalized_required.intersection(aliases):
                normalized_required.add(key)

            if normalized_candidate.intersection(aliases):
                normalized_candidate.add(key)

        matched = sorted(
            normalized_candidate & normalized_required
        )

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
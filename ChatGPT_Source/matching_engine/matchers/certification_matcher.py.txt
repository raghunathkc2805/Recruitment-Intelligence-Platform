"""
Recruitment Intelligence Platform
Certification Matcher
"""

from __future__ import annotations


class CertificationMatcher:
    """
    Matches candidate certifications with required certifications.
    """

    @staticmethod
    def match(
        candidate_certifications: list[dict],
        required_certifications: list[str],
    ) -> dict:

        candidate = {
            item.get("certification", "").strip().lower()
            for item in candidate_certifications
            if item.get("certification")
        }

        required = {
            item.strip().lower()
            for item in required_certifications
            if item
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
            "required_count": len(required),
            "candidate_count": len(candidate),
            "score": score,
        }
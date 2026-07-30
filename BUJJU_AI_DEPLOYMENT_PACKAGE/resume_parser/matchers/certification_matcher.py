"""
Recruitment Intelligence Platform
Certification Matcher
"""

from __future__ import annotations


class CertificationMatcher:
    """
    Match candidate certifications against required certifications.
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
            certification.strip().lower()
            for certification in required_certifications
            if certification
        }

        matched = sorted(candidate & required)

        missing = sorted(required - candidate)

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
            "matched_count": len(matched),
            "required_count": len(required),
            "score": score,
        }
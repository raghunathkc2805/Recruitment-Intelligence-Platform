"""
Recruitment Intelligence Platform
Candidate Match Extractor
"""

from __future__ import annotations

from resume_parser.matchers.overall_matcher import OverallMatcher


class CandidateMatchExtractor:
    """
    Performs complete candidate matching against
    job requirements.
    """

    @classmethod
    def extract(
        cls,
        candidate: dict,
        requirements: dict,
    ) -> dict:

        match_result = OverallMatcher.match(
            candidate,
            requirements,
        )

        return {
            "candidate": candidate,
            "requirements": requirements,
            "match_result": match_result,
            "overall_score": match_result["overall_score"],
        }
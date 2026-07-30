"""
Match Explanation Service
"""

from __future__ import annotations


class MatchExplainer:

    @staticmethod
    def explain(
        candidate,
        match_result,
    ) -> dict:

        return {

            "overall_score": match_result.get(
                "score",
                0,
            ),

            "skills_score": match_result.get(
                "skills_score",
                0,
            ),

            "experience_score": match_result.get(
                "experience_score",
                0,
            ),

            "education_score": match_result.get(
                "education_score",
                0,
            ),

            "location_score": match_result.get(
                "location_score",
                0,
            ),

            "strengths": match_result.get(
                "strengths",
                [],
            ),

            "gaps": match_result.get(
                "gaps",
                [],
            ),

            "recommendation": match_result.get(
                "recommendation",
                "",
            ),

            "candidate": {

                "candidate_id": candidate.id,

                "candidate_code": candidate.candidate_code,

                "name": candidate.full_name,

                "designation": candidate.current_designation,

                "location": candidate.location,

            },

        }

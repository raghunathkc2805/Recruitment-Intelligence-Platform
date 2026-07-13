"""
Recruitment Intelligence Platform
Candidate Match Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class CandidateMatch:
    """
    Represents the matching outcome for a single candidate.
    """

    candidate_id: str = ""
    candidate_name: str = ""

    overall_score: float = 0.0

    recommendation: str = ""

    priority: str = ""

    match_result: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:

        return {
            "candidate_id": self.candidate_id,
            "candidate_name": self.candidate_name,
            "overall_score": self.overall_score,
            "recommendation": self.recommendation,
            "priority": self.priority,
            "match_result": self.match_result,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "CandidateMatch":

        return cls(
            candidate_id=data.get("candidate_id", ""),
            candidate_name=data.get("candidate_name", ""),
            overall_score=float(
                data.get("overall_score", 0)
            ),
            recommendation=data.get(
                "recommendation",
                "",
            ),
            priority=data.get(
                "priority",
                "",
            ),
            match_result=data.get(
                "match_result",
                {},
            ),
            metadata=data.get(
                "metadata",
                {},
            ),
        )
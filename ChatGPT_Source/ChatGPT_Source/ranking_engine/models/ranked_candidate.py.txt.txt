"""
Recruitment Intelligence Platform
Ranked Candidate Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class RankedCandidate:
    """
    Represents a ranked candidate.
    """

    candidate_id: str = ""

    candidate_name: str = ""

    rank: int = 0

    overall_score: float = 0.0

    recommendation: str = ""

    priority: str = ""

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        return {
            "candidate_id": self.candidate_id,
            "candidate_name": self.candidate_name,
            "rank": self.rank,
            "overall_score": self.overall_score,
            "recommendation": self.recommendation,
            "priority": self.priority,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "RankedCandidate":

        return cls(
            candidate_id=data.get(
                "candidate_id",
                "",
            ),
            candidate_name=data.get(
                "candidate_name",
                "",
            ),
            rank=int(data.get("rank", 0)),
            overall_score=float(
                data.get(
                    "overall_score",
                    0,
                )
            ),
            recommendation=data.get(
                "recommendation",
                "",
            ),
            priority=data.get(
                "priority",
                "",
            ),
            metadata=data.get(
                "metadata",
                {},
            ),
        )
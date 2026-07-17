"""
Recruitment Intelligence Platform
Ranking Result Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class RankingResult:
    """
    Complete ranking result.
    """

    ranked_candidates: list[dict] = field(
        default_factory=list
    )

    total_candidates: int = 0

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        return {
            "ranked_candidates": self.ranked_candidates,
            "total_candidates": self.total_candidates,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "RankingResult":

        return cls(
            ranked_candidates=data.get(
                "ranked_candidates",
                [],
            ),
            total_candidates=int(
                data.get(
                    "total_candidates",
                    0,
                )
            ),
            metadata=data.get(
                "metadata",
                {},
            ),
        )
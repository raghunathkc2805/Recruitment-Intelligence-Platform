"""
Recruitment Intelligence Platform
Matching Result Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class MatchingResult:
    """
    Represents the complete matching result between
    a candidate and a job.
    """

    overall_score: float = 0.0

    recommendation: str = ""

    priority: str = ""

    skill_match: dict[str, Any] = field(default_factory=dict)

    experience_match: dict[str, Any] = field(default_factory=dict)

    education_match: dict[str, Any] = field(default_factory=dict)

    designation_match: dict[str, Any] = field(default_factory=dict)

    location_match: dict[str, Any] = field(default_factory=dict)

    certification_match: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:

        return {
            "overall_score": self.overall_score,
            "recommendation": self.recommendation,
            "priority": self.priority,
            "skill_match": self.skill_match,
            "experience_match": self.experience_match,
            "education_match": self.education_match,
            "designation_match": self.designation_match,
            "location_match": self.location_match,
            "certification_match": self.certification_match,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "MatchingResult":

        return cls(
            overall_score=float(data.get("overall_score", 0.0)),
            recommendation=data.get("recommendation", ""),
            priority=data.get("priority", ""),
            skill_match=data.get("skill_match", {}),
            experience_match=data.get("experience_match", {}),
            education_match=data.get("education_match", {}),
            designation_match=data.get("designation_match", {}),
            location_match=data.get("location_match", {}),
            certification_match=data.get("certification_match", {}),
            metadata=data.get("metadata", {}),
        )
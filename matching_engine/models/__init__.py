"""
Recruitment Intelligence Platform
Job Requirement Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class JobRequirement:
    """
    Represents a normalized Job Requirement.
    """

    job_id: str = ""

    job_title: str = ""

    skills: list[str] = field(default_factory=list)

    experience: float = 0.0

    education: list[str] = field(default_factory=list)

    designations: list[str] = field(default_factory=list)

    locations: list[str] = field(default_factory=list)

    certifications: list[str] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:

        return {
            "job_id": self.job_id,
            "job_title": self.job_title,
            "skills": self.skills,
            "experience": self.experience,
            "education": self.education,
            "designations": self.designations,
            "locations": self.locations,
            "certifications": self.certifications,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "JobRequirement":

        return cls(
            job_id=data.get("job_id", ""),
            job_title=data.get("job_title", ""),
            skills=list(data.get("skills", [])),
            experience=float(
                data.get("experience", 0)
            ),
            education=list(
                data.get("education", [])
            ),
            designations=list(
                data.get("designations", [])
            ),
            locations=list(
                data.get("locations", [])
            ),
            certifications=list(
                data.get("certifications", [])
            ),
            metadata=data.get("metadata", {}),
        )
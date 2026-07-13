"""
Recruitment Intelligence Platform
Project Model
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Project:
    """
    Represents a candidate project.
    """

    project_name: str | None = None
    client: str | None = None
    role: str | None = None
    duration: str | None = None
    technologies: list[str] = field(default_factory=list)
    description: str | None = None
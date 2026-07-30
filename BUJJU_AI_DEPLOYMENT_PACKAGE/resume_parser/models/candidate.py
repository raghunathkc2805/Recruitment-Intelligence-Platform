"""
Recruitment Intelligence Platform
Candidate Model
"""

from __future__ import annotations

from dataclasses import dataclass, field

from resume_parser.models.certification import Certification
from resume_parser.models.education import Education
from resume_parser.models.employment import Employment
from resume_parser.models.project import Project
from resume_parser.models.skill import Skill


@dataclass(slots=True)
class Candidate:
    """
    Represents a parsed candidate profile.
    """

    name: str | None = None
    email: str | None = None
    phone: str | None = None
    summary: str | None = None

    total_experience: dict | None = None

    education: list[Education] = field(default_factory=list)

    employment: list[Employment] = field(default_factory=list)

    skills: list[Skill] = field(default_factory=list)

    certifications: list[Certification] = field(default_factory=list)

    projects: list[Project] = field(default_factory=list)

    languages: list[dict] = field(default_factory=list)

    locations: list[dict] = field(default_factory=list)

    employers: list[dict] = field(default_factory=list)
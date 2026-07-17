"""
Recruitment Intelligence Platform
Resume Model
"""

from __future__ import annotations

from dataclasses import dataclass, field

from resume_parser.models.candidate import Candidate


@dataclass(slots=True)
class Resume:
    """
    Represents a parsed resume.
    """

    file_name: str
    file_type: str
    file_size: int
    page_count: int | None

    success: bool = True
    status: str = "success"

    metadata: dict = field(default_factory=dict)

    errors: list[str] = field(default_factory=list)

    raw_text: str = ""

    candidate: Candidate = field(default_factory=Candidate)
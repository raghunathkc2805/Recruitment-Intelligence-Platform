"""
Recruitment Intelligence Platform
Education Model
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Education:
    """
    Represents an education record.
    """

    degree: str
    institution: str | None = None
    specialization: str | None = None
    year: str | None = None
    percentage: str | None = None
    cgpa: str | None = None
    text: str | None = None
"""
Recruitment Intelligence Platform
Employment Model
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Employment:
    """
    Represents an employment record.
    """

    company: str
    designation: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    duration: str | None = None
    location: str | None = None
    employment_type: str | None = None
    description: str | None = None
"""
Recruitment Intelligence Platform
Certification Model
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Certification:
    """
    Represents a candidate certification.
    """

    name: str
    issuer: str | None = None
    year: str | None = None
    credential_id: str | None = None
    confidence: float = 100.0
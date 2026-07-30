"""
Recruitment Intelligence Platform
Skill Model
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Skill:
    """
    Represents a candidate skill.
    """

    name: str
    category: str
    confidence: float = 100.0
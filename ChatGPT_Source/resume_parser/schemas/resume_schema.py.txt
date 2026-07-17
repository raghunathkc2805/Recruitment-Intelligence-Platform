"""
Recruitment Intelligence Platform
Resume Response Schema
"""

from __future__ import annotations

from typing import TypedDict


class ExperienceSchema(TypedDict, total=False):
    text: str
    years: float
    months: int
    total_months: int


class ResumeSchema(TypedDict):

    success: bool
    status: str

    file_name: str
    file_type: str
    file_size: int
    pages: int | None

    metadata: dict
    errors: list[str]

    text: str

    candidate: dict
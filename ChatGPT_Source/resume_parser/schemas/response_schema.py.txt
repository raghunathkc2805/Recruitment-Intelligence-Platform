"""
Recruitment Intelligence Platform
Response Schema
"""

from __future__ import annotations

from typing import TypedDict

from resume_parser.schemas.resume_schema import ResumeSchema


class ResponseSchema(TypedDict):
    """
    Standard response returned by the Resume Parser.
    """

    success: bool

    message: str

    data: ResumeSchema
"""
Candidate API Schemas
"""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr


class CandidateCreateRequest(BaseModel):

    candidate_code: str
    full_name: str
    email: EmailStr

    mobile: str = ""
    location: str = ""
    experience_years: float = 0.0
    current_designation: str = ""


class CandidateResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    candidate_code: str
    full_name: str
    email: EmailStr

    mobile: str
    location: str
    experience_years: float
    current_designation: str
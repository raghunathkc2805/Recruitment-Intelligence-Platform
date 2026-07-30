"""
Candidate API Schemas
"""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field


class CandidateCreateRequest(BaseModel):

    candidate_code: str = Field(min_length=1, max_length=50)

    full_name: str = Field(min_length=2, max_length=200)

    email: EmailStr

    mobile: str = Field(default="", max_length=20)

    location: str = Field(default="", max_length=200)

    experience_years: float = Field(
        default=0.0,
        ge=0,
        le=60,
    )

    current_designation: str = Field(
        default="",
        max_length=200,
    )


class CandidateUpdateRequest(BaseModel):

    full_name: str | None = None

    mobile: str | None = None

    location: str | None = None

    experience_years: float | None = Field(
        default=None,
        ge=0,
        le=60,
    )

    current_designation: str | None = None


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
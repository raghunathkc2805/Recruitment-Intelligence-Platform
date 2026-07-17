"""
Recruitment Intelligence Platform
Resume Validator
"""

from __future__ import annotations

from resume_parser.utils.constants import MIN_TEXT_LENGTH
from resume_parser.validators.education_validator import (
    EducationValidator,
)
from resume_parser.validators.email_validator import (
    EmailValidator,
)
from resume_parser.validators.experience_validator import (
    ExperienceValidator,
)
from resume_parser.validators.phone_validator import (
    PhoneValidator,
)


class ResumeValidator:
    """
    Validate parsed resume output.
    """

    @classmethod
    def validate(cls, result: dict) -> dict:

        candidate = result.get("candidate", {})

        text = result.get("text", "")

        return {

            "valid": (

                len(text) >= MIN_TEXT_LENGTH

                and EmailValidator.validate(
                    candidate.get("email")
                )

                and PhoneValidator.validate(
                    candidate.get("phone")
                )

            ),

            "checks": {

                "minimum_text": len(text) >= MIN_TEXT_LENGTH,

                "email": EmailValidator.validate(
                    candidate.get("email")
                ),

                "phone": PhoneValidator.validate(
                    candidate.get("phone")
                ),

                "experience": ExperienceValidator.validate(
                    candidate.get("experience")
                ),

                "education": EducationValidator.validate(
                    candidate.get("education")
                ),

            },

        }
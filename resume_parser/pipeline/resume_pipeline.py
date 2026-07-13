"""
Recruitment Intelligence Platform
resume_parser/pipeline/resume_pipeline.py
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from resume_parser.extractors.certification_extractor import (
    CertificationExtractor,
)
from resume_parser.extractors.education_extractor import (
    EducationExtractor,
)
from resume_parser.extractors.email_extractor import (
    EmailExtractor,
)
from resume_parser.extractors.employer_extractor import (
    EmployerExtractor,
)
from resume_parser.extractors.experience_extractor import (
    ExperienceExtractor,
)
from resume_parser.extractors.languages_extractor import (
    LanguageExtractor,
)
from resume_parser.extractors.location_extractor import (
    LocationExtractor,
)
from resume_parser.extractors.name_extractor import (
    NameExtractor,
)
from resume_parser.extractors.phone_extractor import (
    PhoneExtractor,
)
from resume_parser.extractors.project_extractor import (
    ProjectExtractor,
)
from resume_parser.extractors.skills_extractor import (
    SkillsExtractor,
)
from resume_parser.extractors.summary_extractor import (
    SummaryExtractor,
)
from resume_parser.parsers.parser_factory import ParserFactory
from resume_parser.utils.constants import (
    KEY_ERRORS,
    KEY_FILE_NAME,
    KEY_FILE_SIZE,
    KEY_FILE_TYPE,
    KEY_METADATA,
    KEY_PAGE_COUNT,
    KEY_STATUS,
    KEY_SUCCESS,
    KEY_TEXT,
)


class ResumePipeline:
    """
    Production Resume Processing Pipeline.
    """

    @staticmethod
    def _safe(callable_obj, *args, default=None):

        try:
            return callable_obj(*args)
        except Exception:
            return default

    @classmethod
    def process(cls, file_path: str | Path) -> dict[str, Any]:

        parser = ParserFactory.get_parser(file_path)

        parsed = parser.parse(file_path)

        text = parsed.get(KEY_TEXT, "")

        return {

            KEY_SUCCESS: parsed.get(KEY_SUCCESS, True),

            KEY_STATUS: parsed.get(KEY_STATUS),

            KEY_FILE_NAME: parsed.get(KEY_FILE_NAME),

            KEY_FILE_TYPE: parsed.get(KEY_FILE_TYPE),

            KEY_FILE_SIZE: parsed.get(KEY_FILE_SIZE),

            KEY_PAGE_COUNT: parsed.get(KEY_PAGE_COUNT),

            KEY_METADATA: parsed.get(KEY_METADATA, {}),

            KEY_ERRORS: parsed.get(KEY_ERRORS, []),

            KEY_TEXT: text,

            "candidate": {

                "name": cls._safe(
                    NameExtractor.extract,
                    text,
                ),

                "email": cls._safe(
                    EmailExtractor.extract,
                    text,
                ),

                "phone": cls._safe(
                    PhoneExtractor.extract,
                    text,
                ),

                "summary": cls._safe(
                    SummaryExtractor.extract,
                    text,
                ),

                "experience": cls._safe(
                    ExperienceExtractor.extract,
                    text,
                ),

                "education": cls._safe(
                    EducationExtractor.extract,
                    text,
                    default=[],
                ),

                "skills": cls._safe(
                    SkillsExtractor.extract,
                    text,
                    default={},
                ),

                "locations": cls._safe(
                    LocationExtractor.extract,
                    text,
                    default=[],
                ),

                "employers": cls._safe(
                    EmployerExtractor.extract,
                    text,
                    default=[],
                ),

                "certifications": cls._safe(
                    CertificationExtractor.extract,
                    text,
                    default=[],
                ),

                "languages": cls._safe(
                    LanguageExtractor.extract,
                    text,
                    default=[],
                ),

                "projects": cls._safe(
                    ProjectExtractor.extract,
                    text,
                    default=[],
                ),
            },
        }

    @classmethod
    def parse(cls, file_path: str | Path) -> dict[str, Any]:
        return cls.process(file_path)
"""
Recruitment Intelligence Platform
resume_parser/resume_service.py
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from resume_parser.pipeline.resume_pipeline import ResumePipeline


class ResumeService:
    """
    High-level service wrapper for the Resume Pipeline.
    """

    @staticmethod
    def parse(file_path: str | Path) -> dict[str, Any]:
        return ResumePipeline.process(file_path)

    @staticmethod
    def parse_resume(file_path: str | Path) -> dict[str, Any]:
        return ResumePipeline.process(file_path)

    @staticmethod
    def process(file_path: str | Path) -> dict[str, Any]:
        return ResumePipeline.process(file_path)
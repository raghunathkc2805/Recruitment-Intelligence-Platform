"""
Recruitment Intelligence Platform
Storage Manager
"""

from __future__ import annotations

import shutil
import uuid
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

STORAGE_ROOT = PROJECT_ROOT / "storage"

RESUME_ROOT = STORAGE_ROOT / "resumes"

JD_ROOT = STORAGE_ROOT / "job_descriptions"

TEMP_ROOT = STORAGE_ROOT / "temp"

EXPORT_ROOT = STORAGE_ROOT / "exports"

ARCHIVE_ROOT = STORAGE_ROOT / "archive"


class StorageManager:

    @staticmethod
    def initialize() -> None:

        for folder in (
            STORAGE_ROOT,
            RESUME_ROOT,
            JD_ROOT,
            TEMP_ROOT,
            EXPORT_ROOT,
            ARCHIVE_ROOT,
        ):
            folder.mkdir(
                parents=True,
                exist_ok=True,
            )

    @staticmethod
    def save_resume(
        source_file: str | Path,
        original_filename: str,
    ) -> Path:

        StorageManager.initialize()

        today = datetime.now()

        resume_id = f"RES-{uuid.uuid4().hex[:12].upper()}"

        destination = (
            RESUME_ROOT
            / str(today.year)
            / f"{today.month:02}"
            / resume_id
            / "V1"
        )

        destination.mkdir(
            parents=True,
            exist_ok=True,
        )

        target = destination / original_filename

        shutil.copy2(
            source_file,
            target,
        )

        return target

    @staticmethod
    def save_jd(
        source_file: str | Path,
        original_filename: str,
    ) -> Path:

        StorageManager.initialize()

        today = datetime.now()

        jd_id = f"JD-{uuid.uuid4().hex[:12].upper()}"

        destination = (
            JD_ROOT
            / str(today.year)
            / f"{today.month:02}"
            / jd_id
        )

        destination.mkdir(
            parents=True,
            exist_ok=True,
        )

        target = destination / original_filename

        shutil.copy2(
            source_file,
            target,
        )

        return target

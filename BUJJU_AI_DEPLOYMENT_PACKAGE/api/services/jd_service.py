"""
JD Service
"""

from __future__ import annotations

import logging

from pathlib import Path
from tempfile import NamedTemporaryFile

from sqlalchemy.orm import Session

from api.storage.storage_manager import StorageManager

from database.models.job_description import JobDescription

from database.repositories.job_repository import JobRepository
from database.repositories.job_skill_repository import JobSkillRepository

from jd_parser.services.jd_service import JDService as Parser


logger = logging.getLogger(__name__)


class JDService:

    PARSER_VERSION = "1.0"

    @classmethod
    def parse(
        cls,
        db: Session,
        upload_file,
    ):

        temp_file: Path | None = None
        stored: Path | None = None

        try:

            suffix = Path(
                upload_file.filename
            ).suffix

            with NamedTemporaryFile(
                delete=False,
                suffix=suffix,
            ) as tmp:

                tmp.write(
                    upload_file.file.read()
                )

                temp_file = Path(
                    tmp.name
                )

            stored = StorageManager.save_jd(

                temp_file,

                upload_file.filename,

            )

            parsed = Parser.parse(
                stored
            )

            job = JobRepository(
                db
            ).create(

                JobDescription(

                    job_code=parsed.get(
                        "job_code",
                        "",
                    ),

                    designation=parsed.get(
                        "designation",
                        "",
                    ),

                    location=parsed.get(
                        "location",
                        "",
                    ),

                    experience_required=float(
                        parsed.get(
                            "experience_required",
                            0,
                        )
                    ),

                )

            )

            repository = JobSkillRepository(
                db
            )

            for skill in parsed.get(
                "skills",
                [],
            ):

                if isinstance(
                    skill,
                    str,
                ):

                    repository.create(

                        job.id,

                        skill,

                    )

            db.commit()

            db.refresh(
                job
            )

            return {

                "job_id": job.id,

                "job_code": job.job_code,

                "skills_saved": len(

                    parsed.get(
                        "skills",
                        [],
                    )

                ),

                "parsed_data": parsed,

            }

        except Exception:

            db.rollback()

            logger.exception(
                "JD upload transaction failed."
            )

            if (
                stored is not None
                and stored.exists()
            ):

                try:

                    stored.unlink()

                except Exception:

                    logger.exception(
                        "Unable to remove stored JD."
                    )

            raise

        finally:

            if (
                temp_file is not None
                and temp_file.exists()
            ):

                try:

                    temp_file.unlink()

                except Exception:

                    logger.exception(
                        "Unable to remove temporary JD."
                    )

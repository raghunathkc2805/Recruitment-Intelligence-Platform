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
from jd_parser.core.docx_reader import extract_docx_text



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

            parser = Parser()

            if stored.suffix.lower() == ".docx":
                text = extract_docx_text(stored)
            else:
                text = stored.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

            parsed = parser.parse(
                text=text,
                jd_file=stored,
                parser_version=cls.PARSER_VERSION,
            )

            if hasattr(parsed, "__dict__"):
                parsed_data = parsed.__dict__
            else:
                parsed_data = parsed

            job = JobRepository(
                db
            ).create(

                JobDescription(

                    job_code=parsed_data.get(
                        "job_code",
                        "",
                    ) or f"JD-{__import__('uuid').uuid4().hex[:8].upper()}",

                    designation=parsed_data.get(
                        "designation",
                        parsed_data.get(
                            "title",
                            "",
                        ),
                    ),

                    location=parsed_data.get(
                        "location",
                        "",
                    ),

                    experience_required=float(
                        parsed_data.get(
                            "experience_required",
                            parsed_data.get(
                                "minimum_experience",
                                0,
                            ),
                        )
                        or 0
                    ),

                )

            )

            repository = JobSkillRepository(
                db
            )

            extracted_skills = []

            for key in [
                "skills",
                "technical_skills",
                "functional_skills",
                "soft_skills",
                "certifications",
            ]:
                values = parsed_data.get(
                    key,
                    []
                )

                if isinstance(values, list):
                    extracted_skills.extend(values)

            extracted_skills = list(
                set(extracted_skills)
            )

            for skill in extracted_skills:

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
                    extracted_skills
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

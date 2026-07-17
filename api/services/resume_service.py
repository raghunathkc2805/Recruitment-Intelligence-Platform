"""
Recruitment Intelligence Platform
Resume Service
"""

from __future__ import annotations

import logging
import uuid

from pathlib import Path
from tempfile import NamedTemporaryFile

from sqlalchemy.orm import Session

from api.storage.storage_manager import StorageManager
from api.utils.hash_util import HashUtil

from database.models.candidate import Candidate
from database.models.resume import Resume

from database.repositories.candidate_repository import CandidateRepository
from database.repositories.resume_repository import ResumeRepository

from database.repositories.candidate_skill_repository import (
    CandidateSkillRepository,
)

from database.repositories.candidate_education_repository import (
    CandidateEducationRepository,
)

from database.repositories.candidate_experience_repository import (
    CandidateExperienceRepository,
)

from database.repositories.candidate_certification_repository import (
    CandidateCertificationRepository,
)

from database.repositories.candidate_project_repository import (
    CandidateProjectRepository,
)

from resume_parser.resume_service import ResumeService as Parser

logger = logging.getLogger(__name__)


class ResumeService:

    PARSER_VERSION = "1.0"

    @classmethod
    def parse(
        cls,
        db: Session,
        upload_file,
    ) -> dict:

        temp_file: Path | None = None
        stored_resume: Path | None = None

        try:

            suffix = Path(
                upload_file.filename
            ).suffix

            with NamedTemporaryFile(
                delete=False,
                suffix=suffix,
            ) as tmp:

                content = upload_file.file.read()

                tmp.write(
                    content
                )

                temp_file = Path(
                    tmp.name
                )

            resume_hash = HashUtil.calculate(
                temp_file
            )

            resume_repo = ResumeRepository(
                db
            )

            existing_resume = (
                resume_repo.get_by_hash(
                    resume_hash
                )
            )

            if existing_resume is not None:

                if (
                    temp_file
                    and temp_file.exists()
                ):
                    temp_file.unlink()

                return {

                    "duplicate": True,

                    "resume_saved": False,

                    "resume_id": existing_resume.id,

                    "candidate_id": existing_resume.candidate_id,

                    "message": "Resume already exists.",

                }

            stored_resume = StorageManager.save_resume(

                source_file=temp_file,

                original_filename=upload_file.filename,

            )

            parsed = Parser.parse(
                stored_resume
            )

            candidate_repo = CandidateRepository(
                db
            )

            email = (
                parsed.get(
                    "email",
                    "",
                )
                .strip()
                .lower()
            )

            candidate = None

            if email:

                candidate = (
                    candidate_repo.get_by_email(
                        email
                    )
                )

            if candidate is None:

                candidate = Candidate(

                    candidate_code=(
                        f"CAN-{uuid.uuid4().hex[:10].upper()}"
                    ),

                    full_name=parsed.get(
                        "name",
                        "Unknown Candidate",
                    ),

                    email=email,

                    mobile=parsed.get(
                        "mobile",
                        "",
                    ),

                    location=parsed.get(
                        "location",
                        "",
                    ),

                    experience_years=float(
                        parsed.get(
                            "experience_years",
                            0,
                        )
                    ),

                    current_designation=parsed.get(
                        "designation",
                        "",
                    ),

                )

                candidate = (
                    candidate_repo.create(
                        candidate
                    )
                )

            resume = Resume(

                candidate_id=candidate.id,

                file_name=upload_file.filename,

                file_path=str(
                    stored_resume
                ),

                resume_hash=resume_hash,

                file_size=Path(
                    stored_resume
                ).stat().st_size,

                mime_type=(
                    upload_file.content_type
                    or ""
                ),

                parser_version=cls.PARSER_VERSION,

            )

            resume = resume_repo.create(
                resume
            )

            skill_repo = CandidateSkillRepository(
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

                    skill_repo.create(
                        candidate.id,
                        skill,
                    )
            education_repo = CandidateEducationRepository(
                db
            )

            for education in parsed.get(
                "education",
                [],
            ):

                education_repo.create(

                    candidate_id=candidate.id,

                    degree=education.get(
                        "degree",
                        "",
                    ),

                    specialization=education.get(
                        "specialization",
                        "",
                    ),

                    institution=education.get(
                        "institution",
                        "",
                    ),

                    passing_year=education.get(
                        "passing_year",
                        "",
                    ),

                )

            experience_repo = (
                CandidateExperienceRepository(
                    db
                )
            )

            for experience in parsed.get(
                "experience",
                [],
            ):

                experience_repo.create(

                    candidate_id=candidate.id,

                    company_name=experience.get(
                        "company",
                        "",
                    ),

                    designation=experience.get(
                        "designation",
                        "",
                    ),

                    experience_years=float(
                        experience.get(
                            "years",
                            0,
                        )
                    ),

                )

            certification_repo = (
                CandidateCertificationRepository(
                    db
                )
            )

            for certification in parsed.get(
                "certifications",
                [],
            ):

                certification_repo.create(

                    candidate_id=candidate.id,

                    certification_name=certification.get(
                        "name",
                        "",
                    ),

                    issuing_organization=certification.get(
                        "issuer",
                        "",
                    ),

                )

            project_repo = (
                CandidateProjectRepository(
                    db
                )
            )

            for project in parsed.get(
                "projects",
                [],
            ):

                project_repo.create(

                    candidate_id=candidate.id,

                    project_name=project.get(
                        "name",
                        "",
                    ),

                    description=project.get(
                        "description",
                        "",
                    ),

                    technologies=", ".join(

                        project.get(
                            "technologies",
                            [],
                        )

                    ),

                )

            db.commit()

            db.refresh(
                candidate
            )

            db.refresh(
                resume
            )

            return {

                "duplicate": False,

                "resume_saved": True,

                "candidate_id": candidate.id,

                "candidate_code": (
                    candidate.candidate_code
                ),

                "resume_id": resume.id,

                "resume_hash": resume_hash,

                "parsed_data": parsed,

            }

        except Exception:

            db.rollback()

            logger.exception(
                "Resume upload transaction failed."
            )

            if (
                stored_resume is not None
                and stored_resume.exists()
            ):

                try:

                    stored_resume.unlink()

                except Exception:

                    logger.exception(
                        "Unable to remove stored resume."
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
                        "Unable to remove temporary resume."
                    )

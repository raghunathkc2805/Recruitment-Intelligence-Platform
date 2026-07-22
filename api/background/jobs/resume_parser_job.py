"""
Sprint 8
Resume Background Processing Job
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def process_resume(
    resume_service,
    candidate_id: str,
    file_path: str,
):

    logger.info(
        "Starting resume parsing for %s",
        candidate_id,
    )

    result = resume_service.parse_resume(
        candidate_id=candidate_id,
        resume_path=file_path,
    )

    logger.info(
        "Completed resume parsing for %s",
        candidate_id,
    )

    return result

"""
Sprint 8
JD Background Processing Job
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def process_job_description(
    jd_service,
    job_id: str,
    file_path: str,
):

    logger.info(
        "Starting JD parsing: %s",
        job_id,
    )

    result = jd_service.parse_job_description(
        job_id=job_id,
        jd_path=file_path,
    )

    logger.info(
        "Completed JD parsing: %s",
        job_id,
    )

    return result

"""
Sprint 8
AI Recommendation Background Job
"""

from __future__ import annotations

import logging
import time

logger = logging.getLogger(__name__)


def process_recommendation(
    recommendation_service,
    candidate_id: str,
    job_id: str,
):

    logger.info(
        "Recommendation started | Candidate=%s Job=%s",
        candidate_id,
        job_id,
    )

    started = time.perf_counter()

    result = recommendation_service.generate_recommendation(
        candidate_id=candidate_id,
        job_id=job_id,
    )

    elapsed = round(
        time.perf_counter() - started,
        3,
    )

    logger.info(
        "Recommendation completed | Candidate=%s Job=%s Time=%ss",
        candidate_id,
        job_id,
        elapsed,
    )

    return result

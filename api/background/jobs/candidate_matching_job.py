"""
Sprint 8
Candidate Matching Background Job
"""

from __future__ import annotations

import logging
import time

logger = logging.getLogger(__name__)


def process_candidate_matching(
    matching_service,
    candidate_id: str,
    job_id: str,
):

    logger.info(
        "Candidate matching started | Candidate=%s Job=%s",
        candidate_id,
        job_id,
    )

    started = time.perf_counter()

    result = matching_service.match_candidate(
        candidate_id=candidate_id,
        job_id=job_id,
    )

    elapsed = round(
        time.perf_counter() - started,
        3,
    )

    logger.info(
        "Candidate matching completed | Candidate=%s Job=%s Time=%ss",
        candidate_id,
        job_id,
        elapsed,
    )

    return result


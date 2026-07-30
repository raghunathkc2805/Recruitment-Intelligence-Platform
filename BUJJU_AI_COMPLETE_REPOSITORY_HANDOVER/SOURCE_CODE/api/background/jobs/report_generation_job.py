"""
Sprint 8
Report Generation Background Job
"""

from __future__ import annotations

import logging
import time

logger = logging.getLogger(__name__)


def generate_report(
    report_service,
    report_type: str,
    parameters: dict,
):

    logger.info(
        "Report generation started | Type=%s",
        report_type,
    )

    started = time.perf_counter()

    report = report_service.generate(
        report_type=report_type,
        parameters=parameters,
    )

    elapsed = round(
        time.perf_counter() - started,
        3,
    )

    logger.info(
        "Report generation completed | Type=%s Time=%ss",
        report_type,
        elapsed,
    )

    return report

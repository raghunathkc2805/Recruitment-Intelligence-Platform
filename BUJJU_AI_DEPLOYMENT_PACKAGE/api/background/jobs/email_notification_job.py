"""
Sprint 8
Email Notification Background Job
"""

from __future__ import annotations

import logging
import time

logger = logging.getLogger(__name__)


def send_email_notification(
    email_service,
    recipients: list[str],
    subject: str,
    body: str,
    attachments: list[str] | None = None,
):

    logger.info(
        "Email notification started (%d recipients)",
        len(recipients),
    )

    started = time.perf_counter()

    result = email_service.send_email(
        recipients=recipients,
        subject=subject,
        body=body,
        attachments=attachments or [],
    )

    elapsed = round(time.perf_counter() - started, 3)

    logger.info(
        "Email notification completed (%d recipients) %.3fs",
        len(recipients),
        elapsed,
    )

    return result


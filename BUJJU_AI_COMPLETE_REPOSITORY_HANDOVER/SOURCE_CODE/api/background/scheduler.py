"""
Enterprise Background Scheduler
"""

from __future__ import annotations

import logging
from apscheduler.schedulers.background import BackgroundScheduler

logger = logging.getLogger(__name__)


class SchedulerManager:

    def __init__(self):

        self.scheduler = BackgroundScheduler(timezone="UTC")

    def start(self):

        if not self.scheduler.running:
            self.scheduler.start()
            logger.info("Background scheduler started.")

    def shutdown(self):

        if self.scheduler.running:
            self.scheduler.shutdown(wait=False)

    def add_interval_job(
        self,
        func,
        minutes: int,
        job_id: str,
    ):

        self.scheduler.add_job(
            func,
            trigger="interval",
            minutes=minutes,
            id=job_id,
            replace_existing=True,
            coalesce=True,
            max_instances=1,
        )

scheduler_manager = SchedulerManager()

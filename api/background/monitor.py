from __future__ import annotations

from collections import Counter
from datetime import datetime


class BackgroundMonitor:

    def __init__(self):

        self.statistics = Counter()

        self.running_jobs = {}

        self.completed_jobs = {}

    def job_started(
        self,
        task,
    ):

        self.statistics["submitted"] += 1

        self.statistics["running"] += 1

        task.started_at = datetime.utcnow()

        self.running_jobs[task.id] = task

    def job_completed(
        self,
        task,
    ):

        self.statistics["running"] -= 1

        self.statistics["completed"] += 1

        task.completed_at = datetime.utcnow()

        self.completed_jobs[task.id] = task

        self.running_jobs.pop(task.id, None)

    def job_failed(
        self,
        task,
    ):

        self.statistics["running"] -= 1

        self.statistics["failed"] += 1

        task.completed_at = datetime.utcnow()

        self.completed_jobs[task.id] = task

        self.running_jobs.pop(task.id, None)

    def dashboard(self):

        return {

            "submitted": self.statistics["submitted"],

            "running": self.statistics["running"],

            "completed": self.statistics["completed"],

            "failed": self.statistics["failed"],

            "active_jobs": len(self.running_jobs),

            "completed_jobs": len(self.completed_jobs),

        }


background_monitor = BackgroundMonitor()

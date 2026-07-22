from pydantic import BaseModel


class BackgroundDashboard(BaseModel):

    submitted: int

    running: int

    completed: int

    failed: int

    active_jobs: int

    completed_jobs: int

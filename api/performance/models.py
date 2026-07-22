from pydantic import BaseModel


class PerformanceReport(BaseModel):

    metrics: dict

    system: dict

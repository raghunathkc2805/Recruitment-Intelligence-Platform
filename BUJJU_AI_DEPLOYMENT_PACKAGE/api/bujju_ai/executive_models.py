from pydantic import BaseModel
from datetime import datetime


class ExecutiveMetricsRequest(BaseModel):
    total_open_positions: int
    critical_positions: int
    ageing_positions: int
    active_pipeline_candidates: int
    offers_released: int
    joined_candidates: int


class ExecutiveMetricsResponse(BaseModel):
    hiring_health_score: float
    hiring_status: str
    insights: list[str]
    recommendations: list[str]
    generated_at: datetime

from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class HiringRiskRequest(BaseModel):
    position_id: str
    position_title: str
    open_days: int
    required_skills: list[str]
    available_candidates: int
    matching_candidates: int


class HiringRiskResponse(BaseModel):
    position_id: str
    risk_score: float
    risk_level: RiskLevel
    reasons: list[str]
    recommendations: list[str]
    generated_at: datetime

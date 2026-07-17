"""
Common API Schemas
"""

from __future__ import annotations

from datetime import datetime, UTC
from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class ApiResponse(BaseModel):

    success: bool = True
    message: str = "Success"
    data: Any | None = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))


class ErrorResponse(BaseModel):

    success: bool = False
    message: str
    error_code: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))


class PaginationResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    total: int
    page: int
    page_size: int
    items: list[Any]
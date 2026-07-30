"""
API Schemas
"""

from .candidate import (
    CandidateCreateRequest,
    CandidateResponse,
)

from .common import (
    ApiResponse,
    ErrorResponse,
    PaginationResponse,
)

__all__ = [
    "CandidateCreateRequest",
    "CandidateResponse",
    "ApiResponse",
    "ErrorResponse",
    "PaginationResponse",
]
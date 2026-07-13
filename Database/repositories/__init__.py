"""
Repository Layer
"""

from .base_repository import BaseRepository
from .candidate_repository import CandidateRepository

__all__ = [
    "BaseRepository",
    "CandidateRepository",
]
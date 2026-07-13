"""
Ranking Engine Constants
"""

from __future__ import annotations

DEFAULT_WEIGHTS = {
    "skills": 35,
    "experience": 25,
    "education": 15,
    "designation": 10,
    "certification": 10,
    "location": 5,
}

HIGH_PRIORITY = 90.0
MEDIUM_PRIORITY = 75.0
LOW_PRIORITY = 60.0

MAX_SCORE = 100.0
MIN_SCORE = 0.0
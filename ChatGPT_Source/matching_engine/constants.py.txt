"""
Matching Engine Constants
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

MATCH_FIELDS = (
    "skill_match",
    "experience_match",
    "education_match",
    "designation_match",
    "location_match",
    "certification_match",
)

MAX_SCORE = 100.0
MIN_SCORE = 0.0
"""
API Routers
"""

from .auth import router as auth_router
from .candidates import router as candidates_router
from .health import router as health_router
from .jd import router as jd_router
from .matching import router as matching_router
from .ranking import router as ranking_router
from .recommendation import router as recommendation_router
from .resume import router as resume_router
from .search import router as search_router

__all__ = [

    "auth_router",

    "candidates_router",

    "health_router",

    "jd_router",

    "matching_router",

    "ranking_router",

    "recommendation_router",

    "resume_router",

    "search_router",

]

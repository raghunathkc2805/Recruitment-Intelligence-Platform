"""
Recruitment Intelligence Platform
Unified FastAPI Application
"""

from __future__ import annotations

from fastapi import FastAPI

from api.routers.health import router as health_router
from api.routers.resume import router as resume_router
from api.routers.jd import router as jd_router
from api.routers.matching import router as matching_router
from api.routers.ranking import router as ranking_router
from api.routers.search import router as search_router

from api.routers.candidates import (
    router as candidate_router,
)


app = FastAPI(
    title="Recruitment Intelligence Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(health_router)
app.include_router(resume_router)
app.include_router(jd_router)
app.include_router(matching_router)
app.include_router(ranking_router)
app.include_router(search_router)

app.include_router(candidate_router)
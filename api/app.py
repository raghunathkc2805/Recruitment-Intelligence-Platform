"""
Recruitment Intelligence Platform
Unified FastAPI Application
"""

from __future__ import annotations

from fastapi import FastAPI
from api.observability.metrics_middleware import MetricsMiddleware
from api.observability.opentelemetry_config import configure_tracing
from api.observability.instrumentation import instrument
from api.observability.trace_middleware import TraceMiddleware
from api.observability import RequestLoggingMiddleware
from api.background import background_manager
from api.cache import cache_manager
from api.middleware.compression import register_compression
from api.background.scheduler import scheduler_manager
from api.middleware.security_headers import SecurityHeadersMiddleware
from api.middleware.rate_limiter import RateLimiterMiddleware
from api.middleware.audit_logging import AuditLoggingMiddleware
from api.middleware.security_hardening import SecurityHardeningMiddleware

from api.routers.health import router as health_router
from api.routers.resume import router as resume_router
from api.routers.jd import router as jd_router
from api.routers.matching import router as matching_router
from api.routers.ranking import router as ranking_router
from api.routers.search import router as search_router
from api.routers.candidates import router as candidate_router
from api.routers.auth import router as auth_router
from api.routers.recommendation import router as recommendation_router

app = FastAPI(
    title="Recruitment Intelligence Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(RateLimiterMiddleware)
app.add_middleware(AuditLoggingMiddleware)
app.add_middleware(SecurityHardeningMiddleware)

# Core APIs
app.include_router(health_router)
app.include_router(resume_router)
app.include_router(jd_router)
app.include_router(matching_router)
app.include_router(ranking_router)
app.include_router(search_router)

# Business APIs
app.include_router(candidate_router)

# Authentication
app.include_router(auth_router)





from api.background.jobs.cleanup_job import cleanup_temp_files
from api.background.jobs.database_maintenance_job import database_maintenance
from api.background.jobs.cache_cleanup_job import cache_cleanup


@app.on_event("startup")
async def startup_scheduler():

    scheduler_manager.add_interval_job(
        cleanup_temp_files,
        minutes=30,
        job_id="cleanup_job",
    )

    scheduler_manager.add_interval_job(
        cache_cleanup,
        minutes=60,
        job_id="cache_cleanup",
    )

    scheduler_manager.add_interval_job(
        database_maintenance,
        minutes=180,
        job_id="database_maintenance",
    )

    scheduler_manager.start()



from api.database.connection_pool import engine
from api.database.pool_metrics import pool_metrics

pool_metrics.register(engine)


register_compression(app)


from api.utils.http_client import http_client


@app.on_event("shutdown")
async def shutdown_async_clients():

    await http_client.close()


app.add_middleware(
    RequestLoggingMiddleware,
)


app.add_middleware(
    TraceMiddleware,
)


configure_tracing()

instrument(app)


app.add_middleware(
    MetricsMiddleware
)

from api.routers.metrics import router as metrics_router

app.include_router(metrics_router)


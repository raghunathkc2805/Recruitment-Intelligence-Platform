from __future__ import annotations
from api.routers.talent_marketplace import router as talent_marketplace_router
from api.routers.candidate_discovery import router as candidate_discovery_router
from api.routers.analytics import router as analytics_router
from api.routers.market_intelligence import router as market_intelligence_router
from api.routers.recruiter_hiring_intelligence import router as recruiter_hiring_router
from api.routers.candidate_intelligence_advanced import router as candidate_analysis_router
from api.routers.skill_competency import router as skill_competency_router
from api.routers.ai_candidate_ranking import router as ai_ranking_router
from api.routers.knowledge_governance import router as knowledge_governance_router
from api.routers.continuous_learning import router as learning_router
from api.routers.whatsapp_outreach import router as whatsapp_router
from api.routers.candidate_relationship import router as candidate_relationship_router
from api.routers.recruiter_copilot import router as recruiter_ai_router
from api.routers.explainable_ai import router as explainable_ai_router
from api.routers.similar_candidate import router as similar_candidate_router
from api.routers.candidate_intelligence import router as candidate_intelligence_router
from api.routers.designation_intelligence import router as designation_intelligence_router
from api.routers.skill_intelligence import router as skill_intelligence_router
from api.routers.knowledge_graph import router as knowledge_graph_router
from api.routers.knowledge import router as knowledge_router
"""
Recruitment Intelligence Platform
Unified FastAPI Application
"""


from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from api.observability.metrics_middleware import MetricsMiddleware
from api.observability.opentelemetry_config import configure_tracing
from api.observability.instrumentation import instrument
from api.observability.trace_middleware import TraceMiddleware
from api.observability import RequestLoggingMiddleware
from api.background import background_manager
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
from api.routes.audit import router as audit_router

app = FastAPI(
    title="Recruitment Intelligence Platform",
    version="1.0.0",
    docs_url=None,
    redoc_url="/redoc",
)



app.mount("/static", StaticFiles(directory="api/static"), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_docs():

    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Recruitment Intelligence Platform</title>
        <link rel="stylesheet" href="/static/swagger-ui.css">
    </head>
    <body>

    <div id="swagger-ui"></div>

    <script src="/static/swagger-ui-bundle.js"></script>

    <script>
    SwaggerUIBundle({
        url: "/openapi.json",
        dom_id: "#swagger-ui"
    })
    </script>

    </body>
    </html>
    """)


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

# Audit
app.include_router(audit_router)





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



app.include_router(knowledge_router)

app.include_router(knowledge_graph_router)

app.include_router(skill_intelligence_router)
app.include_router(designation_intelligence_router)

app.include_router(candidate_intelligence_router)

app.include_router(similar_candidate_router)

app.include_router(explainable_ai_router)

app.include_router(recruiter_ai_router)

app.include_router(candidate_relationship_router)

app.include_router(whatsapp_router)

app.include_router(learning_router)

app.include_router(knowledge_governance_router)

app.include_router(ai_ranking_router)

app.include_router(skill_competency_router)

app.include_router(candidate_analysis_router)

app.include_router(recruiter_hiring_router)

app.include_router(market_intelligence_router)

app.include_router(analytics_router)

app.include_router(candidate_discovery_router)

app.include_router(talent_marketplace_router)

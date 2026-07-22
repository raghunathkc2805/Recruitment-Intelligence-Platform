"""
Enterprise Recommendation API
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from api.auth.permission_constants import Permission
from api.auth.permission_dependency import require_permission
from api.dependencies import DatabaseSession

from database.repositories.job_repository import JobRepository

from api.services.recommendation_service import RecommendationService
from api.background import background_manager
from api.background.jobs.recommendation_job import process_recommendation

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
)


@router.get(
    "/{job_id}",
    dependencies=[
        Depends(
            require_permission(
                Permission.RECOMMENDATION_RUN,
            )
        )
    ],
)
async def recommend_candidates(
    job_id: str,
    db: DatabaseSession,
    limit: int = 10,
):

    job = JobRepository(db).get(job_id)

    if job is None:

        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    recommendations = RecommendationService.recommend(
        db=db,
        job=job,
        limit=limit,
    )

    return {
        "job_id": job.id,
        "job_title": getattr(
            job,
            "job_title",
            "",
        ),
        "total_recommendations": len(
            recommendations
        ),
        "recommendations": recommendations,
    }


@router.get(
    "/{job_id}/top",
    dependencies=[
        Depends(
            require_permission(
                Permission.RECOMMENDATION_RUN,
            )
        )
    ],
)
async def top_candidate(
    job_id: str,
    db: DatabaseSession,
):

    job = JobRepository(db).get(job_id)

    if job is None:

        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    recommendations = RecommendationService.recommend(
        db=db,
        job=job,
        limit=1,
    )

    if not recommendations:
        return {}

    return recommendations[0]

# ==============================================================================
# Queue Recommendation Generation
# ==============================================================================

def queue_recommendation(
    recommendation_service,
    candidate_id: str,
    job_id: str,
):

    return background_manager.submit(
        "recommendation",
        process_recommendation,
        recommendation_service,
        candidate_id,
        job_id,
    )


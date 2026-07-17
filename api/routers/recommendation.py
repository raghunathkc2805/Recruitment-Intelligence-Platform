"""
Enterprise Recommendation API
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import HTTPException

from api.dependencies import DatabaseSession

from database.repositories.job_repository import JobRepository

from api.services.recommendation_service import RecommendationService

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
)


@router.get("/{job_id}")
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


@router.get("/{job_id}/top")
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

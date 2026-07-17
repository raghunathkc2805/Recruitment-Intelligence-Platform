"""
Enterprise Search Router
"""

from __future__ import annotations

from fastapi import APIRouter

from api.dependencies import DatabaseSession
from api.services.search_service import SearchService

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@router.post("")
async def search(
    payload: dict,
    db: DatabaseSession,
):

    return SearchService.run(
        db=db,
        payload=payload,
    )


@router.post("/skills")
async def search_by_skills(
    payload: dict,
    db: DatabaseSession,
):

    return SearchService.run(
        db=db,
        payload={
            "query": payload.get(
                "skills",
                "",
            ),
            "designation": payload.get(
                "designation",
            ),
            "location": payload.get(
                "location",
            ),
            "experience": payload.get(
                "experience",
            ),
        },
    )


@router.post("/designation")
async def search_by_designation(
    payload: dict,
    db: DatabaseSession,
):

    return SearchService.run(
        db=db,
        payload={
            "designation": payload.get(
                "designation",
            ),
        },
    )


@router.post("/location")
async def search_by_location(
    payload: dict,
    db: DatabaseSession,
):

    return SearchService.run(
        db=db,
        payload={
            "location": payload.get(
                "location",
            ),
        },
    )


@router.post("/advanced")
async def advanced_search(
    payload: dict,
    db: DatabaseSession,
):

    return SearchService.run(
        db=db,
        payload=payload,
    )

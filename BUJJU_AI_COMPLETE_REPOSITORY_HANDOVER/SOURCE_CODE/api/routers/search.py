"""
Enterprise Search Router
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends

from api.auth.permission_constants import Permission
from api.auth.permission_dependency import require_permission
from api.dependencies import DatabaseSession
from api.services.search_service import SearchService

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@router.post(
    "",
    dependencies=[
        Depends(
            require_permission(
                Permission.SEARCH_EXECUTE,
            )
        )
    ],
)
async def search(
    payload: dict,
    db: DatabaseSession,
):
    return SearchService.run(
        db=db,
        payload=payload,
    )


@router.post(
    "/skills",
    dependencies=[
        Depends(
            require_permission(
                Permission.SEARCH_EXECUTE,
            )
        )
    ],
)
async def search_by_skills(
    payload: dict,
    db: DatabaseSession,
):
    return SearchService.run(
        db=db,
        payload={
            "query": payload.get("skills", ""),
            "designation": payload.get("designation"),
            "location": payload.get("location"),
            "experience": payload.get("experience"),
        },
    )


@router.post(
    "/designation",
    dependencies=[
        Depends(
            require_permission(
                Permission.SEARCH_EXECUTE,
            )
        )
    ],
)
async def search_by_designation(
    payload: dict,
    db: DatabaseSession,
):
    return SearchService.run(
        db=db,
        payload={
            "designation": payload.get("designation"),
        },
    )


@router.post(
    "/location",
    dependencies=[
        Depends(
            require_permission(
                Permission.SEARCH_EXECUTE,
            )
        )
    ],
)
async def search_by_location(
    payload: dict,
    db: DatabaseSession,
):
    return SearchService.run(
        db=db,
        payload={
            "location": payload.get("location"),
        },
    )


@router.post(
    "/advanced",
    dependencies=[
        Depends(
            require_permission(
                Permission.SEARCH_EXECUTE,
            )
        )
    ],
)
async def advanced_search(
    payload: dict,
    db: DatabaseSession,
):
    return SearchService.run(
        db=db,
        payload=payload,
    )

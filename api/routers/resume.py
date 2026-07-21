"""
Resume Router
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile

from api.auth.permission_constants import Permission
from api.auth.permission_dependency import require_permission
from api.dependencies import DatabaseSession
from api.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)


@router.post(
    "/parse",
    dependencies=[
        Depends(
            require_permission(
                Permission.RESUME_UPLOAD,
            )
        )
    ],
)
async def parse_resume(
    file: UploadFile = File(...),
    db: DatabaseSession = None,
):
    return ResumeService.parse(
        db=db,
        upload_file=file,
    )

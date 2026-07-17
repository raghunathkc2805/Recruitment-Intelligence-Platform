"""
Resume Router
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

from api.dependencies import DatabaseSession
from api.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)


@router.post("/parse")
async def parse_resume(
    file: UploadFile = File(...),
    db: DatabaseSession = None,
):

    return ResumeService.parse(
        db=db,
        upload_file=file,
    )

from fastapi import APIRouter, UploadFile, File

from api.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)


@router.post("/parse")
async def parse_resume(
    file: UploadFile = File(...)
):

    return ResumeService.parse(
        file
    )
from fastapi import APIRouter, UploadFile, File

from api.services.jd_service import JDService

router = APIRouter(
    prefix="/jd",
    tags=["JD"],
)


@router.post("/parse")
async def parse_jd(
    file: UploadFile = File(...)
):

    return JDService.parse(
        file
    )
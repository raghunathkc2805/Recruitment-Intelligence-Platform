from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

from api.dependencies import DatabaseSession
from api.services.jd_service import JDService

router = APIRouter(
    prefix="/jd",
    tags=["JD"],
)


@router.post("/parse")
async def parse_jd(
    file: UploadFile = File(...),
    db: DatabaseSession = None,
):

    return JDService.parse(
        db=db,
        upload_file=file,
    )

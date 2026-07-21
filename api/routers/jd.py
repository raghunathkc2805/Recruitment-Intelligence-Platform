from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile

from api.auth.permission_constants import Permission
from api.auth.permission_dependency import require_permission
from api.dependencies import DatabaseSession
from api.services.jd_service import JDService

router = APIRouter(
    prefix="/jd",
    tags=["JD"],
)


@router.post(
    "/parse",
    dependencies=[
        Depends(
            require_permission(
                Permission.JD_CREATE,
            )
        )
    ],
)
async def parse_jd(
    file: UploadFile = File(...),
    db: DatabaseSession = None,
):
    return JDService.parse(
        db=db,
        upload_file=file,
    )

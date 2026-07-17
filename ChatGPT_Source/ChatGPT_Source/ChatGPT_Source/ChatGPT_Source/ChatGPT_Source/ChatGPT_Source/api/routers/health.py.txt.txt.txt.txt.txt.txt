from fastapi import APIRouter

router = APIRouter(
    prefix="",
    tags=["Health"],
)


@router.get("/health")
async def health():

    return {
        "status": "healthy",
        "platform": "Recruitment Intelligence Platform",
        "version": "1.0.0",
    }
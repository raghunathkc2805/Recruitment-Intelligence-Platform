from fastapi import APIRouter

from api.health import health_service

router = APIRouter(tags=["Health"])

@router.get("/health")
def health():
    return health_service.health()

@router.get("/live")
def live():
    return health_service.liveness()

@router.get("/ready")
def ready():
    return health_service.readiness()

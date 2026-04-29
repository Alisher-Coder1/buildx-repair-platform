from fastapi import APIRouter

from app.core.config import API_VERSION
from app.core.responses import success_response

router = APIRouter()


@router.get("/health")
def health_check():
    return success_response(
        {
            "status": "ok",
            "service": "buildx-repair-platform-api",
            "version": API_VERSION,
        }
    )

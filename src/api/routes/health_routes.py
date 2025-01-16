from fastapi import APIRouter, status
from ..middleware.error_handler import APIError

router = APIRouter(tags=["health"])

@router.get("/health")
async def health_check():
    try:
        return {"status": "healthy"}
    except Exception as e:
        raise APIError(
            message="Health check failed",
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            details={"error": str(e)}
        )

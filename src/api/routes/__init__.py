from fastapi import APIRouter

from src.api.routes.cache import router as cache_router
from src.api.routes.execution import router as execution_router
from src.api.routes.graph_routes import router as graph_router
from src.api.routes.health import router as health_router
from src.api.routes.llm_routes import router as llm_router
from src.api.routes.metrics import router as metrics_router

router = APIRouter()

router.include_router(cache_router, prefix="/cache", tags=["cache"])
router.include_router(execution_router, prefix="/execution", tags=["execution"])
router.include_router(graph_router, prefix="/graph", tags=["graph"])
router.include_router(health_router, prefix="/health", tags=["health"])
router.include_router(llm_router, prefix="/llm", tags=["llm"])
router.include_router(metrics_router, prefix="/metrics", tags=["metrics"])

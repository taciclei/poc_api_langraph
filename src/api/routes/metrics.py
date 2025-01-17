from fastapi import APIRouter, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from ..metrics.prometheus import metrics
from ..services.llm_service import LLMService

router = APIRouter(prefix="/metrics", tags=["metrics"])
llm_service = LLMService()

@router.get("")
async def get_metrics():
    """Endpoint Prometheus"""
    return Response(
        generate_latest(metrics.registry),
        media_type=CONTENT_TYPE_LATEST
    )

@router.get("/summary")
async def get_metrics_summary():
    """Résumé des métriques pour le dashboard"""
    cache_stats = await llm_service.get_cache_stats()
    
    return {
        "llm": {
            "requests": {
                provider: metrics.llm_requests.labels(
                    provider=provider,
                    cache_hit="false"
                )._value.get()
                for provider in await llm_service.get_available_providers()
            },
            "cache_hits": sum(
                metrics.llm_requests.labels(
                    provider=provider,
                    cache_hit="true"
                )._value.get()
                for provider in await llm_service.get_available_providers()
            )
        },
        "cache": cache_stats,
        "api": {
            "total_requests": sum(
                metrics.api_requests.labels(
                    endpoint=endpoint,
                    method=method,
                    status=status
                )._value.get()
                for endpoint, method, status in metrics.api_requests._metrics
            )
        }
    }

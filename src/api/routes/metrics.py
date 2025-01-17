from fastapi import APIRouter
from typing import Dict, List, Any

router = APIRouter()

@router.get("/")
async def get_metrics() -> Dict[str, Any]:
    return {
        "requests_total": 100,
        "request_duration_seconds": 0.5,
        "active_graphs": 10
    }

@router.get("/graphs")
async def get_graph_metrics() -> Dict[str, Any]:
    return {
        "total_graphs": 10,
        "active_executions": 5,
        "average_execution_time": 2.5
    }

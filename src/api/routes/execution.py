from fastapi import APIRouter, HTTPException
from typing import Dict, Any, Optional
from src.api.services.execution_service import ExecutionService

router = APIRouter()
execution_service = ExecutionService()

@router.post("/{graph_id}")
async def execute_graph(graph_id: str, inputs: Dict[str, Any]):
    """Execute un graphe avec les entrées spécifiées"""
    try:
        result = execution_service.execute_graph(graph_id, inputs)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{execution_id}")
async def get_execution(execution_id: str):
    """Récupère les détails d'une exécution"""
    try:
        result = execution_service.get_execution(execution_id)
        if not result:
            raise HTTPException(status_code=404, detail="Execution not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
async def list_executions(
    graph_id: Optional[str] = None,
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 10
):
    """Liste les exécutions avec filtres optionnels"""
    try:
        executions = execution_service.list_executions(
            graph_id=graph_id,
            status=status,
            skip=skip,
            limit=limit
        )
        return executions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

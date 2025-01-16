"""Routes for graph execution management."""
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException

from src.api.models.execution import (
    Execution,
    ExecutionCreate,
    ExecutionUpdate,
    ExecutionFilter
)
from src.api.services.execution.execution_service import ExecutionService
from src.api.services.graph_service import GraphService

router = APIRouter(prefix="/executions", tags=["executions"])


async def get_execution_service() -> ExecutionService:
    """Dependency injection for execution service."""
    graph_service = GraphService()  # TODO: Use proper DI
    return ExecutionService(graph_service)


@router.post("/", response_model=Execution)
async def create_execution(
    execution_create: ExecutionCreate,
    service: ExecutionService = Depends(get_execution_service)
) -> Execution:
    """Create and start a new execution."""
    try:
        return await service.create_execution(execution_create)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{execution_id}", response_model=Execution)
async def get_execution(
    execution_id: UUID,
    service: ExecutionService = Depends(get_execution_service)
) -> Execution:
    """Get execution by ID."""
    execution = await service.get_execution(execution_id)
    if not execution:
        raise HTTPException(status_code=404, detail="Execution not found")
    return execution


@router.get("/", response_model=List[Execution])
async def list_executions(
    graph_id: UUID = None,
    status: str = None,
    start_time_after: str = None,
    start_time_before: str = None,
    service: ExecutionService = Depends(get_execution_service)
) -> List[Execution]:
    """List executions with optional filtering."""
    filter_params = ExecutionFilter(
        graph_id=graph_id,
        status=status,
        start_time_after=start_time_after,
        start_time_before=start_time_before
    )
    return await service.list_executions(filter_params)


@router.patch("/{execution_id}", response_model=Execution)
async def update_execution(
    execution_id: UUID,
    execution_update: ExecutionUpdate,
    service: ExecutionService = Depends(get_execution_service)
) -> Execution:
    """Update execution details."""
    execution = await service.update_execution(execution_id, execution_update)
    if not execution:
        raise HTTPException(status_code=404, detail="Execution not found")
    return execution
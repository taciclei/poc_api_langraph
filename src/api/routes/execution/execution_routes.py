from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from pydantic import BaseModel
from src.api.services.execution.execution_service import ExecutionService

router = APIRouter(prefix="/execution", tags=["execution"])
execution_service = ExecutionService()

class ExecutionRequest(BaseModel):
    graph_id: str
    input_data: Dict[str, Any]

@router.post("/start")
async def start_execution(request: ExecutionRequest):
    try:
        result = await execution_service.execute_graph(
            request.graph_id,
            request.input_data
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": f"Execution failed: {str(e)}"}
        )

@router.get("/status/{execution_id}")
async def get_execution_status(execution_id: str):
    try:
        return await execution_service.get_execution_status(execution_id)
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail={"message": str(e)}
        )

@router.get("/list/{graph_id}")
async def list_executions(graph_id: str):
    return await execution_service.list_executions(graph_id)

from fastapi import APIRouter, HTTPException
from typing import Dict, Any, Optional
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class ExecutionRequest(BaseModel):
    graph_id: str
    input_data: Dict[str, Any]
    config: Optional[Dict[str, Any]] = None

class ExecutionResponse(BaseModel):
    execution_id: str
    status: str
    start_time: datetime
    end_time: Optional[datetime] = None
    result: Optional[Dict[str, Any]] = None

@router.post("/", response_model=ExecutionResponse)
async def create_execution(request: ExecutionRequest):
    try:
        return ExecutionResponse(
            execution_id="exec_123",
            status="pending",
            start_time=datetime.now()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{execution_id}", response_model=ExecutionResponse)
async def get_execution(execution_id: str):
    return ExecutionResponse(
        execution_id=execution_id,
        status="completed",
        start_time=datetime.now(),
        end_time=datetime.now(),
        result={"output": "Sample result"}
    )

@router.post("/{execution_id}/cancel")
async def cancel_execution(execution_id: str):
    return {"status": "cancelled"}

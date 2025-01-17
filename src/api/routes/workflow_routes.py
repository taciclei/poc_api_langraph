from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List, Optional
from pydantic import BaseModel

router = APIRouter()

class WorkflowStep(BaseModel):
    id: str
    agent_id: str
    input_mapping: Dict[str, str]
    output_mapping: Dict[str, str]
    condition: Optional[Dict[str, Any]] = None

class WorkflowConfig(BaseModel):
    name: str
    description: str
    steps: List[WorkflowStep]
    error_handling: Optional[Dict[str, Any]] = None

class WorkflowResponse(BaseModel):
    id: str
    config: WorkflowConfig
    status: str

@router.post("/", response_model=WorkflowResponse)
async def create_workflow(config: WorkflowConfig):
    return WorkflowResponse(
        id="workflow_123",
        config=config,
        status="created"
    )

@router.get("/{workflow_id}", response_model=WorkflowResponse)
async def get_workflow(workflow_id: str):
    return WorkflowResponse(
        id=workflow_id,
        config=WorkflowConfig(
            name="test",
            description="test workflow",
            steps=[]
        ),
        status="active"
    )

@router.post("/{workflow_id}/execute")
async def execute_workflow(workflow_id: str, input_data: Dict[str, Any]):
    return {
        "execution_id": "exec_123",
        "status": "started",
        "workflow_id": workflow_id
    }

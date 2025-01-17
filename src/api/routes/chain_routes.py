from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List, Optional
from pydantic import BaseModel

router = APIRouter()

class ChainStep(BaseModel):
    id: str
    type: str
    config: Dict[str, Any]
    next_steps: List[str] = []
    error_handler: Optional[str] = None

class ChainConfig(BaseModel):
    name: str
    description: str
    steps: List[ChainStep]
    input_schema: Dict[str, Any]
    output_schema: Dict[str, Any]
    metadata: Dict[str, Any] = {}

class ChainResponse(BaseModel):
    id: str
    config: ChainConfig
    status: str
    version: str

@router.post("/", response_model=ChainResponse)
async def create_chain(config: ChainConfig):
    return ChainResponse(
        id="chain_123",
        config=config,
        status="created",
        version="1.0"
    )

@router.get("/templates")
async def list_chain_templates():
    return {
        "templates": [
            {
                "id": "qa_chain",
                "name": "Question Answering",
                "description": "Chain for Q&A over documents"
            },
            {
                "id": "summarization_chain",
                "name": "Summarization",
                "description": "Chain for text summarization"
            }
        ]
    }

@router.post("/{chain_id}/execute")
async def execute_chain(chain_id: str, input_data: Dict[str, Any]):
    return {
        "execution_id": "exec_123",
        "status": "running",
        "chain_id": chain_id
    }

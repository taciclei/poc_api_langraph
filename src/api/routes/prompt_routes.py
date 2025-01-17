from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class PromptTemplate(BaseModel):
    name: str
    template: str
    variables: List[str]
    description: str
    version: str
    tags: List[str] = []
    metadata: Dict[str, Any] = {}

class PromptResponse(BaseModel):
    id: str
    template: PromptTemplate
    created_at: datetime
    updated_at: datetime

@router.post("/", response_model=PromptResponse)
async def create_prompt(template: PromptTemplate):
    now = datetime.now()
    return PromptResponse(
        id="prompt_123",
        template=template,
        created_at=now,
        updated_at=now
    )

@router.get("/templates")
async def list_templates():
    return {
        "templates": [
            {
                "id": "tpl_1",
                "name": "ReAct Agent",
                "description": "Template for ReAct reasoning"
            },
            {
                "id": "tpl_2",
                "name": "Chain of Thought",
                "description": "Template for step-by-step reasoning"
            }
        ]
    }

@router.post("/{prompt_id}/validate")
async def validate_prompt(prompt_id: str, variables: Dict[str, str]):
    return {
        "is_valid": True,
        "rendered_prompt": "Example rendered prompt",
        "token_count": 150
    }

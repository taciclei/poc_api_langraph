from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List, Optional
from pydantic import BaseModel

router = APIRouter()

class ModelConfig(BaseModel):
    name: str
    provider: str
    api_key_env: str
    parameters: Dict[str, Any] = {}
    max_tokens: Optional[int] = None
    timeout: Optional[int] = None

class ModelResponse(BaseModel):
    id: str
    config: ModelConfig
    status: str
    metrics: Optional[Dict[str, Any]] = None

@router.post("/", response_model=ModelResponse)
async def register_model(config: ModelConfig):
    return ModelResponse(
        id="model_123",
        config=config,
        status="registered"
    )

@router.get("/providers")
async def list_providers():
    return {
        "providers": [
            "openai",
            "anthropic",
            "google",
            "mistral",
            "ollama"
        ]
    }

@router.get("/{model_id}/performance")
async def get_model_performance(model_id: str):
    return {
        "average_latency": 0.8,
        "tokens_per_second": 150,
        "error_rate": 0.02,
        "cost_per_1k_tokens": 0.002
    }

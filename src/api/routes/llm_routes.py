from typing import Optional, Dict, List
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from ..services.llm_service import LLMService
from ..llm.interface.base_llm import LLMResponse

router = APIRouter(prefix="/llm", tags=["llm"])

class GenerateRequest(BaseModel):
    prompt: str
    provider: Optional[str] = None
    max_tokens: Optional[int] = None
    temperature: float = 0.7
    use_cache: bool = True

@router.get("/providers", response_model=List[str])
async def get_available_providers(llm_service: LLMService = Depends()):
    return llm_service.get_available_providers()

@router.post("/generate", response_model=LLMResponse)
async def generate_text(
    request: GenerateRequest,
    llm_service: LLMService = Depends()
):
    try:
        return await llm_service.generate(
            prompt=request.prompt,
            provider=request.provider,
            use_cache=request.use_cache,
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/stream")
async def stream_text(
    request: GenerateRequest,
    llm_service: LLMService = Depends()
):
    try:
        return await llm_service.stream(
            prompt=request.prompt,
            provider=request.provider,
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

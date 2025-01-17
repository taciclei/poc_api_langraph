from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from typing import Optional
from pydantic import BaseModel
from ..services.llm_service import LLMService

router = APIRouter()
llm_service = LLMService()

class CompletionRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = None
    temperature: Optional[float] = None
    stream: Optional[bool] = False

@router.post("/v1/completions")
async def create_completion(request: CompletionRequest):
    try:
        if request.stream:
            return StreamingResponse(
                llm_service.stream(
                    request.prompt,
                    max_tokens=request.max_tokens,
                    temperature=request.temperature
                ),
                media_type="text/event-stream"
            )
        else:
            return await llm_service.generate(
                request.prompt,
                max_tokens=request.max_tokens,
                temperature=request.temperature
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

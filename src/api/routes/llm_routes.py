from fastapi import APIRouter, HTTPException
<<<<<<< HEAD
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
=======
from typing import Dict, Any, List
from pydantic import BaseModel

router = APIRouter()

class CompletionRequest(BaseModel):
    prompt: str
    model: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_tokens: int = 150

class CompletionResponse(BaseModel):
    text: str
    model: str
    usage: Dict[str, int]

@router.post("/complete", response_model=CompletionResponse)
async def complete(request: CompletionRequest):
    try:
        # TODO: Implement actual LLM completion
        return CompletionResponse(
            text="Sample completion",
            model=request.model,
            usage={"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models")
async def list_models() -> List[str]:
    return ["gpt-3.5-turbo", "gpt-4", "claude-2", "gemini-pro"]
>>>>>>> release/1.1.0

from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List
from src.api.services.llm_service import LLMService

router = APIRouter()
llm_service = LLMService()

@router.post("/complete")
async def complete_text(prompt: Dict[str, str]):
    """Génère une complétion de texte avec le LLM"""
    try:
        result = await llm_service.complete(prompt)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat")
async def chat_completion(messages: List[Dict[str, str]]):
    """Génère une réponse de chat avec le LLM"""
    try:
        result = await llm_service.chat(messages)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

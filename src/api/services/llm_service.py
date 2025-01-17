from typing import AsyncGenerator, Optional, Dict, Any
from ..llm.fallback.llm_manager import LLMManager
from ..llm.providers.openai_llm import OpenAILLM
import time

class LLMService:
    def __init__(self):
        self.llm_manager = LLMManager([
            OpenAILLM()
        ])

    async def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Génère une réponse"""
        start_time = time.time()
        try:
            response = await self.llm_manager.generate(prompt, **kwargs)
            return {
                "text": response,
                "duration": time.time() - start_time
            }
        except Exception as e:
            return {
                "error": str(e),
                "duration": time.time() - start_time
            }

    async def stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        """Stream une réponse"""
        async for chunk in self.llm_manager.stream(prompt, **kwargs):
            yield chunk

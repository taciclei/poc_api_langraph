from typing import List, AsyncGenerator
from ..providers.openai_llm import OpenAILLM
from ..base_llm import BaseLLM
import logging

logger = logging.getLogger(__name__)

class LLMManager:
    def __init__(self, providers: List[BaseLLM] = None):
        self.providers = providers or [OpenAILLM()]

    async def generate(self, prompt: str, **kwargs) -> str:
        """Génère une réponse avec fallback"""
        last_error = None
        
        for provider in self.providers:
            try:
                return await provider.generate(prompt, **kwargs)
            except Exception as e:
                logger.warning(f"Error with {provider.provider}: {str(e)}")
                last_error = e
        
        raise last_error or Exception("No available LLM providers")

    async def stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        """Stream une réponse avec fallback"""
        last_error = None
        
        for provider in self.providers:
            try:
                async for chunk in provider.stream(prompt, **kwargs):
                    yield chunk
                return
            except Exception as e:
                logger.warning(f"Error with {provider.provider}: {str(e)}")
                last_error = e
        
        raise last_error or Exception("No available LLM providers")

from typing import Optional, Dict, Any
import asyncio
import google.generativeai as genai

from ..interface.base_llm import BaseLLM
from ...config import get_settings

settings = get_settings()

class GeminiLLM(BaseLLM):
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.GEMINI_API_KEY
        self.provider = "gemini"
        self.model = "gemini-pro"
        
        # Configure the Gemini client
        genai.configure(api_key=self.api_key)
        self.model_client = genai.GenerativeModel(self.model)
        self._temperature = 0.7
        self._max_tokens = None

    async def agenerate(
        self,
        prompt: str,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        temp = temperature if temperature is not None else self._temperature
        
        generation_config = {
            "temperature": temp,
        }
        if max_tokens is not None:
            generation_config["max_output_tokens"] = max_tokens

        # Utiliser asyncio.to_thread pour exécuter l'appel API de manière asynchrone
        response = await asyncio.to_thread(
            self.model_client.generate_content,
            prompt,
            generation_config=generation_config
        )
        
        return response.text

    def get_config(self) -> Dict[str, Any]:
        return {
            "provider": self.provider,
            "model": self.model,
            "temperature": self._temperature,
            "max_tokens": self._max_tokens
        }

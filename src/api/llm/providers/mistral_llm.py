from typing import Optional, Dict, Any, AsyncGenerator
import asyncio
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

from ..interface.base_llm import BaseLLM
from ...config import get_settings

settings = get_settings()

class MistralLLM(BaseLLM):
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.MISTRAL_API_KEY
        self.provider = "mistral"
        self.model = "mistral-large-latest"
        self.client = MistralClient(api_key=self.api_key)
        self._temperature = 0.7
        self._max_tokens = None

    async def generate(self, prompt: str, **kwargs) -> str:
        """Méthode synchrone pour la compatibilité avec l'interface"""
        return await self.agenerate(prompt, **kwargs)

    async def stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        """Stream the response from the LLM"""
        temp = kwargs.get('temperature', self._temperature)
        max_tok = kwargs.get('max_tokens', self._max_tokens)

        # Utiliser asyncio.to_thread pour rendre l'appel asynchrone
        chat_response = await asyncio.to_thread(
            self.client.chat_stream,
            model=self.model,
            messages=[ChatMessage(role="user", content=prompt)],
            temperature=temp,
            max_tokens=max_tok
        )

        for chunk in chat_response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    async def agenerate(
        self,
        prompt: str,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        temp = temperature if temperature is not None else self._temperature
        max_tok = max_tokens if max_tokens is not None else self._max_tokens

        # Utiliser asyncio.to_thread pour rendre l'appel asynchrone
        chat_response = await asyncio.to_thread(
            self.client.chat,
            model=self.model,
            messages=[ChatMessage(role="user", content=prompt)],
            temperature=temp,
            max_tokens=max_tok
        )

        return chat_response.choices[0].message.content

    def get_config(self) -> Dict[str, Any]:
        return {
            "provider": self.provider,
            "model": self.model,
            "temperature": self._temperature,
            "max_tokens": self._max_tokens
        }

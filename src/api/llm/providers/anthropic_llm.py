from typing import Optional, Dict, Any, AsyncGenerator
import anthropic

from ..interface.base_llm import BaseLLM
from ...config import get_settings

settings = get_settings()

class AnthropicLLM(BaseLLM):
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.ANTHROPIC_API_KEY
        self.provider = "anthropic"
        self.model = "claude-3-opus-20240229"
        self.client = anthropic.AsyncAnthropic(api_key=self.api_key)
        self._temperature = 0.7
        self._max_tokens = None

    async def generate(self, prompt: str, **kwargs) -> str:
        """Méthode synchrone pour la compatibilité avec l'interface"""
        return await self.agenerate(prompt, **kwargs)

    async def stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        """Stream the response from the LLM"""
        temp = kwargs.get('temperature', self._temperature)
        max_tok = kwargs.get('max_tokens', self._max_tokens)

        message = await self.client.messages.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temp,
            max_tokens=max_tok,
            stream=True
        )

        async for chunk in message:
            if chunk.content:
                yield chunk.content[0].text

    async def agenerate(
        self,
        prompt: str,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        temp = temperature if temperature is not None else self._temperature
        max_tok = max_tokens if max_tokens is not None else self._max_tokens

        message = await self.client.messages.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temp,
            max_tokens=max_tok
        )

        return message.content[0].text

    def get_config(self) -> Dict[str, Any]:
        return {
            "provider": self.provider,
            "model": self.model,
            "temperature": self._temperature,
            "max_tokens": self._max_tokens
        }

from typing import AsyncGenerator, Optional
from openai import AsyncOpenAI
from ...config import get_settings
from ..base_llm import BaseLLM

settings = get_settings()

class OpenAILLM(BaseLLM):
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key or settings.OPENAI_API_KEY
        self._provider = "openai"
        self._model = model or settings.DEFAULT_MODEL
        self.client = AsyncOpenAI(api_key=self.api_key)

    @property
    def provider(self) -> str:
        return self._provider

    @property
    def model(self) -> str:
        return self._model

    async def generate(self, prompt: str, **kwargs) -> str:
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            stream=False,
            **kwargs
        )
        return response.choices[0].message.content

    async def stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        async for chunk in await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            **kwargs
        ):
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

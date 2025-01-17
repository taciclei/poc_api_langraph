from typing import Dict, Optional, AsyncGenerator
from .interface.base_llm import BaseLLM, LLMResponse

class ModelManager:
    def __init__(self):
        self.providers: Dict[str, BaseLLM] = {}
        self.default_provider = None

    def register_provider(self, name: str, provider: BaseLLM, is_default: bool = False):
        self.providers[name] = provider
        if is_default or self.default_provider is None:
            self.default_provider = name

    async def generate(self, prompt: str, provider_name: Optional[str] = None, **kwargs) -> LLMResponse:
        provider = self._get_provider(provider_name)
        return await provider.generate(prompt, **kwargs)

    async def stream(self, prompt: str, provider_name: Optional[str] = None, **kwargs) -> AsyncGenerator[str, None]:
        provider = self._get_provider(provider_name)
        async for chunk in provider.stream(prompt, **kwargs):
            yield chunk

    def _get_provider(self, provider_name: Optional[str] = None) -> BaseLLM:
        if provider_name is None:
            provider_name = self.default_provider
        if provider_name not in self.providers:
            raise ValueError(f"Provider {provider_name} not found")
        return self.providers[provider_name]

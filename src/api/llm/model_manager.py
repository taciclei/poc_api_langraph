from typing import Dict, List, Optional
from .interface.base_llm import BaseLLM, LLMResponse
from .fallback.llm_manager import LLMManager
from ..cache.storage.tinydb_cache import TinyDBCache

class ModelManager:
    def __init__(self):
        self.cache = TinyDBCache("data/llm_cache.json")
        self.providers: Dict[str, BaseLLM] = {}
        self.fallback_manager: Optional[LLMManager] = None

    def register_provider(self, name: str, provider: BaseLLM):
        self.providers[name] = provider
        if self.fallback_manager is None:
            self.fallback_manager = LLMManager([provider])
        else:
            self.fallback_manager.providers.append(provider)

    async def generate(self,
                      prompt: str,
                      provider_name: Optional[str] = None,
                      use_cache: bool = True,
                      **kwargs) -> LLMResponse:
        if use_cache:
            cache_key = f"llm:{provider_name or 'fallback'}:{hash(prompt)}"
            cached_response = self.cache.get(cache_key)
            if cached_response:
                return LLMResponse(**cached_response)

        if provider_name:
            if provider_name not in self.providers:
                raise ValueError(f"Provider {provider_name} not found")
            response = await self.providers[provider_name].generate(prompt, **kwargs)
        else:
            if not self.fallback_manager:
                raise ValueError("No providers registered")
            response = await self.fallback_manager.generate_with_fallback(prompt, **kwargs)

        if use_cache:
            self.cache.set(cache_key, response.dict())

        return response

    async def stream(self,
                    prompt: str,
                    provider_name: Optional[str] = None,
                    **kwargs):
        if provider_name:
            if provider_name not in self.providers:
                raise ValueError(f"Provider {provider_name} not found")
            async for chunk in self.providers[provider_name].stream(prompt, **kwargs):
                yield chunk
        else:
            if not self.fallback_manager:
                raise ValueError("No providers registered")
            async for chunk in self.fallback_manager.stream_with_fallback(prompt, **kwargs):
                yield chunk

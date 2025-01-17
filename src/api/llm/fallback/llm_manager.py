from typing import List, Optional, Dict
from ..interface.base_llm import BaseLLM, LLMResponse

class LLMManager:
    def __init__(self, providers: List[BaseLLM], max_retries: int = 3):
        self.providers = providers
        self.max_retries = max_retries
        self._current_provider = 0

    async def generate_with_fallback(self, 
                                   prompt: str,
                                   max_tokens: Optional[int] = None,
                                   temperature: float = 0.7,
                                   stop_sequences: Optional[List[str]] = None) -> LLMResponse:
        errors = []
        retries = 0
        
        while retries < self.max_retries * len(self.providers):
            provider = self.providers[self._current_provider]
            try:
                response = await provider.generate(
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    stop_sequences=stop_sequences
                )
                return response
            except Exception as e:
                errors.append({
                    "provider": provider.__class__.__name__,
                    "error": str(e)
                })
                self._current_provider = (self._current_provider + 1) % len(self.providers)
                retries += 1
        
        raise Exception(f"All providers failed after {retries} attempts: {errors}")

    async def stream_with_fallback(self, 
                                 prompt: str,
                                 max_tokens: Optional[int] = None,
                                 temperature: float = 0.7,
                                 stop_sequences: Optional[List[str]] = None):
        errors = []
        retries = 0
        
        while retries < self.max_retries * len(self.providers):
            provider = self.providers[self._current_provider]
            try:
                async for chunk in provider.stream(
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    stop_sequences=stop_sequences
                ):
                    yield chunk
                return
            except Exception as e:
                errors.append({
                    "provider": provider.__class__.__name__,
                    "error": str(e)
                })
                self._current_provider = (self._current_provider + 1) % len(self.providers)
                retries += 1
        
        raise Exception(f"All providers failed after {retries} attempts: {errors}")

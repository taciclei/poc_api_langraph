from typing import Dict, List, Optional
import anthropic
from ..interface.base_llm import BaseLLM, LLMResponse

class AnthropicLLM(BaseLLM):
    def __init__(self, model_name: str = "claude-2", api_key: Optional[str] = None):
        self.model_name = model_name
        self.client = anthropic.Client(api_key=api_key)

    async def generate(self, 
                      prompt: str,
                      max_tokens: Optional[int] = None,
                      temperature: float = 0.7,
                      stop_sequences: Optional[List[str]] = None) -> LLMResponse:
        response = await self.client.messages.create(
            model=self.model_name,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return LLMResponse(
            text=response.content[0].text,
            tokens_used=response.usage.total_tokens,
            model_name=self.model_name,
            provider="anthropic",
            metadata={"stop_reason": response.stop_reason}
        )

    async def stream(self, 
                    prompt: str,
                    max_tokens: Optional[int] = None,
                    temperature: float = 0.7,
                    stop_sequences: Optional[List[str]] = None):
        async with self.client.messages.stream(
            model=self.model_name,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}]
        ) as stream:
            async for chunk in stream:
                if chunk.content:
                    yield chunk.content

    def get_token_count(self, text: str) -> int:
        # Utiliser l'estimateur de tokens d'Anthropic
        return self.client.count_tokens(text)

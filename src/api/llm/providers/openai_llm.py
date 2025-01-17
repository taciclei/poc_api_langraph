from typing import Dict, List, Optional
import openai
from ..interface.base_llm import BaseLLM, LLMResponse

class OpenAILLM(BaseLLM):
    def __init__(self, model_name: str = "gpt-3.5-turbo", api_key: Optional[str] = None):
        self.model_name = model_name
        if api_key:
            openai.api_key = api_key

    async def generate(self, 
                      prompt: str,
                      max_tokens: Optional[int] = None,
                      temperature: float = 0.7,
                      stop_sequences: Optional[List[str]] = None) -> LLMResponse:
        response = await openai.ChatCompletion.acreate(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
            stop=stop_sequences
        )
        
        return LLMResponse(
            text=response.choices[0].message.content,
            tokens_used=response.usage.total_tokens,
            model_name=self.model_name,
            provider="openai",
            metadata={"finish_reason": response.choices[0].finish_reason}
        )

    async def stream(self, 
                    prompt: str,
                    max_tokens: Optional[int] = None,
                    temperature: float = 0.7,
                    stop_sequences: Optional[List[str]] = None):
        async for chunk in await openai.ChatCompletion.acreate(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
            stop=stop_sequences,
            stream=True
        ):
            if chunk and chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    def get_token_count(self, text: str) -> int:
        # Utiliser tiktoken pour le comptage précis des tokens
        import tiktoken
        encoding = tiktoken.encoding_for_model(self.model_name)
        return len(encoding.encode(text))

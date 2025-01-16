from typing import Dict, List, Optional
import mistralai
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from ..interface.base_llm import BaseLLM, LLMResponse

class MistralLLM(BaseLLM):
    def __init__(self, api_key: str, model_name: str = "mistral-medium"):
        self.client = MistralClient(api_key=api_key)
        self.model_name = model_name

    async def generate(self, 
                      prompt: str,
                      max_tokens: Optional[int] = None,
                      temperature: float = 0.7,
                      stop_sequences: Optional[List[str]] = None) -> LLMResponse:
        messages = [ChatMessage(role="user", content=prompt)]
        
        response = self.client.chat(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stop=stop_sequences
        )
        
        return LLMResponse(
            text=response.choices[0].message.content,
            tokens_used=response.usage.total_tokens,
            model_name=self.model_name,
            provider="mistral",
            metadata={"finish_reason": response.choices[0].finish_reason}
        )

    async def stream(self, 
                    prompt: str,
                    max_tokens: Optional[int] = None,
                    temperature: float = 0.7,
                    stop_sequences: Optional[List[str]] = None):
        messages = [ChatMessage(role="user", content=prompt)]
        
        stream = self.client.chat_stream(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stop=stop_sequences
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    def get_token_count(self, text: str) -> int:
        # Estimation simple pour Mistral
        return len(text.split()) * 1.3

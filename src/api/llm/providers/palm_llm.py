from typing import Dict, List, Optional
import google.generativeai as palm
from ..interface.base_llm import BaseLLM, LLMResponse

class PaLMLLM(BaseLLM):
    def __init__(self, model_name: str = "models/text-bison-001", api_key: Optional[str] = None):
        self.model_name = model_name
        if api_key:
            palm.configure(api_key=api_key)

    async def generate(self, 
                      prompt: str,
                      max_tokens: Optional[int] = None,
                      temperature: float = 0.7,
                      stop_sequences: Optional[List[str]] = None) -> LLMResponse:
        response = palm.generate_text(
            model=self.model_name,
            prompt=prompt,
            temperature=temperature,
            max_output_tokens=max_tokens,
            stop_sequences=stop_sequences
        )
        
        return LLMResponse(
            text=response.result,
            tokens_used=len(response.result.split()),  # Estimation
            model_name=self.model_name,
            provider="palm",
            metadata={"safety_ratings": response.safety_ratings}
        )

    async def stream(self, 
                    prompt: str,
                    max_tokens: Optional[int] = None,
                    temperature: float = 0.7,
                    stop_sequences: Optional[List[str]] = None):
        response = palm.generate_text(
            model=self.model_name,
            prompt=prompt,
            temperature=temperature,
            max_output_tokens=max_tokens,
            stop_sequences=stop_sequences
        )
        # Simulation de streaming car PaLM ne supporte pas nativement le streaming
        words = response.result.split()
        for word in words:
            yield word + " "

    def get_token_count(self, text: str) -> int:
        # Estimation simple pour PaLM
        return len(text.split())

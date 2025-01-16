from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from pydantic import BaseModel

class LLMResponse(BaseModel):
    text: str
    tokens_used: int
    model_name: str
    provider: str
    metadata: Dict = {}

class BaseLLM(ABC):
    @abstractmethod
    async def generate(self, 
                      prompt: str, 
                      max_tokens: Optional[int] = None,
                      temperature: float = 0.7,
                      stop_sequences: Optional[List[str]] = None) -> LLMResponse:
        pass

    @abstractmethod
    async def stream(self, 
                    prompt: str,
                    max_tokens: Optional[int] = None,
                    temperature: float = 0.7,
                    stop_sequences: Optional[List[str]] = None):
        pass

    @abstractmethod
    def get_token_count(self, text: str) -> int:
        pass

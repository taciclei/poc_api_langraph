from abc import ABC, abstractmethod
from typing import AsyncGenerator, Optional, Dict
from pydantic import BaseModel

class LLMResponse(BaseModel):
    text: str
    usage: Optional[Dict] = None
    model: Optional[str] = None

class BaseLLM(ABC):
    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> LLMResponse:
        pass

    @abstractmethod
    async def stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        pass

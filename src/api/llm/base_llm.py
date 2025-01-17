from abc import ABC, abstractmethod
from typing import AsyncGenerator, Optional, Dict, Any

class BaseLLM(ABC):
    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> str:
        """Génère une réponse à partir d'un prompt"""
        pass

    @abstractmethod
    async def stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        """Stream une réponse à partir d'un prompt"""
        pass

    @property
    @abstractmethod
    def provider(self) -> str:
        """Retourne le nom du provider"""
        pass

    @property
    @abstractmethod
    def model(self) -> str:
        """Retourne le nom du modèle"""
        pass

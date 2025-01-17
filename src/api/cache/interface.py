from abc import ABC, abstractmethod
from typing import Any, Optional
from datetime import datetime

class CacheInterface(ABC):
    @abstractmethod
    async def get(self, key: str) -> Optional[Any]:
        """Récupère une valeur du cache"""
        pass

    @abstractmethod
    async def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        """Stocke une valeur dans le cache"""
        pass

    @abstractmethod
    async def delete(self, key: str) -> bool:
        """Supprime une valeur du cache"""
        pass

    @abstractmethod
    async def clear(self) -> bool:
        """Vide le cache"""
        pass

    @abstractmethod
    async def get_stats(self) -> dict:
        """Retourne les statistiques du cache"""
        pass

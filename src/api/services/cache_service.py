from typing import Any, Dict, Optional
from src.api.models.cache import CacheItem, CacheStats

class CacheService:
    def __init__(self):
        self._cache: Dict[str, Any] = {}
        self._stats = CacheStats()

    async def get(self, key: str) -> Optional[Any]:
        """Récupère une valeur du cache"""
        value = self._cache.get(key)
        if value is not None:
            self._stats.hits += 1
            return value
        self._stats.misses += 1
        return None

    async def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        """Stocke une valeur dans le cache"""
        self._cache[key] = value
        self._stats.keys = len(self._cache)
        return True

    async def delete(self, key: str) -> bool:
        """Supprime une valeur du cache"""
        if key in self._cache:
            del self._cache[key]
            self._stats.keys = len(self._cache)
            return True
        return False

    async def clear(self) -> bool:
        """Vide le cache"""
        self._cache.clear()
        self._stats = CacheStats()
        return True

    async def get_stats(self) -> CacheStats:
        """Récupère les statistiques du cache"""
        return self._stats

    async def get_all(self) -> Dict[str, Any]:
        """Récupère toutes les valeurs du cache"""
        return self._cache

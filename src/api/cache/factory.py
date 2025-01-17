from enum import Enum
from typing import Optional
from .interface import CacheInterface
from .tinydb_cache import TinyDBCache
from ..config import get_settings

class CacheType(Enum):
    """Types de cache disponibles"""
    TINYDB = "tinydb"
    # Possibilité d'ajouter d'autres types plus tard
    # SQLITE = "sqlite"
    # MEMORY = "memory"

class CacheFactory:
    """Factory pour créer des instances de cache"""
    _instances: dict = {}
    
    @classmethod
    async def get_cache(
        cls,
        cache_type: CacheType = CacheType.TINYDB,
        collection_name: str = "cache"
    ) -> CacheInterface:
        """
        Récupère une instance de cache
        Args:
            cache_type: Type de cache souhaité
            collection_name: Nom de la collection pour TinyDB
        Returns:
            Instance de cache
        """
        # Clé unique pour l'instance
        instance_key = f"{cache_type.value}_{collection_name}"
        
        # Retourner l'instance existante si elle existe
        if instance_key in cls._instances:
            return cls._instances[instance_key]
        
        # Créer une nouvelle instance
        settings = get_settings()
        
        if cache_type == CacheType.TINYDB:
            cache = TinyDBCache(
                db_path=settings.db_path,
                collection_name=collection_name
            )
        else:
            raise ValueError(f"Type de cache non supporté: {cache_type}")
        
        # Stocker l'instance
        cls._instances[instance_key] = cache
        return cache

    @classmethod
    async def clear_all(cls) -> None:
        """Vide tous les caches"""
        for cache in cls._instances.values():
            await cache.clear()

    @classmethod
    async def get_all_stats(cls) -> dict:
        """
        Récupère les statistiques de tous les caches
        Returns:
            Dict avec les stats par type de cache
        """
        stats = {}
        for key, cache in cls._instances.items():
            stats[key] = await cache.get_stats()
        return stats

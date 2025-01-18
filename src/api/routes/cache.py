from fastapi import APIRouter, HTTPException
from typing import Any, Dict

from src.api.models.cache import CacheItem, CacheStats
from src.api.services.cache_service import CacheService

router = APIRouter()
cache_service = CacheService()

@router.get("/{key}")
async def get_cache(key: str) -> Any:
    """Récupère une valeur du cache"""
    value = await cache_service.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return value

@router.put("/{key}")
async def set_cache(key: str, item: CacheItem) -> bool:
    """Stocke une valeur dans le cache"""
    return await cache_service.set(item.key, item.value, item.ttl)

@router.delete("/{key}")
async def delete_cache(key: str) -> bool:
    """Supprime une valeur du cache"""
    return await cache_service.delete(key)

@router.delete("/")
async def clear_cache() -> bool:
    """Vide le cache"""
    return await cache_service.clear()

@router.get("/stats")
async def get_cache_stats() -> CacheStats:
    """Récupère les statistiques du cache"""
    return await cache_service.get_stats()

@router.get("/")
async def list_cache() -> Dict[str, Any]:
    """Liste toutes les valeurs du cache"""
    return await cache_service.get_all()

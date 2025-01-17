from fastapi import APIRouter, HTTPException
from typing import Any, Optional

from ..cache.factory import CacheFactory, CacheType
from ..config import get_settings

router = APIRouter(
    prefix="/cache",
    tags=["cache"]
)

settings = get_settings()

@router.get("/{key}")
async def get_cache(key: str) -> Any:
    cache = await CacheFactory.get_cache(CacheType(settings.CACHE_TYPE))
    value = await cache.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return value

@router.put("/{key}")
async def set_cache(key: str, value: Any, ttl: Optional[int] = None) -> bool:
    cache = await CacheFactory.get_cache(CacheType(settings.CACHE_TYPE))
    return await cache.set(key, value, ttl)

@router.delete("/{key}")
async def delete_cache(key: str) -> bool:
    cache = await CacheFactory.get_cache(CacheType(settings.CACHE_TYPE))
    return await cache.delete(key)

@router.delete("/")
async def clear_cache() -> bool:
    cache = await CacheFactory.get_cache(CacheType(settings.CACHE_TYPE))
    return await cache.clear()

@router.get("/stats")
async def get_cache_stats() -> dict:
    cache = await CacheFactory.get_cache(CacheType(settings.CACHE_TYPE))
    return await cache.get_stats()

from fastapi import APIRouter, HTTPException
<<<<<<< HEAD
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
=======
from typing import Any, Dict, Optional
from pydantic import BaseModel

router = APIRouter()

class CacheItem(BaseModel):
    key: str
    value: Any
    ttl: Optional[int] = None

@router.get("/{key}")
async def get_cache(key: str):
    return {"key": key, "value": "cached_value"}

@router.post("/{key}")
async def set_cache(key: str, item: CacheItem):
    return item

@router.delete("/{key}")
async def delete_cache(key: str):
    return {"status": "deleted"}

@router.get("/")
async def list_cache():
    return {"items": []}
>>>>>>> release/1.1.0

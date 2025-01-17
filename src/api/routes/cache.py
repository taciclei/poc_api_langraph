from fastapi import APIRouter, HTTPException
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

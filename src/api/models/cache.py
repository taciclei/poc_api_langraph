from pydantic import BaseModel
from typing import Any, Optional

class CacheItem(BaseModel):
    key: str
    value: Any
    ttl: Optional[int] = None

class CacheStats(BaseModel):
    hits: int = 0
    misses: int = 0
    keys: int = 0
    memory_usage: int = 0

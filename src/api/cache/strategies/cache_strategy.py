from enum import Enum
from typing import Any, Optional
from datetime import timedelta

class CacheStrategy(Enum):
    ALWAYS = "always"
    NEVER = "never"
    CONDITIONAL = "conditional"

class CacheManager:
    def __init__(self, cache_backend):
        self.cache = cache_backend
        self.default_ttl = timedelta(hours=1)

    def cached_call(self, 
                   key: str, 
                   callback, 
                   strategy: CacheStrategy = CacheStrategy.ALWAYS,
                   ttl: Optional[timedelta] = None) -> Any:
        """
        Exécute une fonction avec cache selon la stratégie définie
        """
        if strategy == CacheStrategy.NEVER:
            return callback()

        cached_value = self.cache.get(key)
        if cached_value is not None:
            return cached_value

        result = callback()
        if strategy == CacheStrategy.ALWAYS or (
            strategy == CacheStrategy.CONDITIONAL and result is not None
        ):
            self.cache.set(key, result, ttl or self.default_ttl)
        
        return result

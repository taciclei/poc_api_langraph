from typing import Optional, Any
from datetime import timedelta
from ..cache.storage.tinydb_cache import TinyDBCache
from ..cache.strategies.cache_strategy import CacheManager, CacheStrategy

class CacheService:
    def __init__(self):
        self.cache_backend = TinyDBCache("data/cache.json")
        self.cache_manager = CacheManager(self.cache_backend)

    async def cache_llm_response(self, 
                               prompt: str, 
                               response: str, 
                               ttl: Optional[timedelta] = None) -> None:
        """Cache une réponse LLM"""
        key = f"llm_response:{hash(prompt)}"
        self.cache_backend.set(key, response, ttl)

    async def get_cached_llm_response(self, prompt: str) -> Optional[str]:
        """Récupère une réponse LLM cachée"""
        key = f"llm_response:{hash(prompt)}"
        return self.cache_backend.get(key)

    async def cache_graph_execution(self, 
                                  graph_id: str, 
                                  input_data: dict, 
                                  result: Any, 
                                  ttl: Optional[timedelta] = None) -> None:
        """Cache le résultat d'exécution d'un graphe"""
        key = f"graph_execution:{graph_id}:{hash(str(input_data))}"
        self.cache_backend.set(key, result, ttl)

    async def get_cached_graph_execution(self, 
                                       graph_id: str, 
                                       input_data: dict) -> Optional[Any]:
        """Récupère un résultat d'exécution de graphe caché"""
        key = f"graph_execution:{graph_id}:{hash(str(input_data))}"
        return self.cache_backend.get(key)

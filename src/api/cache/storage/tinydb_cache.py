from datetime import datetime, timedelta
from typing import Any, Optional
from tinydb import TinyDB, Query
from ..core.interface import CacheInterface

class TinyDBCache(CacheInterface):
    def __init__(self, db_path: str = "cache.json"):
        self.db = TinyDB(db_path)
        self.cache = self.db.table('cache')
        self.Query = Query()
        
        # Nettoyage initial des entrées expirées
        self._cleanup()

    def get(self, key: str) -> Optional[Any]:
        self._cleanup()  # Nettoyer les entrées expirées
        result = self.cache.get(self.Query.key == key)
        if result and (not result.get('expires_at') or 
                      datetime.fromisoformat(result['expires_at']) > datetime.now()):
            return result['value']
        return None

    def set(self, key: str, value: Any, ttl: Optional[timedelta] = None) -> None:
        expires_at = None
        if ttl:
            expires_at = (datetime.now() + ttl).isoformat()
        
        self.cache.upsert(
            {
                'key': key,
                'value': value,
                'expires_at': expires_at,
                'created_at': datetime.now().isoformat()
            },
            self.Query.key == key
        )

    def delete(self, key: str) -> None:
        self.cache.remove(self.Query.key == key)

    def clear(self) -> None:
        self.cache.truncate()

    def _cleanup(self) -> None:
        """Supprime les entrées expirées"""
        now = datetime.now().isoformat()
        self.cache.remove(
            (self.Query.expires_at.exists()) & 
            (self.Query.expires_at < now)
        )

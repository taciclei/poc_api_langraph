from typing import Optional, Any
from tinydb import TinyDB, Query
from datetime import datetime, timedelta
import json
from ..config import get_settings

settings = get_settings()

class TinyDBCache:
    def __init__(self):
        self.db = TinyDB(settings.DB_PATH)
        self.cache = self.db.table('cache')
        self.Query = Query()

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        """Stocke une valeur dans le cache"""
        expiration = None
        if ttl:
            expiration = (datetime.now() + timedelta(seconds=ttl)).isoformat()

        try:
            self.cache.upsert(
                {
                    'key': key,
                    'value': json.dumps(value),
                    'expiration': expiration
                },
                self.Query.key == key
            )
            return True
        except Exception:
            return False

    def get(self, key: str) -> Optional[Any]:
        """Récupère une valeur du cache"""
        result = self.cache.get(self.Query.key == key)
        if not result:
            return None

        if result['expiration']:
            expiration = datetime.fromisoformat(result['expiration'])
            if datetime.now() > expiration:
                self.delete(key)
                return None

        try:
            return json.loads(result['value'])
        except json.JSONDecodeError:
            return None

    def delete(self, key: str) -> bool:
        """Supprime une valeur du cache"""
        try:
            self.cache.remove(self.Query.key == key)
            return True
        except Exception:
            return False

    def clear(self) -> bool:
        """Vide le cache"""
        try:
            self.cache.truncate()
            return True
        except Exception:
            return False

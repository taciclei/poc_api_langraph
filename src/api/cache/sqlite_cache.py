import sqlite3
import json
import time
from typing import Any, Optional
from .interface import CacheInterface

class SQLiteCache(CacheInterface):
    def __init__(self, db_path: str = "cache.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS cache (
                    key TEXT PRIMARY KEY,
                    value TEXT,
                    expires_at INTEGER
                )
            """)
            conn.execute("PRAGMA journal_mode=WAL")

    async def get(self, key: str) -> Optional[Any]:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(
                "SELECT value, expires_at FROM cache WHERE key = ?",
                (key,)
            )
            row = cur.fetchone()
            if not row:
                return None
            value, expires_at = row
            if expires_at and time.time() > expires_at:
                await self.delete(key)
                return None
            return json.loads(value)

    async def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        expires_at = int(time.time() + ttl) if ttl else None
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    "INSERT OR REPLACE INTO cache (key, value, expires_at) VALUES (?, ?, ?)",
                    (key, json.dumps(value), expires_at)
                )
            return True
        except Exception:
            return False

    async def delete(self, key: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM cache WHERE key = ?", (key,))
            return True

    async def clear(self) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM cache")
            return True

    async def get_stats(self) -> dict:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute("""
                SELECT 
                    COUNT(*) as total,
                    SUM(CASE WHEN expires_at > ? THEN 1 ELSE 0 END) as active
                FROM cache
            """, (int(time.time()),))
            total, active = cur.fetchone()
            return {
                "total_entries": total,
                "active_entries": active,
                "expired_entries": total - active
            }

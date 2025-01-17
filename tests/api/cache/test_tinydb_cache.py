import pytest
from datetime import timedelta
from src.api.cache.storage.tinydb_cache import TinyDBCache

@pytest.fixture
def cache():
    return TinyDBCache("test_cache.json")

def test_set_get(cache):
    cache.set("test_key", "test_value")
    assert cache.get("test_key") == "test_value"

def test_ttl(cache):
    cache.set("ttl_key", "ttl_value", timedelta(seconds=1))
    assert cache.get("ttl_key") == "ttl_value"
    import time
    time.sleep(1.1)
    assert cache.get("ttl_key") is None

def test_delete(cache):
    cache.set("delete_key", "delete_value")
    cache.delete("delete_key")
    assert cache.get("delete_key") is None

def test_clear(cache):
    cache.set("key1", "value1")
    cache.set("key2", "value2")
    cache.clear()
    assert cache.get("key1") is None
    assert cache.get("key2") is None

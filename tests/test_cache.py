import pytest
from src.api.cache.interface import CacheInterface
from src.api.cache.factory import CacheFactory, CacheType

@pytest.mark.asyncio
async def test_cache_operations():
    cache = await CacheFactory.get_cache(CacheType.TINYDB)
    
    # Test set
    key = "test_key"
    value = "test_value"
    assert await cache.set(key, value)
    
    # Test get
    result = await cache.get(key)
    assert result == value
    
    # Test delete
    assert await cache.delete(key)
    assert await cache.get(key) is None

@pytest.mark.asyncio
async def test_cache_ttl():
    cache = await CacheFactory.get_cache(CacheType.TINYDB)
    
    # Set with TTL
    key = "ttl_key"
    value = "ttl_value"
    assert await cache.set(key, value, ttl=1)
    
    # Should exist initially
    assert await cache.get(key) == value
    
    # Wait for TTL
    import asyncio
    await asyncio.sleep(2)
    
    # Should be expired
    assert await cache.get(key) is None

@pytest.mark.asyncio
async def test_cache_clear():
    cache = await CacheFactory.get_cache(CacheType.TINYDB)
    
    # Add multiple entries
    for i in range(3):
        await cache.set(f"key_{i}", f"value_{i}")
    
    # Clear cache
    assert await cache.clear()
    
    # Verify all entries are gone
    for i in range(3):
        assert await cache.get(f"key_{i}") is None

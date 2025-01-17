from prometheus_client import Counter, Histogram, Gauge
import time

# Métriques pour le cache
cache_hits = Counter('cache_hits_total', 'Total number of cache hits')
cache_misses = Counter('cache_misses_total', 'Total number of cache misses')
cache_size = Gauge('cache_size_bytes', 'Current size of cache in bytes')
cache_operation_duration = Histogram(
    'cache_operation_duration_seconds',
    'Time spent on cache operations',
    ['operation']
)

class CacheMetrics:
    @staticmethod
    def record_hit():
        cache_hits.inc()

    @staticmethod
    def record_miss():
        cache_misses.inc()

    @staticmethod
    def update_size(size_bytes):
        cache_size.set(size_bytes)

    @staticmethod
    def time_operation(operation_name):
        return cache_operation_duration.labels(operation=operation_name).time()

# Exemple d'utilisation dans le cache
class MetricsWrapper:
    def __init__(self, cache_instance):
        self.cache = cache_instance

    async def get(self, key):
        with CacheMetrics.time_operation('get'):
            result = await self.cache.get(key)
            if result is None:
                CacheMetrics.record_miss()
            else:
                CacheMetrics.record_hit()
            return result

    async def set(self, key, value):
        with CacheMetrics.time_operation('set'):
            await self.cache.set(key, value)
            # Mettre à jour la taille du cache
            cache_size_bytes = await self.cache.get_size()
            CacheMetrics.update_size(cache_size_bytes)

from prometheus_client import Counter, Histogram, Gauge, CollectorRegistry
import time

class PrometheusMetrics:
    def __init__(self):
        self.registry = CollectorRegistry()
        
        # Métriques LLM
        self.llm_requests = Counter(
            'llm_requests_total',
            'Nombre total de requêtes LLM',
            ['provider', 'cache_hit'],
            registry=self.registry
        )
        
        self.llm_latency = Histogram(
            'llm_request_duration_seconds',
            'Temps de réponse des requêtes LLM',
            ['provider', 'cache_hit'],
            registry=self.registry
        )
        
        self.llm_tokens = Counter(
            'llm_tokens_total',
            'Nombre total de tokens utilisés',
            ['provider'],
            registry=self.registry
        )
        
        # Métriques Cache
        self.cache_size = Gauge(
            'cache_entries_total',
            'Nombre total d\'entrées en cache',
            ['type'],
            registry=self.registry
        )
        
        self.cache_hits = Counter(
            'cache_hits_total',
            'Nombre total de hits du cache',
            ['type'],
            registry=self.registry
        )
        
        self.cache_misses = Counter(
            'cache_misses_total',
            'Nombre total de misses du cache',
            ['type'],
            registry=self.registry
        )
        
        # Métriques Système
        self.api_requests = Counter(
            'api_requests_total',
            'Nombre total de requêtes API',
            ['endpoint', 'method', 'status'],
            registry=self.registry
        )
        
        self.api_latency = Histogram(
            'api_request_duration_seconds',
            'Temps de réponse des requêtes API',
            ['endpoint', 'method'],
            registry=self.registry
        )

metrics = PrometheusMetrics()

import pytest
from src.api.metrics.prometheus import metrics
from src.api.metrics.cache_metrics import CacheMetrics, CacheMetricsCollector

def test_prometheus_metrics():
    # Test counter increment
    metrics.llm_requests.labels(
        provider="test",
        cache_hit="false"
    ).inc()
    
    # Test histogram observation
    metrics.llm_latency.labels(
        provider="test",
        cache_hit="false"
    ).observe(0.1)
    
    # Verify metrics exist
    assert metrics.llm_requests._name == "llm_requests_total"
    assert metrics.llm_latency._name == "llm_request_duration_seconds"

def test_cache_metrics():
    collector = CacheMetricsCollector()
    
    # Test hit/miss recording
    collector.record_hit()
    collector.record_miss()
    collector.update_entries_count(5)
    
    # Get metrics
    metrics = collector.get_metrics()
    
    # Verify metrics
    assert metrics["hit_rate"] == 50.0  # 1 hit, 1 miss = 50%
    assert metrics["total_entries"] == 5
    assert "memory_usage_mb" in metrics
    assert "uptime_seconds" in metrics

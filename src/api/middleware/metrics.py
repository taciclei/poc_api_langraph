from fastapi import FastAPI
from fastapi.responses import JSONResponse
from prometheus_client import Counter, Histogram
import time

class Metrics:
    def __init__(self):
        self.llm_requests = {
            "total": Counter('llm_requests_total', 'Total LLM requests'),
            "latencies": Histogram('llm_latency_seconds', 'LLM request latencies')
        }
        self.http_requests = {
            "total": Counter('http_requests_total', 'Total HTTP requests'),
            "latencies": Histogram('http_latency_seconds', 'HTTP request latencies')
        }

metrics = Metrics()

def add_metrics_middleware(app: FastAPI) -> None:
    @app.middleware("http")
    async def metrics_middleware(request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        
        metrics.http_requests["total"].inc()
        metrics.http_requests["latencies"].observe(duration)
        
        return response

    @app.get("/metrics")
    async def get_metrics():
        return {
            "llm_requests_total": metrics.llm_requests["total"]._value.get(),
            "http_requests_total": metrics.http_requests["total"]._value.get(),
            "llm_latency_seconds": metrics.llm_requests["latencies"]._sum.get(),
            "http_latency_seconds": metrics.http_requests["latencies"]._sum.get()
        }

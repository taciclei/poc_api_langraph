from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import (
    health_routes,
    cache,
    graph_routes,
    llm_routes,
    execution_routes,
    metrics
)

app = FastAPI(
    title="LangGraph API",
    version="1.0.0",
    description="API for managing LangGraph operations"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes de base
app.include_router(health_routes.router, tags=["health"])
app.include_router(metrics.router, prefix="/metrics", tags=["metrics"])

# Routes principales
app.include_router(graph_routes.router, prefix="/api/v1/graphs", tags=["graphs"])
app.include_router(llm_routes.router, prefix="/api/v1/llm", tags=["llm"])
app.include_router(execution_routes.router, prefix="/api/v1/executions", tags=["executions"])
app.include_router(cache.router, prefix="/api/v1/cache", tags=["cache"])

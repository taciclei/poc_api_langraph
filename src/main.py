from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import (
    health_routes,
    cache,
    graph_routes,
    llm_routes,
    execution_routes,
    metrics,
    monitoring_routes,
    model_routes,
    prompt_routes,
    chain_routes,
    tool_routes,
    workflow_routes,
    agent_routes
)

app = FastAPI(
    title="LangGraph API",
    version="1.1.0",
    description="API for managing LangGraph operations"
)

# CORS
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

# Nouvelles routes
app.include_router(monitoring_routes.router, prefix="/api/v1/monitoring", tags=["monitoring"])
app.include_router(model_routes.router, prefix="/api/v1/models", tags=["models"])
app.include_router(prompt_routes.router, prefix="/api/v1/prompts", tags=["prompts"])
app.include_router(chain_routes.router, prefix="/api/v1/chains", tags=["chains"])
app.include_router(tool_routes.router, prefix="/api/v1/tools", tags=["tools"])
app.include_router(workflow_routes.router, prefix="/api/v1/workflows", tags=["workflows"])
app.include_router(agent_routes.router, prefix="/api/v1/agents", tags=["agents"])

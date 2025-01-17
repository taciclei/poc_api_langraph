from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
<<<<<<< HEAD
from .config import get_settings
from .routes import cache, llm_routes, graph_routes, health_routes
from .middleware.metrics import add_metrics_middleware

settings = get_settings()

app = FastAPI(
    title="LangGraph API",
    description="API pour la gestion de graphes LLM",
    version="1.1.0"
)

# CORS
=======
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

>>>>>>> release/1.1.0
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
# Metrics
add_metrics_middleware(app)

# Routes
app.include_router(health_routes.router, tags=["health"])
app.include_router(cache.router, prefix="/cache", tags=["cache"])
app.include_router(llm_routes.router, tags=["llm"])
app.include_router(graph_routes.router, prefix="/graphs", tags=["graphs"])
=======
# Routes de base
app.include_router(health_routes.router, tags=["health"])
app.include_router(metrics.router, prefix="/metrics", tags=["metrics"])

# Routes principales
app.include_router(graph_routes.router, prefix="/api/v1/graphs", tags=["graphs"])
app.include_router(llm_routes.router, prefix="/api/v1/llm", tags=["llm"])
app.include_router(execution_routes.router, prefix="/api/v1/executions", tags=["executions"])
app.include_router(cache.router, prefix="/api/v1/cache", tags=["cache"])
>>>>>>> release/1.1.0

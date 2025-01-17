from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Metrics
add_metrics_middleware(app)

# Routes
app.include_router(health_routes.router, tags=["health"])
app.include_router(cache.router, prefix="/cache", tags=["cache"])
app.include_router(llm_routes.router, tags=["llm"])
app.include_router(graph_routes.router, prefix="/graphs", tags=["graphs"])

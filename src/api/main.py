from fastapi import FastAPI
from src.api.routes import health_routes, graph_routes

app = FastAPI(title="Graph API")

app.include_router(health_routes.router, prefix="/health", tags=["health"])
app.include_router(graph_routes.router, prefix="/graph", tags=["graph"])

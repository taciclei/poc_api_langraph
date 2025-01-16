from fastapi import FastAPI
from src.api.routes import health_routes, graph_routes
from src.api.routes.execution import execution_routes

app = FastAPI(title="LangGraph API")

app.include_router(health_routes.router, prefix="/health", tags=["health"])
app.include_router(graph_routes.router, prefix="/graph", tags=["graph"])
app.include_router(execution_routes.router, tags=["execution"])

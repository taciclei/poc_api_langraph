from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import health_routes, graph_routes, llm_routes
from .services.llm_service import LLMService

app = FastAPI(
    title="LangGraph API",
    description="API for managing and executing language model graphs",
    version="1.1.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialisation des services
llm_service = LLMService()

# Enregistrement des routes
app.include_router(health_routes.router)
app.include_router(graph_routes.router)
app.include_router(
    llm_routes.router,
    dependencies=[Depends(lambda: llm_service)]
)

@app.on_event("startup")
async def startup_event():
    # Initialisation au démarrage
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Nettoyage à l'arrêt
    pass

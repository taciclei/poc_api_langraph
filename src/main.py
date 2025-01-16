from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import graph_routes
from .core.db import DBConfig

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    DBConfig.connect()

@app.on_event("shutdown")
def shutdown():
    DBConfig.close()

# Routes
app.include_router(graph_routes.router)
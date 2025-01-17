from fastapi import FastAPI
from src.api.routes.llm_routes import router as llm_router

app = FastAPI(title="LangGraph API")

app.include_router(llm_router)

@app.get("/")
async def root():
    return {"message": "Welcome to LangGraph API"}

from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List

router = APIRouter()

@router.get("/")
async def list_graphs():
    """Liste tous les graphes disponibles"""
    return {"graphs": []}

@router.post("/")
async def create_graph(graph_data: Dict[str, Any]):
    """Crée un nouveau graphe"""
    return {"id": "new-graph-id"}

@router.get("/{graph_id}")
async def get_graph(graph_id: str):
    """Récupère les détails d'un graphe"""
    return {"id": graph_id}

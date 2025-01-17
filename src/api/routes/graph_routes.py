from fastapi import APIRouter, HTTPException
from typing import List

from src.api.models.graph import Graph, GraphCreate, GraphUpdate
from src.api.services.graph_service import GraphService

router = APIRouter()
graph_service = GraphService()

@router.post("/", response_model=Graph)
async def create_graph(graph_data: GraphCreate):
    """Crée un nouveau graphe"""
    return await graph_service.create_graph(graph_data)

@router.get("/{graph_id}", response_model=Graph)
async def get_graph(graph_id: str):
    """Récupère un graphe par son ID"""
    graph = await graph_service.get_graph(graph_id)
    if not graph:
        raise HTTPException(status_code=404, detail="Graph not found")
    return graph

@router.put("/{graph_id}", response_model=Graph)
async def update_graph(graph_id: str, graph_data: GraphUpdate):
    """Met à jour un graphe existant"""
    graph = await graph_service.update_graph(graph_id, graph_data)
    if not graph:
        raise HTTPException(status_code=404, detail="Graph not found")
    return graph

@router.delete("/{graph_id}")
async def delete_graph(graph_id: str):
    """Supprime un graphe"""
    success = await graph_service.delete_graph(graph_id)
    if not success:
        raise HTTPException(status_code=404, detail="Graph not found")
    return {"status": "success"}

@router.get("/", response_model=List[Graph])
async def list_graphs(skip: int = 0, limit: int = 10):
    """Liste tous les graphes avec pagination"""
    return await graph_service.list_graphs(skip=skip, limit=limit)

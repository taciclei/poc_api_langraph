from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List
from ..services.graph_service import graph_service
from ..models.graph import Graph, GraphCreate, GraphUpdate

router = APIRouter()

@router.post("/graphs", response_model=Graph)
async def create_graph(graph_data: GraphCreate):
    """Crée un nouveau graphe"""
    return await graph_service.create_graph(graph_data.dict())

@router.get("/graphs/{graph_id}", response_model=Graph)
async def get_graph(graph_id: str):
    """Récupère un graphe par son ID"""
    graph = await graph_service.get_graph(graph_id)
    if not graph:
        raise HTTPException(status_code=404, detail="Graph not found")
    return graph

@router.get("/graphs", response_model=List[Graph])
async def list_graphs(skip: int = 0, limit: int = 10):
    """Liste tous les graphes avec pagination"""
    return await graph_service.list_graphs(skip=skip, limit=limit)

@router.get("/graphs/{graph_id}/export")
async def export_graph(graph_id: str):
    """Exporte un graphe"""
    try:
        graph = await graph_service.get_graph(graph_id)
        if not graph:
            raise HTTPException(status_code=404, detail="Graph not found")
        return graph.dict()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/graphs/import")
async def import_graph(graph_data: Dict[str, Any]):
    """Importe un graphe"""
    try:
        return await graph_service.create_graph(graph_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

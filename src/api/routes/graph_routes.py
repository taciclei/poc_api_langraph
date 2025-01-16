from fastapi import APIRouter, Query
from typing import List, Optional
from ..models.graph import GraphCreate, GraphUpdate
from ..services.graph_service import GraphService

router = APIRouter(prefix="/api/v1")

@router.post("/graphs", response_model=dict)
def create_graph(graph: GraphCreate):
    return GraphService.create_graph(graph.dict())

@router.get("/graphs/{graph_id}", response_model=dict)
def get_graph(graph_id: str):
    return GraphService.get_graph(graph_id)

@router.get("/graphs", response_model=List[dict])
def list_graphs(
    status: Optional[str] = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1)
):
    return GraphService.list_graphs(status, skip, limit)

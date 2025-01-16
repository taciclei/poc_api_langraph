from fastapi import APIRouter, HTTPException
from typing import List
from ..models.edge import EdgeCreate, EdgeUpdate
from ..services.edge_service import EdgeService

router = APIRouter(prefix="/api/v1")

@router.post("/graphs/{graph_id}/edges", response_model=dict)
def create_edge(graph_id: str, edge: EdgeCreate):
    return EdgeService.create_edge(graph_id, edge.dict())

@router.get("/graphs/{graph_id}/edges", response_model=List[dict])
def list_edges(graph_id: str):
    return EdgeService.list_edges(graph_id)

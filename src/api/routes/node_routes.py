from fastapi import APIRouter, HTTPException
from typing import List
from ..models.node import NodeCreate, NodeUpdate
from ..services.node_service import NodeService

router = APIRouter(prefix="/api/v1")

@router.post("/graphs/{graph_id}/nodes", response_model=dict)
def create_node(graph_id: str, node: NodeCreate):
    return NodeService.create_node(graph_id, node.dict())

@router.get("/graphs/{graph_id}/nodes", response_model=List[dict])
def list_nodes(graph_id: str):
    return NodeService.list_nodes(graph_id)

@router.get("/nodes/{node_id}", response_model=dict)
def get_node(node_id: str):
    return NodeService.get_node(node_id)

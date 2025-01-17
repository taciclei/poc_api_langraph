from fastapi import APIRouter
from src.api.models.node import Node
from src.api.services.node_service import NodeService

router = APIRouter()

@router.post("/", status_code=201)
async def create_node(node: Node):
    service = NodeService()
    return await service.create_node(node)

@router.get("/{node_id}")
async def get_node(node_id: str):
    service = NodeService()
    return await service.get_node(node_id)

@router.get("/graph/{graph_id}")
async def list_nodes(graph_id: str):
    service = NodeService()
    return await service.list_nodes(graph_id)

@router.put("/{node_id}")
async def update_node(node_id: str, node: Node):
    service = NodeService()
    return await service.update_node(node_id, node)

@router.delete("/{node_id}")
async def delete_node(node_id: str):
    service = NodeService()
    return await service.delete_node(node_id)

from fastapi import APIRouter
from src.api.models.edge import Edge
from src.api.services.edge_service import EdgeService

router = APIRouter()

@router.post("/", status_code=201)
async def create_edge(edge: Edge):
    service = EdgeService()
    return await service.create_edge(edge)

@router.get("/{edge_id}")
async def get_edge(edge_id: str):
    service = EdgeService()
    return await service.get_edge(edge_id)

@router.get("/graph/{graph_id}")
async def list_edges(graph_id: str):
    service = EdgeService()
    return await service.list_edges(graph_id)

@router.put("/{edge_id}")
async def update_edge(edge_id: str, edge: Edge):
    service = EdgeService()
    return await service.update_edge(edge_id, edge)

@router.delete("/{edge_id}")
async def delete_edge(edge_id: str):
    service = EdgeService()
    return await service.delete_edge(edge_id)

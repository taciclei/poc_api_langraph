from fastapi import APIRouter, HTTPException
from typing import List
from src.api.services.graph_service import GraphService
from src.api.models.graph import Graph, GraphResponse

router = APIRouter()

@router.post("/", response_model=GraphResponse, status_code=201)
async def create_graph(graph: Graph):
    service = GraphService()
    return await service.create_graph(graph)

@router.get("/{graph_id}", response_model=GraphResponse)
async def get_graph(graph_id: str):
    service = GraphService()
    return await service.get_graph(graph_id)

@router.get("/", response_model=List[GraphResponse])
async def list_graphs():
    service = GraphService()
    return await service.list_graphs()

@router.put("/{graph_id}", response_model=GraphResponse)
async def update_graph(graph_id: str, graph: Graph):
    service = GraphService()
    return await service.update_graph(graph_id, graph)

@router.delete("/{graph_id}")
async def delete_graph(graph_id: str):
    service = GraphService()
    return await service.delete_graph(graph_id)

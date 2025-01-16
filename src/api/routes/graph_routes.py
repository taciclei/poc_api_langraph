from fastapi import APIRouter, HTTPException
from typing import Dict, List
from pydantic import BaseModel
from src.api.services.graph_service import GraphService

router = APIRouter()
graph_service = GraphService()

class Edge(BaseModel):
    source: str
    target: str

class GraphCreate(BaseModel):
    name: str
    description: str
    nodes: List[str]
    edges: List[Edge]

@router.post("/create")
def create_graph(graph: GraphCreate):
    """Create a new graph"""
    try:
        result = graph_service.create_graph(
            name=graph.name,
            description=graph.description,
            nodes=graph.nodes,
            edges=[edge.dict() for edge in graph.edges]
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": str(e)})

@router.get("/get/{graph_id}")
def get_graph(graph_id: str):
    """Get a graph by ID"""
    graph = graph_service.get_graph(graph_id)
    if not graph:
        raise HTTPException(status_code=404, detail={"message": "Graph not found"})
    return graph

@router.delete("/delete/{graph_id}")
def delete_graph(graph_id: str):
    """Delete a graph"""
    if not graph_service.delete_graph(graph_id):
        raise HTTPException(status_code=404, detail={"message": "Graph not found"})
    return {"message": "Graph deleted successfully"}

@router.get("/list")
def list_graphs():
    """List all graphs"""
    return graph_service.list_graphs()

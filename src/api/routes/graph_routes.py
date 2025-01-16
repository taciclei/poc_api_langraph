from fastapi import APIRouter, Query
from typing import List, Optional
from ..models.graph import GraphCreate, GraphUpdate
from ..models.node import NodeCreate, NodeUpdate
from ..models.edge import EdgeCreate, EdgeUpdate
from ..services.graph_service import GraphService
from ..services.node_service import NodeService
from ..services.edge_service import EdgeService
from ..services.execution_service import ExecutionService

router = APIRouter(prefix="/api/v1")

# Routes pour les graphes
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

@router.put("/graphs/{graph_id}", response_model=dict)
def update_graph(graph_id: str, graph: GraphUpdate):
    return GraphService.update_graph(graph_id, graph.dict(exclude_unset=True))

@router.delete("/graphs/{graph_id}")
def delete_graph(graph_id: str):
    return GraphService.delete_graph(graph_id)

# Routes pour les nœuds
@router.post("/graphs/{graph_id}/nodes", response_model=dict)
def add_node(graph_id: str, node: NodeCreate):
    return NodeService.add_node(graph_id, node.dict())

@router.get("/graphs/{graph_id}/nodes", response_model=List[dict])
def list_nodes(
    graph_id: str,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1)
):
    return NodeService.list_nodes(graph_id, skip, limit)

# Routes pour les arêtes
@router.post("/graphs/{graph_id}/edges", response_model=dict)
def add_edge(graph_id: str, edge: EdgeCreate):
    return EdgeService.add_edge(graph_id, edge.dict())

@router.get("/graphs/{graph_id}/edges", response_model=List[dict])
def list_edges(
    graph_id: str,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1)
):
    return EdgeService.list_edges(graph_id, skip, limit)

# Routes pour les exécutions
@router.post("/graphs/{graph_id}/execute", response_model=dict)
def execute_graph(graph_id: str, inputs: dict):
    return ExecutionService.execute_graph(graph_id, inputs)

@router.get("/executions/{execution_id}", response_model=dict)
def get_execution(execution_id: str):
    return ExecutionService.get_execution(execution_id)

@router.get("/graphs/{graph_id}/executions", response_model=List[dict])
def list_executions(
    graph_id: str,
    status: Optional[str] = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1)
):
    return ExecutionService.list_executions(graph_id, status, skip, limit)
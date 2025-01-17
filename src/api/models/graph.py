from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class Node(BaseModel):
    id: Optional[str] = None
    name: str
    type: str
    graph_id: Optional[str] = None
    properties: Optional[Dict[str, Any]] = {}

class Edge(BaseModel):
    id: Optional[str] = None
    source_id: str
    target_id: str
    graph_id: Optional[str] = None
    properties: Optional[Dict[str, Any]] = {}

class Graph(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    nodes: List[Node] = []
    edges: List[Edge] = []
    properties: Optional[Dict[str, Any]] = {}

class GraphResponse(BaseModel):
    id: str
    name: str
    description: str
    nodes: List[Node]
    edges: List[Edge]
    properties: Dict[str, Any] = {}

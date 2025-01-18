from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class Node(BaseModel):
    id: str
    type: str
    position: Dict[str, float]
    data: Dict[str, Any]

class Edge(BaseModel):
    id: str
    source: str
    target: str
    type: str = "default"
    data: Dict[str, Any] = Field(default_factory=dict)

class GraphBase(BaseModel):
    name: str
    description: str = ""
    nodes: List[Node] = Field(default_factory=list)
    edges: List[Edge] = Field(default_factory=list)

class GraphCreate(GraphBase):
    pass

class GraphUpdate(GraphBase):
    name: Optional[str] = None
    description: Optional[str] = None
    nodes: Optional[List[Node]] = None
    edges: Optional[List[Edge]] = None

class Graph(GraphBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

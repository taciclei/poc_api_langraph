from pydantic import BaseModel
from typing import List, Dict, Optional

class Graph(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    nodes: List[str]
    edges: List[Dict[str, str]]

class GraphCreate(BaseModel):
    name: str
    description: Optional[str] = None
    nodes: List[str]
    edges: List[Dict[str, str]]

class GraphUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    nodes: Optional[List[str]] = None
    edges: Optional[List[Dict[str, str]]] = None

from pydantic import BaseModel
from typing import List, Dict, Optional

class GraphRequest(BaseModel):
    name: str
    description: Optional[str] = None
    nodes: List[str]
    edges: List[Dict[str, str]]

class GraphResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    nodes: List[str]
    edges: List[Dict[str, str]]

from pydantic import BaseModel
from typing import Optional, Dict, Any

class EdgeBase(BaseModel):
    source_id: str
    target_id: str
    graph_id: str
    type: str = "default"
    metadata: Optional[Dict[str, Any]] = None
    config: Optional[Dict[str, Any]] = None

class EdgeCreate(EdgeBase):
    pass

class EdgeUpdate(EdgeBase):
    type: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    config: Optional[Dict[str, Any]] = None

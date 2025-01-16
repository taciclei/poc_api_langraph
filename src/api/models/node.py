from pydantic import BaseModel
from typing import Optional, Dict, Any

class NodeBase(BaseModel):
    name: str
    type: str
    graph_id: str
    config: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    position_x: Optional[float] = 0
    position_y: Optional[float] = 0

class NodeCreate(NodeBase):
    pass

class NodeUpdate(NodeBase):
    name: Optional[str] = None
    type: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

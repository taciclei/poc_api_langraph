from pydantic import BaseModel
from typing import Optional, Dict, Any

class NodeBase(BaseModel):
    name: str
    type: str
    config: Dict[str, Any]
    metadata: Optional[Dict] = None

class NodeCreate(NodeBase):
    pass

class NodeUpdate(NodeBase):
    name: Optional[str] = None
    type: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
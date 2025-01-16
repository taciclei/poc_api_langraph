from pydantic import BaseModel
from typing import Optional, Dict, Any

class EdgeBase(BaseModel):
    source_id: str
    target_id: str
    condition: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict] = None

class EdgeCreate(EdgeBase):
    pass

class EdgeUpdate(EdgeBase):
    source_id: Optional[str] = None
    target_id: Optional[str] = None
    condition: Optional[Dict[str, Any]] = None
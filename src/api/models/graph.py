from pydantic import BaseModel
from typing import Optional, Dict

class GraphBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: Optional[str] = "draft"
    metadata: Optional[Dict] = None

class GraphCreate(GraphBase):
    pass

class GraphUpdate(GraphBase):
    name: Optional[str] = None

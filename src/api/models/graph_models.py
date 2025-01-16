from typing import Dict, Optional, List, Any
from pydantic import BaseModel, Field

class JSONAPIResource(BaseModel):
    id: str
    type: str
    attributes: Dict
    relationships: Optional[Dict] = None
    links: Optional[Dict] = None

class GraphAttributes(BaseModel):
    name: str
    definition: Dict
    status: str = "inactive"
    metadata: Dict = Field(default_factory=dict)
    config: Optional[Dict] = Field(default_factory=dict)

class GraphResource(JSONAPIResource):
    type: str = "graph"
    attributes: GraphAttributes

class GraphExecutionAttributes(BaseModel):
    graph_id: str
    inputs: Dict
    status: str = "pending"
    result: Optional[Dict] = None
    metadata: Dict = Field(default_factory=dict)

class GraphExecutionResource(JSONAPIResource):
    type: str = "graph-execution"
    attributes: GraphExecutionAttributes

class NodeAttributes(BaseModel):
    name: str
    type: str
    config: Dict = Field(default_factory=dict)
    metadata: Dict = Field(default_factory=dict)

class NodeResource(JSONAPIResource):
    type: str = "node"
    attributes: NodeAttributes

class EdgeAttributes(BaseModel):
    source_id: str
    target_id: str
    condition: Optional[str] = None
    metadata: Dict = Field(default_factory=dict)

class EdgeResource(JSONAPIResource):
    type: str = "edge"
    attributes: EdgeAttributes

class JSONAPIResponse(BaseModel):
    data: JSONAPIResource | List[JSONAPIResource]
    included: Optional[List[JSONAPIResource]] = None
    meta: Optional[Dict] = None